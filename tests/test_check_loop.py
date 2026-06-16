import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "scripts" / "check_loop.py"
INIT = ROOT / "scripts" / "init_loop.py"


def run_cmd(*args, cwd=ROOT):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


class CheckLoopCliTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.target = Path(self.tempdir.name)
        result = run_cmd(sys.executable, str(INIT), "--name", "test-loop", "--dir", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def tearDown(self):
        self.tempdir.cleanup()

    def test_valid_initialized_loop_passes(self):
        result = run_cmd(sys.executable, str(CHECK), "--dir", str(self.target))
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("PASS", result.stdout)

    def test_missing_required_file_fails(self):
        (self.target / ".loop" / "STATE.md").unlink()
        result = run_cmd(sys.executable, str(CHECK), "--dir", str(self.target))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("STATE.md", result.stdout)

    def test_missing_state_marker_fails(self):
        (self.target / ".loop" / "STATE.md").write_text("# STATE\nstatus: Ready\n", encoding="utf-8")
        result = run_cmd(sys.executable, str(CHECK), "--dir", str(self.target))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("round:", result.stdout)

    def test_missing_stop_gate_fails(self):
        (self.target / ".loop" / "STOP_GATE.md").write_text("# STOP_GATE\n## Done\n", encoding="utf-8")
        result = run_cmd(sys.executable, str(CHECK), "--dir", str(self.target))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("HumanGate", result.stdout)

    def test_missing_work_order_marker_fails(self):
        (self.target / ".loop" / "WORK_ORDER.md").write_text("# WORK_ORDER\n## Objective\n## Allowed files\n", encoding="utf-8")
        result = run_cmd(sys.executable, str(CHECK), "--dir", str(self.target))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Required verification", result.stdout)

    def test_json_output_is_parseable(self):
        result = run_cmd(sys.executable, str(CHECK), "--dir", str(self.target), "--json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        payload = json.loads(result.stdout)
        self.assertIs(payload["ok"], True)
        self.assertEqual(payload["issues"], [])


if __name__ == "__main__":
    unittest.main()
