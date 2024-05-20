import pytest
from module2labs import mysplit
from module2labs import ledInputCheck
from module2labs import caesarLineInput
from module2labs import caesarCypherInput
from module2labs import caesarCypher
from module2labs import paliInput
from module2labs import paliOrNot
from module2labs import paliOrNot2
from module2labs import anagrams

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

@pytest.mark.caesarc
def test_caesarCypher():
    assert caesarCypher("The die is cast", 25) == "Sgd chd hr bzrs"  
    assert caesarCypher("abcxyzABCxyz 123", 2) == "cdezabCDEzab 123"

@pytest.mark.pali
def test_paliInput(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"  ")
    assert paliInput() == -1
    monkeypatch.setattr('builtins.input', lambda _:"")
    assert paliInput() == -1
    monkeypatch.setattr('builtins.input', lambda _:"aaa AAA")
    assert paliInput() == "aaaaaa"
    monkeypatch.setattr('builtins.input', lambda _:"7P P7")
    assert paliInput() == "7pp7"

@pytest.mark.pali
def test_paliOrNot():
    assert paliOrNot("tenanimalsislaminanet") == True
    assert paliOrNot("aabbbc") == False

@pytest.mark.pali
def test_paliOrNot2():
    assert paliOrNot2("tenanimalsislaminanet") == True
    assert paliOrNot2("aabbbc") == False

@pytest.mark.an  
def test_anagrams():
    assert anagrams("I am", "You are") == False
    assert anagrams("rail safety", "fairy tales") == True
    assert anagrams("Rail saFety", "fAiry Tales") == True
    assert anagrams("   ", " banana") == False
    assert anagrams(" ", " ") == False


