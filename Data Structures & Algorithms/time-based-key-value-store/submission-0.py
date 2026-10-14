class TimeMap:
    # NOT MY SOLUTION.
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key,[])
        L = 0
        R = len(values) - 1
        res = ""

        while L <= R:

            mid = (R + L) // 2

            if values[mid][1] <= timestamp:
                res= values[mid][0]
                L = mid + 1 
            else:
                R = mid - 1

        return res
