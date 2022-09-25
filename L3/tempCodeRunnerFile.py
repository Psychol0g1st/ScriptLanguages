for letter in solution:
        lowerLetter = letter.lower()
        if lowerLetter in alphabet:
            letterIndex = alphabet.index(lowerLetter)
            newLetterIndex = letterIndex if letterIndex <= len(alphabet)-2 else len(alphabet) - letterIndex - 1
            newLetter = alphabet[newLetterIndex] if letter.islower() else alphabet[newLetterIndex].upper()
            solution = solution.replace(letter, newLetter)
    print(solution)