from module2labs import mysplit

def test_mysplit():
    assert mysplit("") == []
    assert mysplit("   ") == []
    #assert mysplit("cherry is red") == ["cherry", "is", "red"]
    assert mysplit("   abc   ") == ["abc"]