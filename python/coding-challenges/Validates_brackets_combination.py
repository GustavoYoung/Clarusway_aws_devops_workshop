# This code validates brackets combination.

symbol = input("Please enter brackets combination: ")

def check(text):
    pairs = {')': '(', ']': '[', '}': '{'}
    que = []
    for i in text:
        if i in pairs.values():
            que.append(i)
        elif i in pairs.keys():
            if que[-1] == pairs[i]:
                que.pop(-1)
            else:
                return False
        else:
            return False
    return False if que else True

if check(symbol):
    print(symbol, "=", "true")
else:
    print(symbol, "=", "false")
