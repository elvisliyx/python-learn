# -*- coding:utf-8 -*-

age_of_oldboy = 41

# guess_age = int(input("guess age:"))
# if guess_age == age_of_oldboy:
#     print("yes,you got it.")
# elif guess_age > age_of_oldboy:
#     print("think smaller...")
# else:
#     print("think bigger...!")

count = 0
while True:
    if count == 3:
        break
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger...!")
    count +=1



count = 0
while count <3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger...!")
    count +=1
else:
    print("you have tried too my times..fuck off!")




