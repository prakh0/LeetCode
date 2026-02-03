class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums); 
        int index = nums.length - k;
        return nums[index];
    }
}