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
        square_length = float(input("What is the length of all four sides of the square? \n"))
        print(f"The area of the square is {square_length*square_length}.")
    elif chosen_shape == ("trapezium"):
        trapezium_base_length = float(input("What is the base length of the trapezium? \n"))
        trapezium_perpendicular_height = float(input("What is the perpendicular height of the trapezium? \n"))
        trapezium_top_length = float(input("What is the top length of the trapezium? \n"))
        print(f"The area of the trapezium is {(trapezium_base_length+trapezium_top_length)/2*trapezium_perpendicular_height}.")
    else:(invalid_shape())

choose()
area_shape()

