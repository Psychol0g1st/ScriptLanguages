from Verem import Verem

def test_init():
    v: Verem = Verem()
    assert v.meret() == 0

def test_str():
    v: Verem = Verem()
    assert str(v) == "["
    v.betesz(1)
    v.betesz(10)
    v.betesz('Text')
    assert str(v) == "[1, 10, 'Text'"

def test_ures():
    v: Verem = Verem()
    assert v.ures() == True
    v.betesz(1)
    assert v.ures() == False

def test_betesz():
    v: Verem = Verem()
    v.betesz(1)
    assert v.get_current() == 1
    v.betesz('Text')
    assert v.get_current() == 'Text'

def test_kivesz():
    v: Verem = Verem()
    assert v.kivesz() == None
    assert v.meret() == 0
    v.betesz(1)
    v.betesz('Text')
    assert v.kivesz() == 'Text'
    assert v.get_current() == 1
    assert v.kivesz() == 1

def test_meret():
    v: Verem = Verem()
    assert v.meret() == 0
    v.betesz(1)
    assert v.meret() == 1
    v.betesz('Text')
    assert v.meret() == 2
    v.kivesz()
    assert v.meret() == 1
    v.kivesz() 
    assert v.meret() == 0
