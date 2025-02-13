from project import get_json
from project import get_antonyms
from project import get_synonyms
from project import get_definition
import pytest


def test_get_synonyms():
    assert "specimen" in get_synonyms(get_json("example"))
    assert "sufficient" in get_synonyms(get_json("enough"))


def test_errors():
    with pytest.raises(ValueError):
        assert get_synonyms(get_json("Hello"))
    with pytest.raises(ValueError):
        assert get_antonyms(get_json("hello"))
    with pytest.raises(ValueError):
        assert get_antonyms(get_json("example"))
    with pytest.raises(ValueError):
        assert get_definition("aeroir")


def test_get_antonyms():
    assert "insufficient" in get_antonyms(get_json("enough"))
    assert "dead" in get_antonyms(get_json("alive"))
