class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0;
        if(prices.length == 1) return ans;
        int p1 = 0, p2 = 1;
        while(p2<prices.length){
            if(prices[p1] >= prices[p2]){
                p1 = p2;
                p2++;
            }else{
                while(p2+1 < prices.length && prices[p2] < prices[p2+1]){
                    p2++;
                }
                ans += prices[p2] - prices[p1];
                p1=p2;
                p2++;
            }
            System.out.println(p2);
        }
        return ans;
    }
}