def For_Loop():
    number=[1,2,3,4,5,6,7,8,9,10]
    for number in number:
        print("Looking at : "+ str(number))
        if number>6:
            print("Too big : "+ str(number),"!\n")
            break
For_Loop()

def For_Loop():
    number=[2,6,7,4,1,9,8,10]
    for number in number:
        if number > 6:
            continue
        print("Looking at : "+ str(number))
For_Loop()