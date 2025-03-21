import subprocess

def main():
    print("Welcome to the Modular Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Select an operation (1-4): ")

    if choice == "1":
        subprocess.run(["python", "add.py"])
    elif choice == "2":
        subprocess.run(["python", "subtract.py"])
    elif choice == "3":
        subprocess.run(["python", "multiply.py"])
    elif choice == "4":
        subprocess.run(["python", "divide.py"])
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
