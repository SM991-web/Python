# with open("abc.txt","r+") as filetxt:
#     filetxt.write("Hello This is my abc.txt file")
#     filetxt.write("writing more contetnt\n")
#     filetxt.seek(0)
#     print(filetxt.read())
#     filetxt.write("I am a Programmer")
#     filetxt.write("I am a Programmer with expert in python")
    
    

with open("example.txt","w+")as file:
    file.write("new line for code")
    file.seek(0)
    a=file.read()
    print(a)
