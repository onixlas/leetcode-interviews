def find_min_arrow_shots(points: list[list[int]]) -> int:
    """
    Calculate the minimum number of arrows needed to burst all balloons.

    The balloons are represented as intervals on a 2D plane (start and end points).
    An arrow shot at x-coordinate x bursts all balloons whose interval includes x.
    The function uses a greedy algorithm to find the optimal shooting points.

    :param points: A list of balloon intervals, where each interval is represented as [start, end]
    :return: The minimum number of arrows required to burst all balloons
    """
    points.sort(key=lambda x: x[1])

    shots = 1
    current_point = points[0]

    for point in points:
        if point[0] > current_point[1]:
            shots += 1
            current_point = point
    return shots

assert find_min_arrow_shots([[10,16],[2,8],[1,6],[7,12]]) == 2, 'Test 1 Failed'
assert find_min_arrow_shots([[1,2],[3,4],[5,6],[7,8]]) == 4, 'Test 2 Failed'