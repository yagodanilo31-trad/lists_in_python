#list1
list = []

while True:
    key = input("y / n or E to exit: ")
    if key == "y":
        food = input(": ")
        list.append(food)
        print("-".center(20, '-'))
        print(sep="|",*list)
        print("-".center(20, '-'))
    elif key == "n":
        delete = list.pop()
        print("-".center(20, '-'))
        print(sep="|",*list)
        print("-".center(20, '-'))
    elif key == "E":
        print("-".center(20, '-'))
        print(sep="|",*list)
        print("-".center(20, '-'))
        break
    else:
        print("-".center(20, '-'))
        print(sep="|",*list)
        print("-".center(20, '-'))
        print("invalid")

#list2
list = []

while True:
    key = input("y / n or E to exit: ")
    print("-".center(20, '-'))
    if key == "y":
        food = input(": ")
        list.append(food)
        print("-".center(20, '-'),"\n",sep="|",*list)
    elif key == "n":
        delete = list.pop()
        print("-".center(20, '-'),"\n",sep="|",*list)
    elif key == "E":
        print("-".center(20, '-'),"\n",sep="|",*list)
        break
    else:
        print("invalid")
        print("-".center(20, '-'),"\n",sep="|",*list)
        print("-".center(20, '-'))
    print("-".center(20, '-'))


#list3
list = []

while True:
    key = input("y / n or E to exit: ")
    print("-".center(20, '-'))
    if key == "y":
        food = input(": ")
        list.append(food)
        print("-".center(20, '-'),"\n",sep="|",*list)
    elif key == "n":
        item = input(": ")
        if item in list:
            delete = list.remove(item)
            print("-".center(20, '-'),"\n",sep="|",*list)
        else:
            print("-".center(20, '-'),"\n","It's not in list")
            print("-".center(20, '-'),"\n",sep="|",*list)
    elif key == "E":
        print("-".center(20, '-'),"\n",sep="|",*list)
        break
    else:
        print("invalid")
        print("-".center(20, '-'),"\n",sep="|",*list)
        print("-".center(20, '-'))
    print("-".center(20, '-'))
