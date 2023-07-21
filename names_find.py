def check_name(filepath, input_name):
    with open(filepath) as f:
        data = f.read()
        print(data)
        data = data.replace(","," ")
        print(data)
        names_vec = data.split()
        print(names_vec)
        print(names_vec)
        if input_name in names_vec:
            return(f"{input_name} exists")
        else:
            return(f"{input_name} does not exist")    
            
            
# Write a function that find names starting with a given letter

def main():
    print("hello\n")
    print("enter a name\n")
    input_data = str(input())
    print(f"enter the name {input_data} \n")
    
    print(check_name("names.txt", input_data))


if __name__ == "__main__":
    main() 
 