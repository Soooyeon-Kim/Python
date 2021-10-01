import random

def main():

    print(random.random())

    print(random.randrange(1,10))

    lst = [1,2,3,4,5,6,7,8,9]
    print(lst)

    random.shuffle(lst)
    print(lst)

    print(random.choice(lst))
    
if __name__ == "__main__":
    main()
