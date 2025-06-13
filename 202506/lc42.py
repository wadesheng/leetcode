class Solution(object):
    def trap(self, height):
        if height is None or len(height) <= 0:
            return 0        
        return self.total_size(height) - self.total_columns(height)

    def total_size(self, height) -> int:
        new_height = []
        for i in range(len(height)):
            if i == 0 || i == len(height) - 1:
                new_height.append(height[i])
            
            if (height[i] < height[i - 1]):
                new_height.append(height[i - 1])
            else:
                new_height.append(height[i])
                
        return self.total_columns(new_height)

    def total_columns(self, height) -> int:
        size = 0
        for i in range(len(height)):
            size += height[i]
        return size