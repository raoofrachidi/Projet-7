from grandpybot.parser import Parser
from grandpybot.stop_words import STOP_WORDS
from grandpybot.google_maps import *
from grandpybot.wikipedia import *

parser = Parser(STOP_WORDS)


class TestSearch:

    def test_parsing_question(self):
        question = "Salut GrandPy, Est-ce que tu peux me parler de Paris?"
        parsed_question = parser.get_relevant_words(question)
        assert parser.get_relevant_words(question) == "paris"

    def test_position_result(self, monkeypatch):
        result = {
            "latitude": 48.856614,
            "longitude": 2.3522219,
            "address": "Paris, France"
        }

        def mockreturn(self, question):
            return result
            monkeypatch.setattr(GMaps, 'get_position', mockreturn)
            gmap = GMaps('google_api_key')
            gmap_result = gmap.get_position(parsed_question)
            assert gmap_result['address'] == "Paris, France"
            assert gmap_result['latitude'] == 48.856614
            assert gmap_result['longitude'] == 2.3522219

    def test_wiki_result(self, monkeypatch):
        result = {
            "title": "Paris",
            "summary": "Capitale de la France"
        }

        def mockreturn(self, question):
            return result
            monkeypatch.setattr(Wiki, 'get_wiki_result', mockreturn)
            wiki = Wiki()
            wiki_result = wiki.get_wiki_result(parsed_question)
            assert wiki_result['title'] == 'Paris'
            assert wiki_result['summary'] == 'Capitale de la France'
