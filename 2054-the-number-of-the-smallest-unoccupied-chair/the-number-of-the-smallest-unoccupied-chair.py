class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        event = []
        for i in range(len(times)):
            [arrival,leaving] = times[i]
            event.append((arrival,0,i))
            event.append((leaving,1,i))
        event.sort(key=lambda x : (x[0],x[1] == 0))
        available_chair = []
        next_chair = 0
        chair_assignment = {}
        for time,event_type,friend_index in event:
            if event_type == 0:
                if available_chair:
                    chair = heapq.heappop(available_chair)
                else:
                    chair = next_chair
                    next_chair += 1
                chair_assignment[friend_index] = chair
                if friend_index == targetFriend:
                    return chair
            else:  
                chair = chair_assignment[friend_index]
                heapq.heappush(available_chair, chair)
        return -1