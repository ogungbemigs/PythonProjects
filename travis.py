known_user = ["Alice","Bob","Claire","Dan","Emma","Fred","George","Harry"]

print(len(known_user))

while True:
    name = input("What is your name?: ").strip().capitalize()
    if name in known_user:
        print("Hello {}".format(name))
        remove_user = input("Do you want to remove your name (y/n): ").lower()
        
        if remove_user == 'y':
            print("Its hard to see you go, bye {}".format(name))
            known_user.remove(name)
    else:
        print("I dont think we have met {}".format(name))
        add_user = input("Do you want me to add you to the list ?: (y/n)").lower()
        if add_user == 'y':
            known_user.append(name)
            print(known_user)