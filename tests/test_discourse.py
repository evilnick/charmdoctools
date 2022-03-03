import pytest

from charmdoctools.discourse import get_raw_url

@pytest.mark.parametrize("test_input,expected", [
    ("https://discourse.ubuntu.com/a_test_post/3615", 'https://discourse.ubuntu.com/raw/3615'),
    ("https://discourse.ubuntu.com/t/a_test_post/3615", 'https://discourse.ubuntu.com/raw/3615'),
    ("https://discourse.ubuntu.com/c/a_test_post/315", 'https://discourse.ubuntu.com/raw/315')])
def test_discourse_urls(test_input,expected):
    assert get_raw_url(test_input) == expected