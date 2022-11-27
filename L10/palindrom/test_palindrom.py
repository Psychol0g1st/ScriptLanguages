from palindrom import is_palindrom, is_palindrom_recursive, is_palindrom_iterative

def test_is_palindrom():
    assert is_palindrom("") == True
    assert is_palindrom("Anna") == True
    assert is_palindrom("traktor") == False
    assert is_palindrom("indul a gorog aludni") == True
    assert is_palindrom("indulagorogaludni") == True
    assert is_palindrom("  indulagorogaludni  ") == True
def test_is_palindrom_recursive():
    assert is_palindrom_recursive("") == True
    assert is_palindrom_recursive("Anna") == True
    assert is_palindrom_recursive("traktor") == False
    assert is_palindrom_recursive("indul a gorog aludni") == True
    assert is_palindrom_recursive("indulagorogaludni") == True
    assert is_palindrom_recursive("  indulagorogaludni  ") == True

def test_is_palindrom_iterative():
    assert is_palindrom_iterative("") == True
    assert is_palindrom_iterative("Anna") == True
    assert is_palindrom_iterative("traktor") == False
    assert is_palindrom_iterative("indul a gorog aludni") == True
    assert is_palindrom_iterative("indulagorogaludni") == True
    assert is_palindrom_iterative("  indulagorogaludni  ") == True
