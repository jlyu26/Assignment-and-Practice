// 169. Majority Element
// Given an array of size n, find the majority element.
// The majority element is the element that appears more than n/2 times.
// You may assume that the array is non-empty and the majority element always exist in the array.
// Difficulty: Easy
// Tags: Array, Divide and Conquer, Bit Manipulation
//
// Boyer–Moore majority vote algorithm
// Key Point在于majority在array中最多只能有1个
// 所以通过把majority的出现次数和其他所有元素的出现次数总和作比较


function majority(nums) {
    var n = nums.length;
    var element = nums[0];                      // element记录temporary majority
    var counter = 0;                            // counter记录temporary majority出现的总次数
    var gap_counter = 0;                        // gap_counter记录temporary majority比其他元素多出现了几次

    nums.forEach(function (num) {               // 对于数组nums中的每个nums[n]
        if (gap_counter === 0) {                // 如果counter为0，即没有temporary majority
            element = num;
            gap_counter = 1;
        } else if (element == num) {            // 如果element跟temporary majority相同
            gap_counter += 1;
        } else {                                // 如果element跟temporary majority不同，就给temporary majority的领先量-1
            gap_counter -= 1;
        }
    });

    nums.forEach(function (num) {               // 对于已经找到的temporary majority，记录出现过的总次数
        if (num == element) {
            counter++;
        }
    });

    if (counter <= n / 2) {                     // 如果没有总出现次数超过半数的element
        return -1;
    }

    return element;
}

function test(nums) {
    console.log('for', nums, 'result', majority(nums));
}

test([2, 1, 3, 3, 2, 2, 2]);                    // for [ 2, 1, 3, 3, 2, 2, 2 ] result 2