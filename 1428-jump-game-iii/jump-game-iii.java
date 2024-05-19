class Solution {
    boolean ans = false;
    public boolean canReach(int[] arr, int start) {
        int n = arr.length;
        boolean[] visited = new boolean[n];
        helper(arr, start, visited);
        return ans;
    }
    public void helper(int[] arr, int start, boolean[] visited){
        visited[start] = true;
        if(arr[start] == 0){
            ans = true;
            return;
        }
        if(start-arr[start] >= 0 && !visited[start-arr[start]]) helper(arr, start-arr[start], visited);
        if(start+arr[start] < arr.length && !visited[start+arr[start]]) helper(arr, start+arr[start], visited);
    }
}