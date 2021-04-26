"""
Palindrome class realization.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack

class Palindrome:
    """
    Class for finding palindromes.
    """

    def __init__(self):
        """
        Initialize with empty stack
        """

        self._stack = ArrayStack()

    def _read_ukrainian(self, filename: str) -> list:
        """
        Return list of ukrainian words in the same order as in the filename.
        """

        # words_list = []
        with open(filename, mode='r', encoding="UTF-8") as words_file:
            for line in words_file:
                if line[0] != ' ':
                    ind = line.find(' ')
                    word = line[:ind]
                    # words_list.append(word)
                    self._stack.push(word)

        return list(self._stack)

    def _read_english(self, filename: str) -> list:
        """
        Return list of english words in the same order as in the filename.
        """

        # words_list = []
        with open(filename, mode='r', encoding="UTF-8") as words_file:
            for line in words_file:
                word = line.strip()
                # words_list.append(word)
                self._stack.push(word)

        return list(self._stack)

    def read_file(self, filename: str) -> list:
        """
        Return list of words in the same order as in the filename.
        """

        self._stack.clear()

        with open(filename, mode='r', encoding="UTF-8") as words_file:
            char = words_file.readline()[0]
            if ord(char.lower()) == 1072:
                return self._read_ukrainian(filename)
            if ord(char.lower()) == 97:
                return self._read_english(filename)

        return None


    def find_palindromes(self, read_filename: str, write_filename: str) -> list:
        """
        Return list of polindromes.
        """

        self.read_file(read_filename)
        words = self._stack
        polindromes = ArrayStack()
        for word in words:
            if word == word[-1::-1]:
                polindromes.push(word)

        self.write_to_file(write_filename, polindromes)
        return list(polindromes)

    @staticmethod
    def write_to_file(filename: str, polindromes: ArrayStack):
        """
        Writes polindromes to file.
        """

        text = ""

        for polindrome in polindromes:
            text += f'{polindrome}\n'

        with open(filename, mode='w', encoding="UTF-8") as write_file:
            write_file.write(text)


if __name__ == "__main__":
    # palindrome = Palindrome()
    # print(palindrome.read_file('base.lst')[:10])
    # print(palindrome.read_file('words.txt')[:10])
    # print( palindrome.find_palindromes("base.lst", "palindrome_uk.txt") )
    # print( palindrome.find_palindromes("words.txt", "palindrome_en.txt") )
    pass
