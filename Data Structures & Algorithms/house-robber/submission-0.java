class Solution {
    public int rob(int[] nums) {     
        if (nums.length == 1) return nums[0];
        if (nums[1] < nums[0]) nums[1] = nums[0];
        if (nums.length == 2) return nums[1];
        
        for (int i = 2; i < nums.length; i++){
            if (nums[i] + nums[i-2] > nums[i-1]){
                nums[i] = nums[i] + nums[i-2];
            } else {
                nums[i] = nums[i-1]; // carries over
            }
        }
        return nums[nums.length-1];
    }
}
