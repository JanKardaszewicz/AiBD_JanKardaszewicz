import pytest
from app import hello, extract_sentiment, text_contain_word, bubble_sort

def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want

testdata = ["I think today will be a great day","I do not think this will turn out well"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

testdata2 = [
    ([64, 34, 25, 12, 22, 11, 90], [11,12,22,25,34,64,90 ]),
    ([39, 12, 18, 85, 72, 10, 2, 18], [2, 10, 12, 18, 18, 39, 72, 85])
    ]
@pytest.mark.parametrize('sample, expected_output', testdata2)
def test_bubble_sort(sample, expected_output):

    assert bubble_sort(sorted) == expected_output