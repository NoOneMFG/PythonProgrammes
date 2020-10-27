str1 = input()
str2 = input()
if sorted(str1) == sorted (str2):
    print("Is an anagram.")
else:
    print("Is not an anagram.")