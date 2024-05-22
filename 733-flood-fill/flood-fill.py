class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.fill(image, sr, sc, color, image[sr][sc])
        return image

    def fill(self, image, i, j, color, start):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
            return
        if image[i][j] == color:
            return
        elif image[i][j] == start:
            image[i][j] = color
            self.fill(image, i-1, j, color, start)
            self.fill(image, i+1, j, color, start)
            self.fill(image, i, j-1, color, start)
            self.fill(image, i, j+1, color, start)
        else:
            return