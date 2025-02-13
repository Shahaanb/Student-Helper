from convert import dec_to_binary
from convert import dec_to_hexa
from convert import hexa_to_dec
from convert import binary_to_dec
import pytest


def test_dec_to_binary():
    assert dec_to_binary(0) == "0000"
    assert dec_to_binary(5) == "0101"
    assert dec_to_binary(10) == "1010"
    assert dec_to_binary(255) == "11111111"
    assert dec_to_binary(174) == "10101110"
    assert dec_to_binary(10000) == "10011100010000"
    with pytest.raises(ValueError):
        assert dec_to_binary(-1)


def test_dec_to_hexa():
    assert dec_to_hexa(10) == "A"
    assert dec_to_hexa(16) == "10"
    assert dec_to_hexa(500) == "1F4"
    assert dec_to_hexa(1000000) == "F4240"
    assert dec_to_hexa(0) == "0"
    assert dec_to_hexa(1) == "1"
    assert dec_to_hexa(9) == "9"
    with pytest.raises(ValueError):
        assert dec_to_hexa(-1)


def test_binary_to_dec():
    assert binary_to_dec("0") == 0
    assert binary_to_dec("1010") == 10
    assert binary_to_dec("111001") == 57
    assert binary_to_dec("10000000") == 128
    with pytest.raises(ValueError):
        assert binary_to_dec("-1")
    with pytest.raises(ValueError):
        assert binary_to_dec("0201") == 0


def test_hexa_to_dec():
    assert hexa_to_dec("A") == 10
    assert hexa_to_dec("0") == 0
    assert hexa_to_dec("10") == 16
    assert hexa_to_dec("A") == 10
    assert hexa_to_dec("2710") == 10000
    assert hexa_to_dec("186A0") == 100000
    with pytest.raises(ValueError):
        assert hexa_to_dec("-1")
    with pytest.raises(ValueError):
        assert hexa_to_dec("-A")
