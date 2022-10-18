import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тести для класу AnonymousSurvey."""

    def setUp(self) -> None:
        """Створити опитування та набір відповідей для всіх тестувальних методів."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Перевірити, чи окрема відповідь зберігається правильно."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Перевірити, чи три індивідуальних відповіді зберігаються правильно."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
