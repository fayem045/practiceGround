# #create an pyramid from a character.(f11 to run)
# char = input("Enter a character: ")
# for i in range(1,7):
#     print(char*i)

# print("")
# print("Play2: pyramid")
#create center pyramid
char2 = input("Enter a Character: ")
for i in range(1,8):
    # print((char2*i).center(20))
    spaces = 7 - i
    characters = 2 * i  - 1
    print(" " * spaces + char2 * characters + " " * spaces)
    
print("")
print("Playe2: update the list")
fruits = ["Apple", "orange", "Banana"]
fruits.insert(2, "Lychee")
#apply,orange,lychee,banana
print(fruits)

print(" ")
print("play3: counting similarities in a list")
students = ["angela", "nana", "Zilong", "nana"]
#case sensitive
print(students.count("nana"))
