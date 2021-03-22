import pytest
import one_hot_encoder


def test_double_city():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_unique_city():
    cities = ['Moscow', 'New York']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [0, 1]),
        ('New York', [1, 0]),
    ]
    assert actual == expected


def test_one_city():
    cities = ['Moscow']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [1]),
    ]
    assert actual == expected


def test_empty_args():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()
