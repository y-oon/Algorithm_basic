a = None

# >>> False
if a:
    print("True")
else:
    print("False")

a = 1

# >>> True
if a:
    print("True")
else:
    print("False")

a = ""

# >>> False
if a:
    print("True")
else:
    print("False")

a = 0

# >>> False
if a:
    print("True")
else:
    print("False")

a = bool(0)

# >>> False
if a:
    print("True")
else:
    print("False")
