from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        res = ''

        l, h = 0, len(values) - 1
        while l <= h:
            m = (l + h) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                h = m - 1

        return res