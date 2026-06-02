class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let lo = 0
        let hi = nums.length
        console.log(hi)

        do {
            let mid = Math.floor((lo + hi) / 2)
            let guess = nums[mid]

            if (guess === target) {
                return mid
            } else if (guess > target) {
                console.log(hi)
                hi = mid - 1
                console.log(hi)
            } else {
                lo = mid + 1
            }
        } while (hi >= lo)

        return -1
    }
}
