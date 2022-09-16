def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
    
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

def pow(a,b):
    answer = a ** b
    print(str(a) + " ** " + str(b) + " = " + str(answer) + "\n")

def modulo(a,b):
    answer = a % b
    print(str(a) + " % " + str(b) + " = " + str(answer) + "\n")

while True:
    print("Choose operator you want! Can Just Input Integer Number")
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Pow")
    print("F. Modulo")
    print("G. Exit")

    choice = input("Input Your Choice: ")
    
    if choice == "a" or choice == "A":
        print("Addition")
        a = float(input("Input Number Here: ")) 
        b = float(input("Input Number Here: ")) 
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Substraction")
        a = float(input("Input Number Here: "))
        b = float(input("Input Number Here: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = float(input("Input Number Here: "))
        b = float(input("Input Number Here: "))
        mul(a,b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = float(input("Input Number Here: "))
        b = float(input("Input Number Here: "))
        div(a,b)
    elif choice == "e" or choice == "E":
        print("Pow")
        a = float(input("Input Number Here: "))
        b = float(input("Input Number Here: "))
        pow(a,b)
    elif choice == "f" or choice == "F":
        print("Modulo")
        a = float(input("Input Number Here: "))
        b = float(input("Input Number Here: "))
        modulo(a,b)
    elif choice == "g" or choice == "G":
        print("Game Ended")
        quit()

