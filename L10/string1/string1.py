from typing import Any

def donuts(count: int) -> str:
    return f'Fánkok száma: {count if count < 10 else "sok"}'

def both_ends(s: str) -> str:
    return '' if len(s) < 2 else s[:2] + s[-2:]

def fix_start(s: str) -> str:
    return s[0] + s[1:].replace(s[0], '*')

def mix_up(a: str, b: str) -> str:
    return f'{b[:2] + a[2:]} {a[:2] + b[2:]}'

def test(got: Any, expected: Any) -> None:
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))

def main() -> None:
    print('donuts')
  
    test(donuts(4), 'Fánkok száma: 4')
    test(donuts(9), 'Fánkok száma: 9')
    test(donuts(10), 'Fánkok száma: sok')
    test(donuts(99), 'Fánkok száma: sok')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
#############################################################################

if __name__ == '__main__':
    main()