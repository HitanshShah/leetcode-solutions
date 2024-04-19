class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0;
        int len = prices.length;
        if(len == 1) return ans;
        int ptr = 0;
        for(int i=1; i<len; i++){
            if(prices[ptr] > prices[i]){
                ptr = i;
            }else{
                ans += prices[i] - prices[ptr];
                ptr = i;
            }
            System.out.println(ptr + " " + i + " " + ans);
        }
        return ans;
    }
}