class Solution {
    public int jump(int[] nums) {
        int maxdist = 0;
        int ans = 0;
        int len = nums.length;
        if(len == 1) return 0;
        int curr = 0;
        while(curr < len){
            ans++;
            maxdist = curr+nums[curr];
            if(maxdist >= len-1) break;
            int next = curr;
            int range = 0;
            for(int i=curr+1; i<=maxdist; i++){
                if(i+nums[i] >= range){
                    range = i+nums[i];
                    next = i;
                }
            }
            curr = next;
        }
        // for(int i=0; i<len; i++){
        //     if(i+nums[i] > maxdist){
        //         maxdist = i+nums[i];
        //         ans++;
        //     }
        //     if(maxdist >= len-1) break;
        // }
        return ans;
    }
}