#READ INPUT FROM USER

name = input("Enter your name \n")
print(f"Your name is {name}")

# READ FROM FILE
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # print the content available in file example.txt

# WRITING TO A FILE    
with open("example.txt", "w") as f:
    f.write("This is written from main program ")


# SOME STRING OPERATION
greeting = "good morning"
print(greeting.upper()) # To uppercase
print(greeting.lower()) # make everything on greeting to lowercase
print(greeting.split()) # split the word 

# STRING FORMATTING

politician = "Gagan thapa"
age = 40 
print(f"His name is {politician} and he is {age} years old ")


