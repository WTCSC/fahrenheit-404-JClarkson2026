import time

class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"°"
def celsius(value, request):
    if request == "f":
        return f"{(value * 1.8) + 32} °F"
    elif request == "c":
        return f"{value} °C"
    else:
        return f"{value + 273.15} K"

def fahrenheit(value, request):
    if request == "c":
        return f"{(value - 32) * 0.5555 } °C"
    elif request == "f":
        return f"{value} °F"
    else:
        return celsius((value - 32) * 0.5555,"k")

def kelvin(value,request):
    if request == "c": 
        return f"{value - 273.15} °C"
    elif request == "k":
        return f"{value} K"
    else:
        return celsius(value-273.15,"f")

def formValid(NorS,ask):
    if NorS == "string":
        userInput = input(ask).lower()
        if userInput[0] == "c" or userInput[0] == "f" or userInput[0] == "k":
            return userInput[0]
        else:
            print("User input invalid! Try again.")
            return formValid(NorS,ask)
    else:
        userInput = input(ask)
        if int(userInput):
            return int(userInput)
        elif userInput[0] == "0":
            return 0
        else:
            print("User input invalid! Try again.")
            return formValid(NorS,ask)

def run():
    askName = input(f"{bColors.HEADER}What is your {bColors.WARNING}name{bColors.HEADER}? ")
    print(f"{bColors.HEADER}Welcome to Fahrenheit {bColors.OKBLUE}404{bColors.HEADER},{bColors.WARNING} {askName}{bColors.HEADER}!")
    time.sleep(0.6)
    
    askCurrentType = formValid("string",f"{bColors.HEADER}What type do you have?{bColors.FAIL} fahrenheit (F){bColors.OKCYAN} kelvin (K){bColors.OKGREEN} celsius (C)? {bColors.HEADER}")
    time.sleep(0.3)
    askDesiredType = formValid("string",f"{bColors.HEADER}What type do you want?{bColors.FAIL} fahrenheit (F){bColors.OKCYAN} kelvin (K){bColors.OKGREEN} celsius (C)? {bColors.HEADER}")

    string = "Loading"
    for i in range(1,6):
        if i == 4:
            string = "Loading."
        else:
            string = string + "."
        print(string)
        time.sleep(.2)
        print ("\033[A                                                                           \033[A")
    
    askNumOne = formValid("num",f"{bColors.HEADER}What is your {bColors.OKBLUE}temperature{bColors.HEADER}? ")
    time.sleep(0.3)
    if askCurrentType == "f":
        print(f"{fahrenheit(askNumOne,askDesiredType)}")
    elif askCurrentType == "c":
        print(f"{celsius(askNumOne,askDesiredType)}")
    else:
        print(f"{kelvin(askNumOne,askDesiredType)}")
run()