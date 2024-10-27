class Sorting:
    # This question can be solved in many ways.
    # Here I have covered some basic linear sorting methods.

    # Bubble sort method
    def sortColors1(self, nums):
        flag = 0
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = 1
            if flag == 0:
                break

    # Selection sort method
    def sortColors2(self, nums):
        for i in range(len(nums)):
            smallest = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[smallest]:
                    smallest = j
            nums[smallest], nums[i] = nums[i], nums[smallest]

    # Insertion sort method
    def sortColors3(self, nums):
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i - 1
            while j >= 0 and temp < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp
