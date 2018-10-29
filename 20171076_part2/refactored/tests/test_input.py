from util import keypress
import pytest

def test_keypress():
    assert keypress('Q') == -1;
    assert keypress('q') == -1;
    assert keypress('W') == 3;
    assert keypress('w') == 3;
    assert keypress('A') == 2;
    assert keypress('a') == 2;
    assert keypress('D') == 1;
    assert keypress('d') == 1;
