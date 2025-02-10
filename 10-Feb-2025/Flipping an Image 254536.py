# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        # reverse each row
        for row in image:
            row = row.reverse()

        for row in range(len(image)):
            for col in range(len(image[0])):
                if image[row][col] == 0:
                    image[row][col] = 1
                elif image[row][col] == 1:
                    image[row][col] = 0
        
        return image