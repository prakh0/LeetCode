class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        n = numberOfUsers 
        mentions = [0] * n
        is_online = [0] * n
        events.sort(key = lambda x: (int(x[1]),x[0] == "MESSAGE"))

        for m,t,ids in events:
            if m == "OFFLINE":
                is_online[int(ids)] = int(t) + 60
                continue 

            for i in ids.split():
                if i == "ALL":
                    for j in range(n):
                        mentions[j] += 1
                elif i == "HERE":
                    for j in range(n):
                        if int(t) >= is_online[j]:
                            mentions[j] += 1
                else:
                    mentions[int(i[2:])] += 1
        return mentions