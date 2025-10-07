
print("Welcome to circle area calculator")

while True:
    r = input("Enter the radius of the circle whose area you want to find: ")

    try:
        r = float(r)   # Its better to use float because area could be decimal
        if r <= 0:
            print("Please enter a number that bigger than zero.")
            continue
        pi = 3.14
        circle_area = pi * (r ** 2)
        print("Area of circle is ", circle_area)
        break  # exit loop on correct entry
    except ValueError:
        print("Pleas enter a valid number.")
        
print( )
print("made by Ahmet H. Yalangün")

