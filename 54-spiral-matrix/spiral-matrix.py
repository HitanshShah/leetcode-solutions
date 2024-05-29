class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        ans = []
        count = rows*cols
        direction = 0
        left, right, top, bot = 0, cols, 0, rows
        while count > 0:
            if direction == 0:
                while j < right:
                    ans.append(matrix[i][j])
                    j+=1
                    count-=1
                j-=1
                i+=1
                top+=1
                direction = (direction+1)%4
            elif direction == 1:
                while i < bot:
                    ans.append(matrix[i][j])
                    i+=1
                    count-=1
                i-=1
                j-=1
                right-=1
                direction = (direction+1)%4
            elif direction == 2:
                while j >= left:
                    ans.append(matrix[i][j])
                    j-=1
                    count-=1
                j+=1
                i-=1
                bot-=1
                direction = (direction+1)%4
            else:
                while i >= top:
                    ans.append(matrix[i][j])
                    i-=1
                    count-=1
                i+=1
                j+=1
                left+=1
                direction = (direction+1)%4
            print(ans)
        return ans
