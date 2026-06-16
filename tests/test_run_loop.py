import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run_loop.py"
INIT = ROOT / "scripts" / "init_loop.py"


def run_cmd(*args, cwd=ROOT):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def loop_hashes(target):
    hashes = {}
    for path in sorted((target / ".loop").glob("*.md")):
        hashes[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


class RunLoopCliTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.target = Path(self.tempdir.name)
        result = run_cmd(sys.executable, str(INIT), "--name", "runner-loop", "--dir", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def tearDown(self):
        self.tempdir.cleanup()

    def test_valid_loop_prints_bootstrap_briefing(self):
        result = run_cmd(sys.executable, str(RUNNER), "--dir", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("Xunhuan loop runner: READY", result.stdout)
        self.assertIn("Status: ReadyForRound1", result.stdout)
        self.assertIn("Round: 0", result.stdout)
        self.assertIn("Work order:", result.stdout)
        self.assertIn("does not execute agents", result.stdout)

    def test_json_output_contains_runner_contract(self):
        result = run_cmd(sys.executable, str(RUNNER), "--dir", str(self.target), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertIs(payload["ok"], True)
        self.assertEqual(payload["status"], "ReadyForRound1")
        self.assertEqual(payload["round"], "0")
        self.assertIn("next_action", payload)
        self.assertTrue(payload["work_order_path"].endswith("WORK_ORDER.md"))
        self.assertIn("WORK_ORDER", payload["work_order_title"])
        self.assertEqual(payload["issues"], [])

    def test_invalid_loop_surfaces_checker_issues_and_exits_nonzero(self):
        (self.target / ".loop" / "STATE.md").unlink()
        result = run_cmd(sys.executable, str(RUNNER), "--dir", str(self.target))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("NOT READY", result.stdout)
        self.assertIn("STATE.md", result.stdout)

    def test_runner_is_read_only_for_loop_files(self):
        before = loop_hashes(self.target)
        result = run_cmd(sys.executable, str(RUNNER), "--dir", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        after = loop_hashes(self.target)
        self.assertEqual(before, after)

    def test_next_action_section_is_extracted(self):
        state = self.target / ".loop" / "STATE.md"
        state.write_text(
            "# STATE\n\nstatus: ReadyForRound2\nround: 1\n\n## Next action\n\nRun verifier and decide stop gate.\n\n## Other\n\nIgnore me.\n",
            encoding="utf-8",
        )
        result = run_cmd(sys.executable, str(RUNNER), "--dir", str(self.target), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "ReadyForRound2")
        self.assertEqual(payload["round"], "1")
        self.assertEqual(payload["next_action"], "Run verifier and decide stop gate.")

    def test_empty_next_action_ignores_metadata_comments(self):
        result = run_cmd(sys.executable, str(RUNNER), "--dir", str(self.target), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["next_action"], "(none specified)")


if __name__ == "__main__":
    unittest.main()
