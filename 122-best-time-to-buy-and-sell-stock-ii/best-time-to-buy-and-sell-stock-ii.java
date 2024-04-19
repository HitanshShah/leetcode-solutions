class Solution {
    public int maxProfit(int[] prices) {
        // int ans = 0;
        // int len = prices.length;
        // if(len == 1) return ans;
        // int p1 = 0, p2 = 1;
        // while(p2<len){
        //     if(prices[p1] >= prices[p2]){
        //         p1 = p2;
        //         p2++;
        //     }else{
        //         while(p2+1 < len && prices[p2] < prices[p2+1]){
        //             p2++;
        //         }
        //         ans += prices[p2] - prices[p1];
        //         p1=p2;
        //         p2++;
        //     }
        // }
        // return ans;

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
        }
        return ans;
    }
}