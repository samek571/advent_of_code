import copy
def subsets(nums):
    if len(nums)==0:
        return [[]]

    first = subsets(nums[:-1])
    final = copy.deepcopy(first[:])

    for element in first:
        element.append(nums[-1])
        final.append(element)

    return final
print(subsets([1,2,3,4,5]))
