# operators

x=["apple","banana"]
y=["apple","banana"]
z=x
# identity operator

print(x is y) #loaction and address is not same
print(x is z) #both have same location
print(x == y)
print(x is not y) # return True

#memebership operators

print("apple" in x)
print("apple" in y)
print("banana" in z)

# bitwise operator

print(1&3)
print(2|5)
print(2^5)
print(~5)
print(2<<5)
print(34>>4)

#logical operator
print(7 and 2 or 8 or 5 and 8)

# precedence operator
print(5+4-7+3)
