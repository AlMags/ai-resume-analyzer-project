import unittest
from prompt_builder import build_resume_prompt

class TestPromptBuilder(unittest.TestCase):
    def test_prompt_contains_resumse(self):
        resume = "Java Developer"
        prompt = build_resume_prompt(resume)
        self.assertIn(resume, prompt) # check if the returned prompt actually contains this text

if __name__ == "__main__":
    unittest.main