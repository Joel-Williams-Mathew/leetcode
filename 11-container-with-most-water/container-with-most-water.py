class Solution:
    def maxArea(self, height: List[int]) -> int:
        output = 0
        i = 0
        j = len(height) - 1

        while i != j:
            length = j-i
            breadth = min(height[i], height[j])
            area = length * breadth
            output = max(area, output)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return output
