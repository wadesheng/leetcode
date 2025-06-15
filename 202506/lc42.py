class Solution(object):
    def trap(self, height) -> int:
        if height is None or len(height) <= 0:
            return 0        
        return self.total_size(height) - self.total_columns(height)

    def total_size(self, height) -> int:
        new_height = []
        max_height = 0
        max_height_index = 0
        for i in range(len(height)):
            new_height.append(0)
            if height[i] > max_height:
                max_height = height[i]
                max_height_index = i
        print("Max height = :", max_height, " at index = :", max_height_index)

        for j in range(max_height_index + 1):
            print("j = :", j)
            if (j == 0) or (j == max_height_index):
                new_height[j] = height[j]
            elif (height[j] < new_height[j - 1]):
                new_height[j] = new_height[j - 1]
            else:
                new_height[j] = height[j]
           
        for k in range(len(height) - 1, max_height_index, -1):
            print("k = :", k)
            if (k == len(height) - 1):
                new_height[k] = height[k]
            elif (height[k] < new_height[k + 1]):
                new_height[k] = new_height[k + 1]
            else:
                new_height[k] = height[k]    
        print("New height = :", new_height)          
        return self.total_columns(new_height)

    def total_columns(self, height) -> int:
        size = 0
        for i in range(len(height)):
            size += height[i]
        print("Total size = :", size)
        return size
    
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap(height))  # Output: 6