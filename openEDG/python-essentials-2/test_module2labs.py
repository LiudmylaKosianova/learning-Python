import pytest
from module2labs import mysplit
from module2labs import ledInputCheck

@pytest.mark.lab1
def test_mysplit():
    assert mysplit("") == []
    assert mysplit("   ") == []
    assert mysplit("cherry is red") == ["cherry", "is", "red"]
    assert mysplit("   abc   ") == ["abc"]

@pytest.mark.lab2
def test_ledInputCheck(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"-7")
    assert ledInputCheck() == -1
    


