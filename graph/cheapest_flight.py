"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w .
Now given all the cities and fights, together with starting city src and the destination dst , your task is to find
the cheapest price from src to dst with up to k stops . If there is no such route, output -1.

Note:
- The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
- The size of flights will be in range [0, n * (n - 1) / 2].
- The format of each flight will be (src, dst, price).
- The price of each flight will be in the range [1, 10000].
- k is in the range of [0, n - 1].
- There will not be any duplicated flights or self cycles.
"""


def find_cheapest(n: int, flights: list, src: int, dst: int, k: int) -> int:
    """
    :param n: the number of cities
    :param flights: llist[list[int]] where each inner list is [ staring_city, destination_city , price of flight ]
    :param src: the starting city
    :param dst: the destination city
    :param k: the maximum stops allowed
    :return: int, the cheapest price given the above info
    """
    # construct dictionary maps from start_city to ( next_city , price it takes)
    prices={}
    for flight in flights:
        if flight[0] in prices:
            prices[flight[0]] = (flight[1],flight[2])
    # get the cheapest path by dijkstra
    import queue


