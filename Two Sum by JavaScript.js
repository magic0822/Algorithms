Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution:

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
        var res =[];
        var numsLen = nums.length;
        for (var i = 0; i < numsLen; i++) {
            for (var j = i+1; j < numsLen; j++) {
                if (nums[i] + nums[j] == target) {
                    res = [i, j];
                    return res;
                }
            }
        }
    };
