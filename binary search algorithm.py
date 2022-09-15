def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = int(input("Put Your target: ")) # made this input from user

binary_search(my_list, target)

while True: #choice to play again
    play = input("Still wanna play ? (y,n) ")
    if play == "Y" or play == "y":
        target1 = int(input("Put Your target: "))
        binary_search(my_list, target1)
    elif play == "N" or play == "n":
        quit()
