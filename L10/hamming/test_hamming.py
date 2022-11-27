from hamming import hamming

def test_hamming():
    assert hamming("toned", "roses") == 3
    assert hamming("toned", "toned") == 0
    assert hamming("toned", "toner") == 1
    assert hamming("toned", "tonedroses") == -1
    assert hamming("helloUser", "tonedroses") == -1
    assert hamming("", "") == 0
    assert hamming("a", "a") == 0
    assert hamming("a", "b") == 1