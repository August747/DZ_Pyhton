import pytest

import library


def test_get_ukrainian_coins():
    assert type(library.get_ukrainian_coins(5)) == str


check_list = [
    (5, 'копійок'),
    (0, 'копійок'),
    (2, 'копійки'),
    (99, 'копійок'),
    (-99, 'копійок'),
]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_get_ukrainian_coins(test_input, expected):
    assert library.get_ukrainian_coins(test_input) == expected



def test_get_ukrainian_hryvnas():
    assert type(library.get_ukrainian_hryvnas(5)) == str


check_list = [
    (6, 'гривень'),
    (22, 'гривні'),
    (32, 'гривні'),
    (199, 'гривень'),
    (-10, 'гривень'),
]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_get_ukrainian_hryvnas(test_input, expected):
    assert library.get_ukrainian_hryvnas(test_input) == expected




