nums = [55, 44, 33, 22, 11]

if not all([i > 5 for i in nums]):
    print("All larger then 5")
if any([i % 2 == 0 for i in nums]):
    print("At least one is even")
for v in enumerate(nums):
    print(v)

list1 = [True, True, False, True]
list2 = [True, True, True, True]
list3 = [False, False, False, False]
print(all(list1))
print(all(list2))
print(all(list3))
print(any(list1))
print(any(list2))
print(any(list3))
print()
nums1 = [2, 4, 6, 7, 8]
nums2 = [2, 4, 6, 8, 10]
nums3 = [1, 3, 5, 7, 9]
nums4 = [1, 2, 3, 5, 7]
print("All:")
print(nums1, all(i % 2 == 0 for i in nums1))
print(nums2, all(i % 2 == 0 for i in nums2))
print(nums3, all(i % 2 == 0 for i in nums3))
print(nums4, all(i % 2 == 0 for i in nums4))
print("\nAny:")
print(nums1, any(i % 2 == 0 for i in nums1))
print(nums2, any(i % 2 == 0 for i in nums2))
print(nums3, any(i % 2 == 0 for i in nums3))
print(nums4, any(i % 2 == 0 for i in nums4))

a = 10 != 10
b = 10 == 10
c = 10 < 10
d = 10 > 10
list_abcd = [a, b, c, d]
print(list_abcd)
n = all(list_abcd)
m = any(list_abcd)
print(n, m)
