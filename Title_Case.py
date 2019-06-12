x = input("Enter a string: ")
i = 0
m = 0
y = ""
while i < len(x):
    ch = x[i]
    if i == 0 and ch != " ":
        if (ord(ch) > 96) and (ord(ch) < 123):
            m = int(ord(ch)-32)
            y += chr(m)
        else:
            m = int(ord(ch))
            y += chr(m)
    elif ch == " ":
        y += " "
        if i+1 < len(x):
            ch1 = x[i+1]
            if (ord(ch1) > 96) and (ord(ch1) < 123):
                m = int(ord(ch1)-32)
                y += chr(m)
            else:
                m = int(ord(ch1))
                y += chr(m)
            i += 1
    elif (ord(ch) > 64) and (ord(ch) < 91):
        m = int(ord(ch)+32)
        y += chr(m)
    else:
        m = int(ord(x[i]))
        y += chr(m)
    i += 1
print("NEW STRING IS: "+y)
