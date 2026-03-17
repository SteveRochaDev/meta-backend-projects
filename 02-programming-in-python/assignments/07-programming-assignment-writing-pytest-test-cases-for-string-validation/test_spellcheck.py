# test_spellcheck.py

# Import statements
import pytest
import spellcheck

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
# beta = "This sentence should fail the test"

# PyTest fixture
@pytest.fixture
def input_value():
    # Default input value for testing
    return alpha

# First test function: test_length
def test_length(input_value):
    """ 
    Tests whether a string has fewer than 10 words and fewer than 50 characters.
    """
    assert spellcheck.word_count(input_value) < 10, "Word count exceeds 10"
    assert spellcheck.char_count(input_value) < 50, "Character count exceeds 50"

# Second test function: test_struc
def test_struc(input_value):
    """ 
    Tests whether a string begins with a capital letter and ends with a period.
    """
    assert spellcheck.first_char(input_value).isupper(), "First character is not uppercase"
    assert spellcheck.last_char(input_value) == ".", "Last character is not a period"