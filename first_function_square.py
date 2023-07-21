def square(x, y):
    return x**y
    
def main():
    print("Hello World!\n")
    print("Enter a number\n")
    input_a = int(input())
    print("what power of this number do you want?\n")
    input_b = int(input())

    print("Doing the job for you!!!!\n")

    print(square(input_a, input_b))

if __name__ == "__main__":
    main()