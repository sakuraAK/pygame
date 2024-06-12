if __name__ == "__main__":
    print("In strings module")
def count_vowels():
    """
    :param a:
    :param b:
    :param c:
    :return:
    """
    word = "whEEls on the bus go round and round" # should print 6
    word = word.lower()
    counter = 0
    vowels = ['a', 'e', 'i', 'u', 'o']
    for c in word:
        # if c == 'a' or c == 'e' or\
        #         c == 'u' or c == 'o' or c == 'i':
        #     counter += 1
        if c in vowels:
            counter += 1

    print(f"Number of vowels in {word} is {counter}")


def count_unique_vowels():
    """
    :param a:
    :param b:
    :param c:
    :return:
    """
    word = "whEEls on the bus go round and round" # should print 6
    word = word.lower()
    counter = 0
    vowels = ['a', 'e', 'i', 'u', 'o']
    s = set()
    for c in word:
        # if c == 'a' or c == 'e' or\
        #         c == 'u' or c == 'o' or c == 'i':
        #     counter += 1
        if c in vowels:
            s.add(c)

    print(f"Number of unique vowels in {word} is {len(s)}")

def is_letters_only():
    """
    Print Yes if the word contains only English letters and No otherwise
    :return:
    """
    word = "Car!"

    # if word.isalpha():
    #     print("Yes")
    # else:
    #     print("No")
    for c in word:
        if not (ord(c) >= ord('a') and ord(c) <= ord('z') \
                or ord(c) >= ord('A') and ord(c) <= ord('Z')):
            print("No")
            return

    print("Yes")


def to_capital():
    """
    Print in all caps
    Hint: use ASCII
    :return:
    """
    line = "I love Python!"
    new_line = []
    # should be I LOVE PYTHON


'''
Five little monkeys jumping on the bed
One fell off and bumped his head
Mama called the doctor and the doctor said
"No more monkeys jumping on the bed!"
Fo+ur little monkeys jumping on the bed
One fell off and bumped his head
Mama called the doctor and the doctor said
"No more monkeys jumping on the bed!"
Three little monkeys jumping on the bed
One fell off and bumped his head
Mama called the doctor and the doctor said
"No more monkeys jumping on the bed!"
Two little monkeys jumping on the bed
One fell off and bumped his head
Mama called the doctor and the doctor said
"No more monkeys jumping on the bed!"
One little monkey jumping on the bed
He fell off and bumped his head
Mama called the doctor and the doctor said
"Put those monkeys right to bed!"
'''


def little_monkeys_gen(monkeys: int):
   pass



def simple_parser(exp: str) -> True:
    """
    Receive an expression and return True if it is a valid expression and False
    otherwise.
    Expression is valid if '(' followed by ')'.
    Example: (a + b), ((a-b) + z) - valid
        ((((a + b) - z) - invalid
    :param exp: expressio
    :return: return True if it is a valid expression and False
    otherwise
    """
    pass

def advanced_parser(exp):
    """
    Advanced parser
    Suggest an improvement for the Simple Parser to be able to decide validity for
    expressions that contain more than one type of brackets (),[], {} ,<>
    :param exp:
    :return:
    """
    pass
