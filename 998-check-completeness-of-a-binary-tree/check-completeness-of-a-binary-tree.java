/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        int counter = 0;
        while(!q.isEmpty()){
            // TreeNode curr = q.poll();
            // System.out.println(curr.val);
            // if(curr.left==null && curr.right==null){

            // }else{
            //     if(curr.left!=null) q.add(curr.left);
            //     else counter++;
            //     if(counter==0 && curr.right!=null) q.add(curr.right);
            //     else if(counter == 0 && curr.right==null) counter++;
            //     else return false;
            // }
            // if(counter>1) return false;
            TreeNode curr = q.poll();
            if(curr == null){
                counter++;
            }else{
                if(counter > 0) return false;
                q.add(curr.left);
                q.add(curr.right);
            }
        }
        return true;
    }
    // public boolean helper(TreeNode root){
    //     if(root.right != null && root.left == null) return false;
    //     if(root.left!=null){
    //         if(root.right!=null) return (helper(root.left) && helper(root.right));
    //         else return helper(root.left);
    //     }else{
    //         return true;
    //     }
    // }
}