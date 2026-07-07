class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def repair_time(time: int) -> bool:
            total_car = 0
            for rank in ranks:
                max_car = int((time//rank) ** 0.5)
                total_car += max_car
                if total_car >= cars:
                    return True
            return False   
        low,high = 1, max(ranks) * cars * cars
        while low < high:
            time = low + (high - low) // 2
            if repair_time(time):
                high = time
            else:
                low = time + 1
        return high
        