#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['sumy']):
    from sumy.parsers.html import HtmlParser
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lsa import LsaSummarizer as Summarizer
    from sumy.nlp.stemmers import Stemmer
    from sumy.utils import get_stop_words

stop_words = get_stop_words('english')
stemmer = Stemmer('english')

summarizer = Summarizer(stemmer)
summarizer.stop_words = stop_words

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    
    contents = fdp.ConsumeRemainingString()
    if fdp.ConsumeBool():
        # Fuzz HTML
        parser = HtmlParser.from_string(contents, Tokenizer('english'))
    else:
        # Fuzz Plaintext
        parser = PlaintextParser.from_string(contents, Tokenizer('english'))

    for _ in summarizer(parser.document, 10):
        pass
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
