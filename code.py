print("Hello world")

print("one more line")


for i in range(0, 5):
    for j in range(0, 3):
        print("* ", end="")
    print()

# pyramid
for i in range(0, 5):
    for j in range(0, i):
        print("* ", end="")
    print()


# right traingle
for i in range(0, 5):
    for j in range(i, 0, -1):
        print("* ", end="")
    print()

# other traingle
for i in range(0, 5):
    for k in range(0, i):
        print("  ", end="")
    print("* ", end="")

    print()

print("first line")
print("second line")
print("third line")
print("four line")
print("five line - fix menu bar")
print("six line")
print("eight line")
print("seven line")

