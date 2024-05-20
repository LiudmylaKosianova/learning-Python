import pytest
from module2labs import mysplit
from module2labs import ledInputCheck
from module2labs import caesarLineInput
from module2labs import caesarCypherInput

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
    monkeypatch.setattr('builtins.input', lambda _:"abc")
    assert ledInputCheck() == -1
    monkeypatch.setattr('builtins.input', lambda _:"975")
    assert ledInputCheck() == "975"

@pytest.mark.caesarc
def test_caesarLineInput(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"hello5 77")
    assert caesarLineInput() == -1
    monkeypatch.setattr('builtins.input', lambda _:"     ")
    assert caesarLineInput() == -1
    monkeypatch.setattr('builtins.input', lambda _:"Hello there")
    assert caesarLineInput() == "Hello there"
     
@pytest.mark.caesarc
def test_ceaserCypherInput_wrongline():
    assert caesarCypherInput(-1) == -1

@pytest.mark.caesarc
def test_caesarCypherInput(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"1")
    assert caesarCypherInput("Hi") == 1
    monkeypatch.setattr('builtins.input', lambda _:"25")
    assert caesarCypherInput("Hi") == 25


