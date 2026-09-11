class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            if i not in map:
                map[i]= 1
            map[i]+=1

        freq = []
        for key, val in map.items():
            freq.append([val, key])
        freq.sort()

        elements = []
        i = 0
        while i < k:
            elements.append(freq.pop()[1])
            i+=1
        return elements

        