kata = "The right format is my skills"

# the rjust bytes array builtin method right adjust the byte array regarding len (42 here) and a filling byte ('-' here)
sentence = kata.rjust(42, '-')
print(sentence)