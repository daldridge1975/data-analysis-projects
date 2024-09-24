# Part 1 A -- Make a Line
# def make_line(size):
#     line = ""
#     for i in range(size):
#         line += "#"
#     return line
# print (make_line(5))



# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = ""
    for i in range(size):
        square += "#" * size + "\n"
    return square
print (make_square(5))





# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
    rectangle = ""
    for i in range(width,height):
        rectangle += "#" * width, height + "\n"
    return rectangle
print (make_rectangle(5,3))
    




# Part 2 A -- Make a Stairs

def make_downward_stairs(height):
    stairs = ""
    for i in range(1, height, +1):
        stairs += "#" * height +"\n"
    return stairs
print (make_downward_stairs(5))




# Part 2 B -- Make Space-Line 





# Part 2 C -- Make Isosceles Triangle





# Part 3 -- Make a Diamond






