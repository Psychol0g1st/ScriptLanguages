from typing import Any


def match_ends(words: list[str]) -> int:
    counter: int  = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            counter += 1
    return counter

def front_x(words: list[str]) -> list[str]:
    words.sort()
    x_words: list[str] = []
    for word in words:
        if word[0] == "x":
            x_words.append(word)
    for word in x_words:
        words.remove(word)
    return x_words + words

def test(got: Any, expected: Any) -> None:
    if got == expected:
        prefix: str = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))

def main() -> None:
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

#############################################################################

if __name__ == '__main__':
    main()