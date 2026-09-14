import json
import unittest
from unittest.mock import patch

from app import build_info


class BuildInfoTests(unittest.TestCase):
    def test_build_info_has_expected_status(self) -> None:
        self.assertEqual(build_info()["status"], "ok")

    def test_build_info_has_application_name(self) -> None:
        self.assertEqual(build_info()["application"], "pratica-09-automacao-build")

    def test_version_can_be_defined_by_environment(self) -> None:
        with patch.dict("os.environ", {"APP_VERSION": "ci"}):
            self.assertEqual(build_info()["version"], "ci")

    def test_payload_is_json_serializable(self) -> None:
        self.assertIsInstance(json.dumps(build_info()), str)


if __name__ == "__main__":
    unittest.main(verbosity=2)

