def square_root(x):
    current_value = 1
    new_value = (current_value + x/current_value)/2

    def helper(x, current_value):
        return (current_value + x/current_value)/2
   
    
    while abs(new_value - current_value) > 0.005:
        current_value = helper(x, current_value)
        new_value = (current_value + x/current_value)/2
        print (current_value)
    
    return new_value    

                 
def main():
    print("Hello User!\n")
    print("Enter a number\n")
    input_a = int(input())
    print(f"The square root of {input_a} is:\n")
    print(square_root(input_a))

if __name__ == "__main__":
    main()