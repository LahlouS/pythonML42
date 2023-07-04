import sys

def text_analyser(str = None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    try:
        int(str)
        print('AssertionError: argument is not a string')
    except:
        if str and not str.isdigit():
            count = 0
            upper_count = 0
            lower_count = 0
            punctuation_count = 0
            space_count = 0

            for character in str:
                count += 1
                if character.islower():
                    lower_count += 1
                elif character.isupper():
                    upper_count += 1
                elif character.isspace():
                    space_count += 1
                elif character.isprintable() and not character.isdigit():
                    punctuation_count += 1

            print(f"""
                The text contains {count} character(s):
                    - {upper_count} upper letter(s)
                    - {lower_count} lower letter(s)
                    - {punctuation_count} punctuation mark(s)
                    - {space_count} space(s)
            """)
        elif not str:
            str = input('What is the text to analyze?\n')
            text_analyser(str)
            pass
        else:
            print('AssertionError: argument is not a string')

#  init script in case module is the main
if __name__ == "__main__" and len(sys.argv) == 2:
    text_analyser(sys.argv[1])
elif __name__ == "__main__":
    print('AssertionError: more than one argument')
