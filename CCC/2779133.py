x = {"CU": "see you", ":-)": "I'm happy", ":-(": "I'm unhappy", ";-)": "wink", ":-P": "stick out my tongue", "(~.~)": "sleepy", "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "beacause", "TY": "thank-you", "YW": "you're welcome", "TTLY": "talk to you later"}
text = []
n = "Somethings"
while n != "TTLY":
    n = input()
    if n in x:
        text.append(x[str(n)])
        if n == "TTLY":
            break
    else:
        text.append(str(n))
for i in text:
    print(i)