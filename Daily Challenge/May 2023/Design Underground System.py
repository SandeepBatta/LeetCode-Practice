# # Challenge Context
# An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

# Challenge Link --> https://leetcode.com/problems/design-underground-system/


class UndergroundSystem:
    def __init__(self):
        # user log format
        # {
        #     45: [
        #         {
        #             "checkIn": {"stationName": "Leyton", "time": 3},
        #             "checkOut": {"stationName": "Waterloo", "time": 3},
        #         }
        #     ]
        # }
        self.user_logs = {}
        self.time_bw_stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        logs = self.user_logs.get(id, None)
        # Update the user log. Create the id if user not present.
        if logs is not None:
            self.user_logs[id].append(
                {"checkIn": {"stationName": stationName, "time": t}}
            )
        else:
            self.user_logs[id] = [{"checkIn": {"stationName": stationName, "time": t}}]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Update the user log
        self.user_logs[id][-1]["checkOut"] = {"stationName": stationName, "time": t}

        # Update the travel time between stations
        checkin_station = self.user_logs[id][-1]["checkIn"]
        checkout_station = self.user_logs[id][-1]["checkOut"]
        route = (checkin_station["stationName"], checkout_station["stationName"])
        travel_time = checkout_station["time"] - checkin_station["time"]
        if self.time_bw_stations.get(route, None) is not None:
            self.time_bw_stations[route].append(travel_time)
        else:
            self.time_bw_stations[route] = [travel_time]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.time_bw_stations[(startStation, endStation)]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
