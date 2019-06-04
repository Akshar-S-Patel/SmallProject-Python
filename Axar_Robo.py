def extract_int_from_str(text):
    nums = []
    for txt in text.split(" "):
        try:
            nums.append(float(txt))
        except ValueError:
            pass
    return nums


def lcm(num1, num2):
    l = num1 if num1 > num2 else num2
    while l <= num1 * num2:
        if l % num1 == 0 and l % num2 == 0:
            return l
        l += num1 if num1 > num2 else num2


def hcf(num1, num2):
    h = num1 if num1 < num2 else num2
    while h >= 1:
        if num1 % h == 0 and num2 % h == 0:
            return h
        h -= 1


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Can not divide by zero")


def end():
    print("Good Bye")
    input("Press any key to exit")
    exit()


def myName():
    print("I am Axar")


def hi():
    print("Hiii")


def sorry():
    print("Sorry, This is beyond my ability")


operators = {"PLUS": add, "ADD": add, "ADDITION": add, "SUM": add, "MINUS": subtract, "SUBTRACTION": subtract,
             "SUBTRACT": subtract, "PRODUCT": multiply, "MULTIPLICATION": multiply, "MULTIPLY": multiply,
             "DIVIDE": division, "DIVISION": division, "LCM":lcm, "HCF":hcf}

commands = {"HI": hi, "NAME": myName, "END": end, "EXIT": end, "CLOSE": end}


def main():
    print("My name is Axar\nWelcome to my world")

    while True:
        print()
        words = input("Enter Text : ")
        for word in words.split(" "):
            if word.upper() in operators.keys():
                try:
                    nums = extract_int_from_str(words)
                    print(operators[word.upper()](nums[0], nums[1]))
                except IndexError:
                    print("Something is wrong plz try again")
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
        else:
            sorry()


if __name__ == '__main__':
    main()
