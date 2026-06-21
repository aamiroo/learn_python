"""
calculator
"""

# input return string
first_number = int(input("adade aval ra vard kon: "))
second_number = int(input("adade dovom ra vard kon: "))

# # gamme dovom : mohased
jam = first_number + second_number
tafrig = first_number - second_number
zarb = first_number * second_number
tagsim = first_number / second_number

# gamme sevom : chaap
print(f"{first_number} + {second_number} = {jam}")
print(f"{first_number} - {second_number} = {tafrig}")
print(f"{first_number} * {second_number} = {zarb}")
print(f"{first_number} / {second_number} = {tagsim}")
