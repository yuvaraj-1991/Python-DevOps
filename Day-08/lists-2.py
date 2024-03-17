import os

#STEPS:-
#Read input from the user 
#Write the for loop as user will provide you the sequence to run code on all folders for list files
#identify modules required
#Print files
#Handle any errors

# number1 = input('Please enter a number : ')

# print(number1)

#STEP1 take the input from users and convert it to a list
folders_list = input("Please provide list of folders names with spaces in between : ").split()
print(folders_list)

#STEP2 we will run for loop for each item/element for Input provided by users and 
#Exception handling for the errors.
for folder in folders_list:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like this folder does not exit :" + folder) 
        break
    except PermissionError:
        break
        print("No access to this folder : " + folder)
    # print("======listing files for each folder ===== " + folder)
    # print(files)
    

    for file in files:
        print(file)
    

