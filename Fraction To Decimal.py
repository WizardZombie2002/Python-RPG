#Fractions to decimals
#By Frogs123
frac = input("Input fraction: ")
num = ""
den = ""
OnNum = True
     
for char in frac:
    if char == "/":
        OnNum = False
    elif OnNum:
        num += char
    else:
        den += char
     
print(int(num)/int(den))
