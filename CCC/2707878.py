str1 = input()
str2 = input()

if sorted(str1.replace(" ", "")) == sorted (str2.replace(" ", "")):
    print("Is an anagram.")
else:
    print("Is not an anagram.")