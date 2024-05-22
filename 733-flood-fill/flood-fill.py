class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.fill(image, sr, sc, color, image[sr][sc])
        return image

    def fill(self, image, i, j, color, start):
        if i >= 0 and i < len(image) and j >= 0 and j < len(image[0]) and image[i][j] == start:
            image[i][j] = color
            self.fill(image, i-1, j, color, start)
            self.fill(image, i+1, j, color, start)
            self.fill(image, i, j-1, color, start)
            self.fill(image, i, j+1, color, start)
        else:
            return