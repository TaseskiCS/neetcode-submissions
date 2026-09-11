class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        map = {}
        groups = []

        for i in strs:
            key = "".join(sorted(i))
            if key not in map:
                map[key] = []
            map[key].append(i)  # don't check for duplicates — all are valid

        for i in map:
            groups.append(map[i])
        return groups
                
