function modifyArray(nums) {
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % 2 == 0) {
            nums[i] = nums[i] * 2;
        }
        else {
            nums[i] = nums[i] * 3;
        }
    }
    return nums
}
