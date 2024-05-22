class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        def fill(i, j):
            if i >= 0 and i < len(image) and j >= 0 and j < len(image[0]) and image[i][j] == start:
                image[i][j] = color
                fill(i-1, j)
                fill(i+1, j)
                fill(i, j-1)
                fill(i, j+1)

        if image[sr][sc] != color:
            fill(sr, sc)
        return image

    