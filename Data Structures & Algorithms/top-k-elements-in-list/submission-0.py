class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # dito i-sstore kung ilang times nag-appear each number
        frequency = [[] for i in range(len(nums) + 1)]  # mga bucket — index is the frequency, laman is mga number na ganun ka dalas or frequent

        #loop to count number of times nag-appear yung each number
        for num in nums:
            count[num] = 1 + count.get(num, 0) # get current count niya (0 kung wala pa), tapos +1 kasi nag-appear siya ulit

        # put each number sa tamang bucket base sa frequency niya
        # example: kung nums = [1,1,1,2,2,2,3], magiging count = {1: 3, 2: 3, 3: 1}
        for n, c in count.items():  # n is the number, c is number of times siya nag-appear
            frequency[c].append(n)
            # gamit natin .append() dahil posibleng maraming number ang may parehong frequency
            # trace natin yung example sa itaas:
            #   n=1, c=3 -> frequency[3].append(1) -> frequency[3] = [1]
            #   n=2, c=2 -> frequency[3].append(2) -> frequency[3] = [1,2]
            #   n=3, c=1 -> frequency[1].append(3) -> frequency[1] = [3]

        result = []  # dito ilalagay yung final answer (top k)

        # STEP 3: galing highest frequency papuntang lowest, kunin yung mga number
        for i in range(len(frequency) - 1, 0, -1):
            # start sa dulo (highest frequency) papunta sa 1
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:  # pag complete na yung k numbers, tapos na
                    return result