import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLANNER = ROOT / "scripts" / "plan_next.py"
INIT = ROOT / "scripts" / "init_loop.py"


def run_cmd(*args, cwd=ROOT):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def loop_hashes(target):
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted((target / ".loop").glob("*.md"))
    }


class PlanNextCliTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.target = Path(self.tempdir.name)
        result = run_cmd(sys.executable, str(INIT), "--name", "planner-loop", "--dir", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.work_order = self.target / ".loop" / "WORK_ORDER.md"
        self.work_order.write_text(
            """# WORK_ORDER - Round 1

## Objective

Build a tiny planner.

## Allowed files

- scripts/plan_next.py
- tests/test_plan_next.py

## Forbidden files/directories

Do not modify:

- 00_CONCEPT/
- 01_PROTOCOL/

## Requirements

1. Parse work order sections.
2. Emit JSON.

```bash
python scripts/plan_next.py --dir .
```

## Required verification before returning

Run:

```bash
python scripts/plan_next.py --help
python tests/test_plan_next.py -v
```

- Verify invalid loop fails.

## Completion report

Return:

- Files changed.
- Commands run.
""",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tempdir.cleanup()

    def test_valid_work_order_prints_plan_briefing(self):
        result = run_cmd(sys.executable, str(PLANNER), "--dir", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("Xunhuan plan next: READY", result.stdout)
        self.assertIn("Objective: Build a tiny planner.", result.stdout)
        self.assertIn("Execution checklist:", result.stdout)
        self.assertIn("scripts/plan_next.py", result.stdout)
        self.assertIn("Required verification:", result.stdout)
        self.assertIn("does not execute agents or commands", result.stdout)

    def test_json_output_contains_plan_contract(self):
        result = run_cmd(sys.executable, str(PLANNER), "--dir", str(self.target), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertIs(payload["ok"], True)
        self.assertEqual(payload["objective"], "Build a tiny planner.")
        self.assertIn("scripts/plan_next.py", payload["allowed_files"])
        self.assertIn("00_CONCEPT/", payload["forbidden_files"])
        self.assertTrue(any("Parse work order sections" in item for item in payload["requirements"]))
        self.assertTrue(any("python scripts/plan_next.py --help" in item for item in payload["required_verification"]))
        self.assertIn("Files changed.", " ".join(payload["completion_report"]))
        self.assertEqual(payload["issues"], [])

    def test_invalid_loop_surfaces_checker_issues_and_exits_nonzero(self):
        (self.target / ".loop" / "STATE.md").unlink()
        result = run_cmd(sys.executable, str(PLANNER), "--dir", str(self.target))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("NOT READY", result.stdout)
        self.assertIn("STATE.md", result.stdout)

    def test_planner_is_read_only_for_loop_files(self):
        before = loop_hashes(self.target)
        result = run_cmd(sys.executable, str(PLANNER), "--dir", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        after = loop_hashes(self.target)
        self.assertEqual(before, after)

    def test_missing_optional_sections_return_empty_lists_not_failure(self):
        self.work_order.write_text(
            "# WORK_ORDER\n\n## Objective\n\nOnly objective.\n\n## Allowed files\n\n## Required verification before returning\n",
            encoding="utf-8",
        )
        result = run_cmd(sys.executable, str(PLANNER), "--dir", str(self.target), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["objective"], "Only objective.")
        self.assertEqual(payload["allowed_files"], [])
        self.assertEqual(payload["requirements"], [])
        self.assertEqual(payload["completion_report"], [])


if __name__ == "__main__":
    unittest.main()
