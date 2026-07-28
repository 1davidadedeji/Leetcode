class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # i need to create a hashmap.. the key is each number in the lists while the value is a list of their position...
        bucket = {}
        duplicate = missing = None
        for i in range(1, len(nums)+1):
            # if i not in bucket.keys():
            bucket[i] = 0
            # else:
            #     bucket[i] += 1
        for i in nums:
            bucket[i] +=1
        for i in bucket:
            if bucket[i] == 2:
                duplicate = i
            elif bucket[i] == 0:
                missing = i
        output = [duplicate, missing]

        return output
        # pos = 0
        # output = []
        # for num in nums:

        #     if num not in bucket.keys():
        #         bucket[num] = num
        #         bucket[num].append(pos)
        #     else:
        #         bucket[num] = []
        #         bucket[num].append(pos)
        #     pos +=1
        # for m in bucket:
        #     if len(bucket[m]) == 1:
        #         del bucket[m]
        # for i in bucket.values:
        #     output.append(bucket.key)
        #     bucket.key += 1
        # return output
