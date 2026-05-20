if name[0].isdigit():
    result = False
elif name in keyword.kwlist:
    result = False
elif "__" in name:
    result = False
else:
    for ch in name:
        if ch.isupper():
            result = False
        elif ch == " ":
            result = False
        elif ch in string.punctuation.replace("_", ""):
            result = False
print(result)

