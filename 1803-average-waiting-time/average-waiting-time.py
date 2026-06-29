class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        order_taken = 0
        for arrival,wait in customers:
            order_taken = max(order_taken,arrival) + wait
            total_time += order_taken - arrival
        return total_time / len(customers)