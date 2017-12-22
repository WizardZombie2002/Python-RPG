def incircle_radius(a,b,c):
    """Returns the inradius of a triangle."""
    area = triangle_area(a,b,c)
    return 2*area/(a+b+c)

def triangle_area(a, b, c):
    """Returns the area of a triangle using Heron's Formula."""
    # Get the semiperimeter
    s = (a+b+c)/2

    return (s*(s-a)*(s-b)*(s-c))**(1/2)

# Get sidelengths
lengths = input("Enter the sidelengths in this format: x y z").split()

# Convert the values to integers
l = []
for i in lengths:
    l.append(int(i))

# Return values
print("Area:", triangle_area(l[0], l[1], l[2]))
print("Inradius:",incircle_radius(l[0],l[1],l[2]))


# a multiplication table for digits
def multiplication_table():
    '''multiplication_table() -> none
    prints a multiplication table for base 10
    that is 10 x 10.'''
    # prints the top row
    string = ''
    topRowString = ''
    for column in range(1,11):
        topRowString += '\t' + str(column)
    print(topRowString)
    string += topRowString + '\n'
    
    # print each subsequent row
    for row in range(1,11):
        rowString = str(row)
        for column in range(1,11):
            rowString += '\t' + str(row*column)
        print(rowString)
        string += rowString + '\n'
    return string
multiplication_table()
