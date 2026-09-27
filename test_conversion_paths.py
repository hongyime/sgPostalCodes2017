"""Offline CLI path contracts; pandas is replaced at the library boundary."""
from pathlib import Path
import runpy
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

SCRIPT = Path(__file__).resolve().parent / "code" / "jsontocsv.py"


class ConversionPaths(unittest.TestCase):
    def test_explicit_paths_with_spaces_are_forwarded_without_a_personal_default(self):
        with tempfile.TemporaryDirectory(prefix="postal paths ") as temp:
            source = Path(temp) / "chosen input.json"
            target = Path(temp) / "chosen output.csv"
            frame = Mock()
            pandas = SimpleNamespace(read_json=Mock(return_value=frame))
            with patch.dict(sys.modules, {"pandas": pandas}):
                main = runpy.run_path(str(SCRIPT))["main"]
                main([str(source), str(target)])
            pandas.read_json.assert_called_once_with(source)
            frame.to_csv.assert_called_once_with(target, index=False)

    def test_import_does_not_read_or_convert_a_file(self):
        pandas = SimpleNamespace(read_json=Mock(side_effect=AssertionError("unexpected read")))
        with patch.dict(sys.modules, {"pandas": pandas}):
            runpy.run_path(str(SCRIPT))
        pandas.read_json.assert_not_called()


if __name__ == "__main__":
    unittest.main()
