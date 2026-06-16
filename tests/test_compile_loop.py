import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPILE = ROOT / "scripts" / "compile_loop.py"
CHECK = ROOT / "scripts" / "check_loop.py"
STANDARD_LOOP_FILES = {
    "TARGET.md",
    "PATH.md",
    "ACCEPTANCE.md",
    "STATE.md",
    "LOOP_LOG.md",
    "STOP_GATE.md",
    "HANDOFF.md",
    "WORK_ORDER.md",
}


def run_cmd(*args, cwd=ROOT):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def file_hashes(target: Path):
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(target.glob("*.md"))
    }


class CompileLoopCliTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.intent = Path(self.tempdir.name) / "intent.md"
        self.intent.write_text(
            """# Intent Brief

## Goal

Build a safe loop compiler.

## Scope

Compile a brief into a proposed loop package.

## Non-goals

- Do not write files.
- Do not execute agents.

## Inputs

- An intent markdown file.

## Outputs

- Structured proposed loop data.

## Constraints

- Read-only.
- Standard library only.

## Acceptance

- Parse sections.
- Emit JSON.

## Risks

- Missing sections should be reported.

## HumanGate

- Writing files requires explicit approval.
""",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tempdir.cleanup()

    def test_valid_intent_prints_compiler_briefing(self):
        result = run_cmd(sys.executable, str(COMPILE), "--intent", str(self.intent))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("Xunhuan compile loop: READY", result.stdout)
        self.assertIn("Goal: Build a safe loop compiler.", result.stdout)
        self.assertIn("Scope: Compile a brief into a proposed loop package.", result.stdout)
        self.assertIn("Non-goals:", result.stdout)
        self.assertIn("Proposed loop:", result.stdout)
        self.assertIn("does not write files or execute agents", result.stdout)

    def test_json_output_contains_proposed_loop_contract(self):
        result = run_cmd(sys.executable, str(COMPILE), "--intent", str(self.intent), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertIs(payload["ok"], True)
        self.assertEqual(payload["goal"], "Build a safe loop compiler.")
        self.assertEqual(payload["scope"], "Compile a brief into a proposed loop package.")
        self.assertIn("Do not write files.", payload["non_goals"])
        self.assertIn("TARGET.md", payload["proposed_loop"])
        self.assertIn("WORK_ORDER.md", payload["proposed_loop"])
        self.assertEqual(payload["issues"], [])

    def test_missing_sections_report_errors(self):
        self.intent.write_text("# Intent Brief\n\n## Goal\n\nOnly goal.\n", encoding="utf-8")
        result = run_cmd(sys.executable, str(COMPILE), "--intent", str(self.intent))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("NOT READY", result.stdout)
        self.assertIn("missing", result.stdout.lower())

    def test_compiler_is_read_only(self):
        before = file_hashes(self.intent.parent)
        result = run_cmd(sys.executable, str(COMPILE), "--intent", str(self.intent), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        after = file_hashes(self.intent.parent)
        self.assertEqual(before, after)

    def test_json_is_parseable(self):
        result = run_cmd(sys.executable, str(COMPILE), "--intent", str(self.intent), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        json.loads(result.stdout)

    def test_write_requires_target_dir(self):
        result = run_cmd(sys.executable, str(COMPILE), "--intent", str(self.intent), "--write")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--dir", result.stderr + result.stdout)

    def test_write_creates_standard_loop_files_that_pass_check(self):
        target = Path(self.tempdir.name) / "target-project"
        target.mkdir()

        result = run_cmd(
            sys.executable,
            str(COMPILE),
            "--intent",
            str(self.intent),
            "--write",
            "--dir",
            str(target),
        )

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("Files written:", result.stdout)
        loop_dir = target / ".loop"
        self.assertEqual({path.name for path in loop_dir.glob("*.md")}, STANDARD_LOOP_FILES)
        check = run_cmd(sys.executable, str(CHECK), "--dir", str(target))
        self.assertEqual(check.returncode, 0, check.stderr + check.stdout)

    def test_write_json_reports_guarded_write_fields(self):
        target = Path(self.tempdir.name) / "json-target"
        target.mkdir()

        result = run_cmd(
            sys.executable,
            str(COMPILE),
            "--intent",
            str(self.intent),
            "--write",
            "--dir",
            str(target),
            "--json",
        )

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertIs(payload["ok"], True)
        self.assertIs(payload["write"], True)
        self.assertEqual(payload["target_dir"], str(target.resolve()))
        self.assertEqual({Path(path).name for path in payload["written_files"]}, STANDARD_LOOP_FILES)
        self.assertEqual(payload["issues"], [])

    def test_write_refuses_overwrite_without_force(self):
        target = Path(self.tempdir.name) / "overwrite-target"
        loop_dir = target / ".loop"
        loop_dir.mkdir(parents=True)
        existing = loop_dir / "TARGET.md"
        existing.write_text("existing target\n", encoding="utf-8")

        result = run_cmd(
            sys.executable,
            str(COMPILE),
            "--intent",
            str(self.intent),
            "--write",
            "--dir",
            str(target),
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("refusing to overwrite", result.stderr + result.stdout)
        self.assertEqual(existing.read_text(encoding="utf-8"), "existing target\n")

    def test_force_overwrites_existing_loop_files(self):
        target = Path(self.tempdir.name) / "force-target"
        loop_dir = target / ".loop"
        loop_dir.mkdir(parents=True)
        existing = loop_dir / "TARGET.md"
        existing.write_text("existing target\n", encoding="utf-8")

        result = run_cmd(
            sys.executable,
            str(COMPILE),
            "--intent",
            str(self.intent),
            "--write",
            "--dir",
            str(target),
            "--force",
        )

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertNotEqual(existing.read_text(encoding="utf-8"), "existing target\n")
        self.assertIn("Build a safe loop compiler.", existing.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
