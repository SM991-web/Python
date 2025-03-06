with open("demofile.txt","w+")as t:
    print(t.write("Hello, welcome to the world of Python"))
    # print(t.seek(0))
    print(t.read())
    # print(len(t))
# f=open("demofile.txt","r")    
# import os 
# print(os.getcwd())
# import os

# # Specify the directory
# directory = "c:/VS files/Python/specific_directory"

# # Ensure the directory exists
# if not os.path.exists(directory):
#     os.makedirs(directory)

# # Specify the full path to the file
# file_path = os.path.join(directory, "demofile.txt")

# # Open the file in the specified directory
# with open(file_path, "w+") as txtfile:
#     print(txtfile.write("Hello, welcome to the world of Python"))
#     txtfile.seek(0)  # Move the cursor to the beginning of the file
#     print(txtfile.read())

# # Print the current working directory
# print(os.getcwd())