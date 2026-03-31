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