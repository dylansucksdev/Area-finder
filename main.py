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
    elif chosen_shape == ("parallelogram"):
        parallelogram_base_length = float(input("What is the base length of the parallelogram? \n"))
        parallelogram_height = float(input("What is the height of the parallelogram? \n"))
        print(f"The area of the parallelogram is {parallelogram_base_length*parallelogram_height}.")
    elif chosen_shape == ("circle"):
        circle_radius = float(input("What is the radius of the circle? \n"))
        print(f"The area of the circle is {3.141592653589793*circle_radius*circle_radius}.")
    elif chosen_shape == ("triangle"):
        triangle_base_length = float(input("What is the base length of the triangle? \n"))
        triangle_height = float(input("What is the height of the triangle? \n"))
        print(f"The area of the triangle is {0.5*triangle_base_length*triangle_height}.")
    elif chosen_shape == ("rectangle"):
        rectangle_length = float(input("What is the length of the rectangle? \n"))
        rectangle_height = float(input("What is the height of the rectangle? \n"))
        print(f"The area of the rectangle is {rectangle_length*rectangle_height}.")
    elif chosen_shape == ("ellipse"):
        ellipse_major_axis = float(input("What is the major axis of the ellipse? \n"))
        ellipse_minor_axis = float(input("What is the minor axis of the ellipse? \n"))
        print(f"The area of the ellipse is {(3.141592653589793*ellipse_major_axis*ellipse_minor_axis)/2}.")
    else:(invalid_shape())

choose()
area_shape()

