from math_function import add, multiply, divide

def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)
    elif operator == "*":
        result = multiply(data_1, data_2)
    elif operator == "/":
        result = divide(data_1, data_2)
    else:
        print("Operator tidak valid")
        return
 print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if _name_ == "_main_":
    print("Hello Main !")
    main()