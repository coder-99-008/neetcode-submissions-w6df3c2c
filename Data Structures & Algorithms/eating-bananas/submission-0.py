class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0

        while low <= high:
            speed = (low + high) // 2
            currHour = 0
            for pile in piles:
                currHour += math.ceil(pile / speed)
            
            if currHour <= h:
                ans = speed
                high = speed - 1
            else:
                low = speed + 1

        return ans