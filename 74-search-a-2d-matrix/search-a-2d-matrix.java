class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        for(int i=0; i<m; i++){
            if(target >= matrix[i][0] && target <= matrix[i][n-1]){
                for(int j=0; j<n; j++){
                    if(matrix[i][j] == target) return true;
                }
            }else continue;
        }
        return false;
    }
}