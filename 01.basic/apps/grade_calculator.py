marks = float(input("Enter your marks:"))

if marks <= 100:

    if marks >= 80:
        print('A+')

    elif marks >= 70:
        print('A')

    elif marks >= 60:
        print('A-')

    elif marks >= 50:
        print('B')

    elif marks >= 40:
        print('C')

    elif marks >= 33:
        print('D')

    elif marks < 0:
        print("Negative  number aren't supported")

    elif marks <= 32.99:
        print('F')
else:
    print("The data you have inputted is not supported")
