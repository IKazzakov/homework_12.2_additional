import pytest
from pytest_proj.utils import dicts

def test_get():
    assert dicts.get_val({'red':'tomato', 'green':'apple'}, 'red') == 'tomato'
    assert dicts.get_val({'red':'tomato', 'green':'apple'}, 'blue') == 'git'
    assert dicts.get_val({'red':'tomato', 'green':'apple'}, 'green', 'git') == 'apple'


def test_get_without_key():
    with pytest.raises(TypeError):
        dicts.get_val({'red':'tomato', 'green':'apple'})
