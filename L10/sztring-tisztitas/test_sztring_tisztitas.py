from sztring_tisztitas import clean_wia_replace, clean_wia_split

def test_clean_wia_replace():
    assert clean_wia_replace("192.168.0.1: \n6666") == "192.168.0.1:6666"
    assert clean_wia_replace("\n192.168   .0   \n.1:6666\n") == "192.168.0.1:6666"
    assert clean_wia_replace("    \n192.168\t.0.1: \n66\t66 \t\t\t  ") == "192.168.0.1:6666"

def test_clean_wia_split():
    assert clean_wia_split("192.168.0.1: \n6666") == "192.168.0.1:6666"
    assert clean_wia_split("\n192.168   .0   \n.1:6666\n") == "192.168.0.1:6666"
    assert clean_wia_split("    \n192.168\t.0.1: \n66\t66 \t\t\t") == "192.168.0.1:6666"