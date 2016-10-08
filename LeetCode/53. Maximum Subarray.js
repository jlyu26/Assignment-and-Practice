/**
 * @param {number[]} nums
 * @return {number}
 */

// - -
// + +
// - +
// + -
// - + - (- - / + -)
// + - + (- + / + +)

var maxSubArray = function(nums) {
    if(nums.length === 0)
    	return 0;
    var previous = Math.max(0, nums[0]),
    	max = nums[0]; 
    for(var i = 1; i < nums.length; i++){
        // previous是以nums[i]结尾的max subarray的大小
        // 在nums[i-1]的(previous < 0)的情况下：nums[i]的previous是nums[i]
        // 在nums[i-1]的(previous >= 0)的情况下：nums[i]的previous是previous + nums[i]
        previous = Math.max(previous + nums[i], nums[i]);  
    	// max是nums[i]的max subarray，要么是previous，要么是nums[i-1]的max
        max = Math.max(previous, max);
        console.log(previous, max);
    }
    return max;
};

function test(nums){
	console.log(maxSubArray(nums));
}


test([2, 3, -1, -9, 3, 4, -4, 0, 1]);