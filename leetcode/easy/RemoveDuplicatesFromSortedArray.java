package leetcode.easy;

import java.util.Arrays;

/**
 * constraints
 * --
 * 1 <= nums.length <= 3 * 104
 * -100 <= nums[i] <= 100
 * nums is sorted in non-decreasing order.
 * 
 * base case(s)
 * --
 * if length(nums) == 1, return nums
 * 
 * pseudocode
 * --
 * num = nums[0]
 * current_index = 0
 * loop over indices of nums + 1:
 *  if nums[index] <= nums[current_index]:
 *      continue
 *  else:
 *      current_index++
 *      nums[current_index] = nums[index]
 *      
 *  
 */
public class RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 1) return 1;

        int current_index = 0;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[current_index]) {
                continue;
            } else {
                current_index++;
                nums[current_index] = nums[i];
            }
        }

        return current_index + 1;
    }

    public static void main(String[] args) {
        RemoveDuplicatesFromSortedArray removeDuplicatesFromSortedArray = new RemoveDuplicatesFromSortedArray();
        int[] nums = {-100,-91,-11,1,2,3,3,4,82};
        int res = removeDuplicatesFromSortedArray.removeDuplicates(nums);
        System.out.println(res);
        System.out.println(Arrays.toString(nums));
    }
}
