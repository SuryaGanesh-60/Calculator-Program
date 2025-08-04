def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: Cannot divide by zero."
    return a / b
def main():
    print("Welcome to CLI Calculator")
    print("----------------------------")
    while True:
        print("\n Select Operation:")
        print("1.Add (+)")
        print("2.Subtract (-)")
        print("3.Multiply (*)")
        print("4. Divide (/)")
        print("5.Exit")
        choice=input("enter choice(1/2/3/4/5):")
        if choice =='5':
            print("Exiting Calculator.GoodBye!")
            break
        if choice in ('1','2','3','4'):
            try:
                num1=float(input("Enter first Number:"))
                num2=float(input("Enter Second Number:"))
            except ValueError:
                print("Invalid input.Please enter Number only.")
                continue
            if choice =='1':
                print(f"{num1} + {num2}={add(num1,num2)}")
            elif choice =='2':
                print(f"{num1} - {num2}={add(num1,num2)}")
            elif choice =='3':
                print(f"{num1} * {num2}={add(num1,num2)}")
            elif choice =='4':
                result =divide(num1,num2)
                print(f"{num1} / {num2}={add(num1,num2)}")
            else:
                print("Invalid input.Please enter a vaild choice(1/2/3/4).")
if __name__ == "__main__":
    main()  