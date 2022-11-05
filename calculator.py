
starting = input("""
    
    Hello And Welcome To My simple calcultor
    I hope you get even a little use out of it
    
    Press [+] To Addition
    Press [-] To Subtraction
    Press [*] To Multiplication
    Press [/] To Division
    Press [E] To Exit
    
    Enter the process you want: """)

def Addition():
    if(starting == "+"):
        num1 = int(input("[*] Enter The First Number: "))
        num2 = int(input("[*] Enter The Socend Number: "))
        print(num1 + num2)
Addition()

def Subtraction():
    if(starting == "-"):
        num1 = int(input("[*] Enter The First Number: "))
        num2 = int(input("[*] Enter The Socend Number: "))
        print(num1 - num2)
Subtraction()

def Multiplication():
    if(starting == "*"):
        num1 = int(input("[*] Enter The First Number: "))
        num2 = int(input("[*] Enter The Socend Number: "))
        print(num1 * num2)
Multiplication()

def Division():
    if(starting == "/"):
        num1 = int(input("[*] Enter The First Number: "))
        num2 = int(input("[*] Enter The Socend Number: "))
        print(num1 / num2)
Division()

def Exit():
    if(starting == "E"):
        print('''THANK YOU FOR USING MY TooL:)

        insta:darsek_
        github:saleh-888''')
Exit()
