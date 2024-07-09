#FOR LOOP


for i in range(5):
    print(i)

# WHILE LOOPS
print("\nWhile  loops: ")
i = 0
while i<7:
    print(i)
    i+=2

#BREAK
print('\nBreak')
for i in range(5):
    if i == 2:
        break  # Exit the loop when i is 2
    print(i)  # Output: 0 1


print('\nContinue')
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop when i is 2
    print(i)  # Output: 0 1 3 4
