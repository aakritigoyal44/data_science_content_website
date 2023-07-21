name_list=(names.txt)
check='letter'
res = [idx for idx in name_list if idx[0].lower() == check.lower()]
if check in name_list:
    return(f"{check} exists")
else:
     return(f"{check} does not exist")   


def main():
    print("enter the letter")
    check=name_list
    print("The list of matching first letter : " + str(res))
    
