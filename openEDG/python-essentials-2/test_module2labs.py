from module2labs import mysplit
import pytest

@pytest.mark.lab1
def test_mysplit():
    assert mysplit("") == []
    assert mysplit("   ") == []
    assert mysplit("cherry is red") == ["cherry", "is", "red"]
    assert mysplit("   abc   ") == ["abc"]