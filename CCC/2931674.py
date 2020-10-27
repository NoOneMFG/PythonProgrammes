x = {"CU": "see you", ":-)": "I'm happy", ":-(": "I'm unhappy", ";-)": "wink", ":-P": "stick out my tongue", "(~.~)": "sleepy", "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "beacause", "TY": "thank-you", "YW": "you're welcome", "TTLY": "talk to you later"}
n = "sgsd"
while n != "TA":
    n = input()
    if n == "TTLY":
        break
    elif n in x:
        print(x[str(n)])
    else:
        print(str(n))
