

function getSecondLargest(nums) {
    let maxV = 0; let secMaxV = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > maxV) {
            maxV = nums[i];
        }
    }
    for (let j = 0; j < nums.length; j++) {
        if (nums[j] > secMaxV && nums[j] < maxV) {
            secMaxV = nums[j];
        }
    }
    return secMaxV
}
