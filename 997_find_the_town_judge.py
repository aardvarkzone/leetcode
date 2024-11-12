class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #directed graph, no weights
        #no need to do search, just find who has n-1 incoming edges, 0 outgoing
        trust_list = [0] * (n + 1)

        for trusting, trusted in trust:
            trust_list[trusting] -= 1
            trust_list[trusted] += 1

        for index, trust_level in enumerate(trust_list):
            if index == 0: continue
            if trust_level == n - 1: return index
        
        return -1
