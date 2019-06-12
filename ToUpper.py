x = input("Enter String: ")
i = 0
y = ""
while i < len(x):
    ch = x[i]
    if (ord(ch) > 96)and (ord(ch) < 123):
        m = int(ord(ch)-32)
        y += chr(m)
    else:
        y += x[i]
    i += 1
print("UpperCase: "+y)
