class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        output = []
        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)
        for lis in hashmap.values():
            output.append(lis)
        return output