from grandpybot.parser import Parser
from grandpybot.stop_words import STOP_WORDS

parser = Parser(STOP_WORDS)


class TestParser:

    def test_parse_words(self):
        question = "Salut GrandPy, Est-ce que tu peux me parler de Paris?"
        assert parser.get_relevant_words(question) == "paris"
