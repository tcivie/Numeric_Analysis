def Bisection_Method(polynome, distance, epsilon=0.0001):
    """
    Finds the root of the polynome using the bisection method
    :param polynome: The polynome EX: lambda x: (x*x) - 4
    :param distance: The distance to look in the solution for the polynome
    :param epsilon: The max distance to stop
    :return: The solution to the problem with epsilon as the max error
    """
    mid = 0
    MAX_RUNS = 100
    i = 0
    while abs(distance[0] - distance[1]) > epsilon and i < MAX_RUNS:
        # Run till the distance between the points is the lowest or passed max runs
        mid = (distance[0] + distance[1]) / 2
        if polynome(distance[0]) * polynome(mid) > 0:
            distance[0] = mid
        else:
            distance[1] = mid
        print(f'X{i} = {mid}')
        i += 1
    if i == MAX_RUNS:
        print("Error: Couldn't find the point due to max runs reached")
    return mid


print(Bisection_Method(lambda x: (x * x) - 4, [-1, 3]))
