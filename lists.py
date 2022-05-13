import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# names_length =  len(names)
# print(names)
# print(names_length)

# random_choice = random.randint(0, names_length-1)
# print(random_choice)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + "is going to pay the bill today.")

# or we can use choice() method to get the same result as above
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to pay the bill today.")







