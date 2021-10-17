class CharacterArray:

    # Define the string
    chArray = []

    # Define the number of characters
    n_ch = 0

    def __init__(self, string) -> None:
        self.chArray = list(string)
        self.n_ch = len(string)
    def __str__(self) -> str:
        rt_str = ""
        for i in self.chArray:
            rt_str += i
        return rt_str

    def check_palindrome(self):
        # Char Iterative Method
        mid = (int)( (self.n_ch)/2 )
        for i in range(mid):
            if self.chArray[i] != self.chArray[self.n_ch - i - 1]:
                return False
        return True

    # Remove element from character list
    def remove_char(self, spec):
        if isinstance(spec, str):
            for i in self.chArray:
                if i == spec:
                    self.chArray.remove(spec)
        elif isinstance(spec, int):
            self.chArray.pop(spec)

    # Get all permutations of the character arrangement
    def get_permutations(self):


def main():
    
    # Check_Palindrome Tests
    test_1 = CharacterArray("omo")
    print(test_1.check_palindrome())
    test_2 = CharacterArray("OmoOMo")
    print(test_2.check_palindrome())
    test_3 = CharacterArray("omuomo")
    print(test_3.check_palindrome())

    # Remove_Char Tests
    test_1.remove_char("o")
    print(test_1)
    test_2.remove_char("m")
    print(test_2)
    test_3.remove_char("u")
    print(test_3)


if __name__ == "__main__":
    main()
    