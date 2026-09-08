class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        graph = {}
        l = 0 
        res = 0
        max_freq = 0
        for i in range(len(s)):
            graph[s[i]] = graph.get(s[i],0) + 1
            max_freq = max(max_freq,graph[s[i]])
            while i - l + 1 - max_freq > k :
                graph[s[l]] -= 1
                l+= 1
            res = max(res , i - l + 1)
        return res

        