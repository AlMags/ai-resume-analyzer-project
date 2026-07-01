import unittest
from json_parser import parse_response

class TestJsonParser(unittest.TestCase):
    def test_valid_json(self):

        sample = """
        {
            "summary": "Java Developer",
            "skills": ["Java"]
        }
        """

        result = parse_response(sample)

        self.assertEqual(result["summary"], "Java Developer")

    def test_invalid_json(self):
        sample = "Hello World"

        result = parse_response(sample)

        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main