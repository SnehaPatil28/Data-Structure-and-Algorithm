class Solution:
    def exitPoint(self, mat):
        row = len(mat)
        col = len(mat[0])
        
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        r, c = 0, 0
        direction = 0
        
        while True:
            if mat[r][c] == 1:
                mat[r][c] = 0
                direction = (direction + 1) % 4
                
            next_r = r + dr[direction]
            next_c = c + dc[direction]  
            
            if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col:
                return [r, c]
                
            r = next_r
            c = next_c
