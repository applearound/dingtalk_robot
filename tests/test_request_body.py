import logging
import unittest
from typing import Self

from dtalk_robot.request import RequestBody, TextBody

log = logging.getLogger(__name__)


class TestRobot(unittest.TestCase):
    def setUp(self: Self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def test_text_message(self: Self) -> None:
        request_body = RequestBody.text_message(text=TextBody(content="content"))

        dict_to_test = request_body.to_dict()

        log.debug("request_dict: %s", dict_to_test)

        self.assertIn("msgtype", dict_to_test)
        self.assertIn("text", dict_to_test)

        self.assertIn("content", dict_to_test["text"])
        self.assertEqual("content", dict_to_test["text"]["content"])


if __name__ == "__main__":
    unittest.main()
