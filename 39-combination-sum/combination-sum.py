class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans_list = []
        curr_list = []
        self.helper(candidates, 0, target, curr_list, ans_list)
        return ans_list
        
    def helper(self, candidates, idx, target, curr_list, ans_list):
        if idx >= len(candidates):
            return
        if target<0:
            return
        if target == 0:
            ans = curr_list
            ans_list.append(list(curr_list))
            return
        curr_list.append(candidates[idx])
        self.helper(candidates, idx, target-candidates[idx], curr_list, ans_list)
        curr_list.pop()
        self.helper(candidates, idx+1, target, curr_list, ans_list)