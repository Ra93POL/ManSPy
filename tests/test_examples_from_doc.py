import unittest
import os.path
import re

from manspy import API, Settings

REGEXP_MARKDOWN_LINK = r'\[([^\]]+)\]\(https://syeysk.ru/api/manspy/run_get\?s=([\w/%\d]+)\)[^>]+((?:<span>`[\w\s\d]+`</span>[\s\w]*)+)'


def collect_examples(doc_path):
    with open(doc_path, 'r', encoding='utf-8') as fdoc:
        match = re.findall(REGEXP_MARKDOWN_LINK, fdoc.read())
        for sentence, encoded_sentence, answer in match:
            decoded_sentence = encoded_sentence.replace('%20', ' ')
            if decoded_sentence == sentence:
                yield sentence, re.findall(r'<span>`([\s\w\d]+)`</span>', answer)


class ExamplesFromDocTestCase(unittest.TestCase):
    def test_examples(self):

        r_texts = {}

        def read_text(r_text, arg0):
            sentence, expecting = arg0
            if sentence not in r_texts:
                r_texts[sentence] = {'real': [], 'expecting': expecting}
            r_texts[sentence]['real'].append(r_text)

        with API() as api:

            for sentence, expecting_answer in collect_examples(os.path.join(os.path.dirname(__file__),
                                                                            '../DOC/Theory.md')):
                language = 'esperanto'
                settings = Settings(read_text=read_text, language=language, answer_type='fake')
                api.write_text(sentence, settings, {'any_data': (sentence, expecting_answer), 'print_time': False})
            #self.assertEqual(True, False)

            for sentence in r_texts:
                real = r_texts[sentence]['real']
                expecting = r_texts[sentence]['expecting']
                self.assertListEqual(real, expecting, sentence)

