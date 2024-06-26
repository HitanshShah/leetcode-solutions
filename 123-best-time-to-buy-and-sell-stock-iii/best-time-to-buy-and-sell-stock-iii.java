class Solution {
    public int maxProfit(int[] prices) {
        // ArrayList<Integer> ans = new ArrayList<Integer>();
        int len = prices.length;
        int buy1 = Integer.MAX_VALUE, buy2 = Integer.MAX_VALUE;
        int sell1 = Integer.MIN_VALUE, sell2 = Integer.MIN_VALUE;
        int ans = 0;
        if(len == 1) return 0;
        for(int i=0; i<len; i++){
            buy1 = Math.min(buy1, prices[i]);
            sell1 = Math.max(sell1, prices[i] - buy1);
            buy2 = Math.min(buy2, prices[i] - sell1);
            sell2 = Math.max(sell2, prices[i] - buy2);
        }
        return sell2;        
    }
}