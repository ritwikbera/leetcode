nums = [2, 3, -2, 4]


def maxProduct(nums):
    max_product, min_product = 1, 1
    max_so_far = 1

    for i in range(len(nums)):
        n = nums[i]
        max_product = max(n, max_product*n, min_product*n)
        min_product = min(n, max_product*n, min_product*n)


        max_so_far = max(max_so_far, max_product)
    return max_so_far

print(maxProduct(nums))


