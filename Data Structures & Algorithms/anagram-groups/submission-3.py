class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        groups = []
        for i in strs:
            key = "".join(sorted(i))
            if key not in map:
                map[key] = []
            map[key].append(i) # append non-sorted version of word into slot by its sorted key eg. cat -> act: act gets appended under the ['cat'] key
        
        for i in map:
            groups.append(map[i])
        return groups

                
