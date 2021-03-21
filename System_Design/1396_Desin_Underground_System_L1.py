""" double hash table
Use two hash tables. 
The first to save the check-in time for a customer
and the second to update the total time between two stations.
"""
class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.trip = defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (preStation, preT) = self.customer[id]
        if (preStation, stationName) not in self.trip:
            self.trip[(preStation, stationName)] = [t-preT, 1]
        else:
            self.trip[(preStation, stationName)][0] += t-preT
            self.trip[(preStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.trip[(startStation, endStation)][0]/self.trip[(startStation, endStation)][1]