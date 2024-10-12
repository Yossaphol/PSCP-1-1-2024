"""BusStop I"""
def main():
    """BusStop I"""
    amount = int(input())
    count = int(input())
    passenger_string = []
    passenger_integer = []
    at_home = 0
    for _ in range(count):
        bus = input().split()
        passenger_string.append(bus)
    passenger_string.sort(key=lambda i: int(i[0]))
    for i in passenger_string:
        stage_bus_stop = int(i[0])
        if len(passenger_integer):
            passenger_integer2 = passenger_integer.copy()
            for arrive in passenger_integer:
                if arrive == stage_bus_stop:
                    passenger_integer2.remove(arrive)
                    at_home += 1
            passenger_integer = passenger_integer2
        for j in range(1, len(i)):
            if len(passenger_integer) == amount:
                break
            if stage_bus_stop < int(i[j]):
                passenger_integer.append(int(i[j]))
    print(at_home)
main()
