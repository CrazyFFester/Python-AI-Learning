from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_numbers():
    assert shorten("cs50") == "cs50"

def test_punctuation():
    assert shorten("hello, world") == "hll, wrld"
