from hangrend import HANGREND_TIPUSOK, hangrend

def test_hangrend():
    assert hangrend("ablak") == "mely"
    assert hangrend("erkély") == "magas"
    assert hangrend("kisvasút") == "vegyes"
    assert hangrend("magas") == "mely"
    assert hangrend("mély") == "magas"
    assert hangrend("pfff") == "semmilyen"
    assert hangrend("") == "semmilyen"