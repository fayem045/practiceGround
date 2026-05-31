#create an pyramid from a character.(f11 to run)
char = input("Enter a character: ")
for i in range(1,7):
    print(char*i)

print("")
print("Play2")
#create center pyramid
char2 = input("Enter a Character: ")
for i in range(1,8):
    print((char2*i).center(20))