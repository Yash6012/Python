import math

# Function to calculate the distance between two points
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Function to calculate the center and radius of a circle that passes through three points
def circle_center_radius(x1, y1, x2, y2, x3, y3):
    # Calculate the distances between each pair of points
    a = dist(x1, y1, x2, y2)
    b = dist(x2, y2, x3, y3)
    c = dist(x3, y3, x1, y1)

    # Calculate the semiperimeter
    s = (a + b + c) / 2

    # Calculate the radius of the circle
    r = (a * b * c) / (4 * math.sqrt(s * (s - a) * (s - b) * (s - c)))

    # Calculate the coordinates of the center of the circle
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    G = 2 * (A * (y3 - y2) - B * (x3 - x2))

    if G == 0:
        # Points are collinear
        return None

    # Calculate the coordinates of the center
    xo = (D * E - B * F) / G
    yo = (A * F - C * E) / G

    return (xo, yo, r)


# Get the coordinates of the three points from the user
x1, y1 = map(float, input("Enter the coordinates of the first point (x1, y1): ").split(','))
x2, y2 = map(float, input("Enter the coordinates of the second point (x2, y2): ").split(','))
x3, y3 = map(float, input("Enter the coordinates of the third point (x3, y3): ").split(','))

# Calculate the center and radius of the circle
result = circle_center_radius(x1, y1, x2, y2, x3, y3)

if result is None:
    print("The points are collinear, a circle cannot be formed.")
else:
    xo, yo, r = result
    print("The coordinates of the center are", xo, yo, "and the radius is", r)
