import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тести для класу AnonymousSurvey."""

    def test_store_single_response(self):
        """Перевірити, чи окрема відповідь зберігається правильно."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Перевірити, чи три індивідуальних відповіді зберігаються правильно."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
