import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INIT_RESEARCH = ROOT / "scripts" / "init_research_pack.py"

PACK_DIRS = {
    "raw",
    "raw/source_captures",
    "clean",
    "reading",
    "insights",
    "kb",
    "workflow",
}

STARTER_FILES = {
    "README.md",
    "clean/sources.json",
    "clean/source_quality.md",
    "insights/synthesis.md",
    "kb/stable_conclusions.md",
    "workflow/patches.md",
    "workflow/next_execution_plan.md",
}


def run_cmd(*args, cwd=ROOT):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


class InitResearchPackCliTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.target = Path(self.tempdir.name)
        self.pack = self.target / "ai-workflow-research"

    def tearDown(self):
        self.tempdir.cleanup()

    def init_pack(self, *extra_args, question="How should research become workflow knowledge?"):
        return run_cmd(
            sys.executable,
            str(INIT_RESEARCH),
            "--name",
            "ai-workflow-research",
            "--dir",
            str(self.target),
            "--question",
            question,
            *extra_args,
        )

    def test_creates_layered_research_pack(self):
        result = self.init_pack()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("wrote:", result.stdout)

        for relative in PACK_DIRS:
            self.assertTrue((self.pack / relative).is_dir(), relative)
        for relative in STARTER_FILES:
            self.assertTrue((self.pack / relative).is_file(), relative)

        readme = (self.pack / "README.md").read_text(encoding="utf-8")
        self.assertIn("How should research become workflow knowledge?", readme)
        self.assertIn("raw/", readme)
        self.assertIn("clean/", readme)
        self.assertIn("promotion gate", readme.lower())
        self.assertIn("Hermes", readme)
        self.assertIn("Codex", readme)
        self.assertIn("Verifier", readme)

    def test_sources_json_starts_parseable_and_empty(self):
        result = self.init_pack()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertEqual(
            (self.pack / "clean" / "sources.json").read_text(encoding="utf-8").strip(),
            "[]",
        )

    def test_dry_run_lists_planned_paths_without_writing(self):
        result = self.init_pack("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("would create:", result.stdout)
        self.assertIn(str((self.pack / "README.md").resolve()), result.stdout)
        self.assertFalse(self.pack.exists())

    def test_refuses_to_overwrite_existing_files_without_force(self):
        self.pack.mkdir(parents=True)
        readme = self.pack / "README.md"
        readme.write_text("existing readme\n", encoding="utf-8")

        result = self.init_pack()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Refusing to overwrite", result.stderr + result.stdout)
        self.assertEqual(readme.read_text(encoding="utf-8"), "existing readme\n")

    def test_force_overwrites_generated_files(self):
        self.pack.mkdir(parents=True)
        readme = self.pack / "README.md"
        readme.write_text("existing readme\n", encoding="utf-8")

        result = self.init_pack("--force", question="x")

        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        content = readme.read_text(encoding="utf-8")
        self.assertNotEqual(content, "existing readme\n")
        self.assertIn("x", content)


if __name__ == "__main__":
    unittest.main()
