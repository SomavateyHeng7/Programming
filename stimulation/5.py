# Prompt the user for the values of a, b, and c
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Compute the discriminant
discriminant = b**2 - 4*a*c

# Determine the nature of the roots and compute the roots (if any)
if discriminant < 0:
    print("The quadratic function has no real roots.")
elif discriminant == 0:
    root = -b / (2*a)
    print("The quadratic function has one real root:", root)
else:
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print("The quadratic function has two real roots:", root1, "and", root2)
