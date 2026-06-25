"""
a program for read a list, uppercase, write to new file csv format
"""

with open("data.csv", "r") as fd:
    first_line = fd.readlines()
first_line[0] = first_line[0].upper()  # uppercase first line
print(first_line)
with open ("new_data.csv" , "w") as www:
    www.writelines (first_line)        # write to new file csv format



        

