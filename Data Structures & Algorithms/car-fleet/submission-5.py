class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [0] * n
        cars = sorted(zip(position, speed))

        for i, (pos, spd) in enumerate(cars):
            time[i] = (target - pos) / spd

        fleets = []
        current_time = 0
        for j in reversed(time):
            if not fleets:
                fleets.append([j])
            else:
                if j <= fleets[-1][0]:
                    fleets[-1].append(j)
                else:
                    fleets.append([j])

        return len(fleets)