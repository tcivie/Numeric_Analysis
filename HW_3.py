MAX_RUNS = 100


def Bisection_Method(polynomial, distance, epsilon=0.0001):
    """
    Finds the root of the Polynomial using the bisection method
    :param polynomial: The Polynomial EX: lambda x: (x*x) - 4
    :param distance: The distance to look in the solution for the Polynomial
    :param epsilon: The max distance to stop
    :return: The solution to the problem with epsilon as the max error
    """
    mid = 0
    i = 0
    while abs(distance[0] - distance[1]) > epsilon and i < MAX_RUNS:
        # Run till the distance between the points is the lowest or passed max runs
        mid = (distance[0] + distance[1]) / 2
        if polynomial(distance[0]) * polynomial(mid) > 0:
            distance[0] = mid
        else:
            distance[1] = mid
        print(f'X{i} = {mid}')
        i += 1
    if i == MAX_RUNS:
        print("Error: Couldn't find the point due to max runs reached")
    return mid


def Newton_Raphson(polynomial, distance, epsilon=0.0001):
    """
    The method solves the root of the Polynomial in the given range using the newton Raphson method
    :param polynomial: The Polynomial to solve
    :param distance: The range where to look (Array<float>[2])
    :param epsilon: The error range
    :return:
    """
    pass


print(Bisection_Method(lambda x: (x * x) - 4, [-1, 3]))
