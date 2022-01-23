class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        n = len(height)
        i, j = 0, n - 1
        while i < j:
            answer = max(answer, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return answer