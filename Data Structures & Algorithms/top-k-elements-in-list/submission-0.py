class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        for num in count :
            if len(heap) == k:
                heapq.heappushpop(heap,(count[num] , num))
            else :
                heapq.heappush(heap,(count[num],num))
        output = []
        for fre,num in heap:
            output.append(num)
        return output
        