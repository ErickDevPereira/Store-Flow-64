from typing import List, Any

class Algorithms:

    @staticmethod
    def binary_search(arr: List[Any], target) -> int | None:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid_ind = (left + right) // 2
            mid_val = arr[mid_ind]
            if mid_val == target:
                return mid_ind #Index with that value
            elif mid_val > target:
                right = mid_ind - 1
            elif mid_val < target:
                left = mid_ind + 1
        return None #Value wasn't found because it doesn't exist