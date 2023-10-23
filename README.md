# myanmar_words

[![PyPI](https://img.shields.io/pypi/v/myanmar_words)](https://pypi.org/project/myanmar_words/)
[![License](https://img.shields.io/github/license/linhtutkyawdev/myanmar_words)](https://github.com/linhtutkyawdev/myanmar_words/blob/main/LICENSE)
[![Build Status](https://travis-ci.org/linhtutkyawdev/myanmar_words.svg?branch=main)](https://travis-ci.org/linhtutkyawdev/myanmar_words)
[![Python Versions](https://img.shields.io/pypi/pyversions/myanmar_words)](https://pypi.org/project/myanmar_words/)

A Python library for working with Myanmar words and sentences.

## Features

- Perform various text processing tasks on Myanmar text.
- Tokenize Myanmar sentences into words.
- Myanmar word count.
- Find Myanmar words in a sentence.
- Retrieve Myanmar words. (nouns, pronouns, verbs, adjectives, adverbs, conjunctions, postpositions, particles, all)

## Installation

You can install `myanmar_words` using pip:

```bash
pip install myanmar_words
```

## Usage

```python
# example.py
from myanmar_words import brake

text="Hello, Myanmar! မင်္ဂလာပါ မြန်မာ!"
print(brake(text))
print(count(text))
print(find(text))
print(get("all"))
```

For detailed documentation and examples, visit my github link [https://github.com/linhtutkyawdev/myanmar_words].

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

We welcome contributions from the community. Please see our Contribution Guidelines for more information.

## Authors

Lin Htut Kyaw
[https://linhtutkyawdev.vercel.app]

## Support

If you have any questions, issues, or feature requests, please open an issue or contact us at [linhtutkyaw.dev@gmail.com].

## Credit

Credit to myanmartools for word collection
[https://github.com/myanmartools/myanmar-words]

## Roadmap

See the open issues for a list of proposed features (and known issues).
