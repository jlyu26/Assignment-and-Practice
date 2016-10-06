function majority(nums) {
    var n = nums.length;
    var element = nums[0];
    var element_1 = nums[0];
    var counter = 0;
    var counter_1 = 0;
    var gap_counter = 0;
    var gap_counter_1 = 0;

    for (i = 0; i < n; i++) {
        if (element === nums[i]) {
            gap_counter++;
        } else if (element_1 === nums[i]) {
            gap_counter_1++;
        } else if (gap_counter === 0) {
            gap_counter++;
            element = nums[i];
        } else if (gap_counter_1 === 0) {
            gap_counter_1++;
            element_1 = nums[i];
        } else {
            gap_counter--;
            gap_counter_1--;
        }
    }

    nums.forEach(function (num) {
        if (num === element) {
            counter++;
        } else if (num === element_1) {
            counter_1++;
        }
    });

    if ((counter > n / 3) && (counter_1 > n / 3)) {
        return [element, element_1];
    } else if (counter > n / 3) {
        return [element];
    } else if (counter_1 > n / 3) {
        return [element_1];
    } else {
        return [];
    }

}

function test(nums) {
    console.log('for', nums, 'result', majority(nums));
}

test([5, 1, 3, 3, 2, 2, 1, 5, 3]);