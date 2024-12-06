shapes = ["Square", "Trapezium", "Parallelogram", "Circle", "Triangle", "Rectangle", "Ellipse", "Trapezoid"]

print(shapes)

def choose():
    global chosen_shape
    chosen_shape = input("Please write a shape from the list above. \n").lower()

def invalid_shape():
    print("You input an invalid shape!")

def area_shape():
    if chosen_shape == ("square"):
        global square_length
        square_length = int(input("What is the length of all four sides of the square? \n"))
        print(f"The area of the square is {square_length*square_length}.")
    else:(invalid_shape())

choose()
area_shape()

