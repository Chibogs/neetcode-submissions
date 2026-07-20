class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Dictionary (HashMap)
        # Format:
        #   Key   = number we've already seen
        #   Value = index of that number
        #
        # Example:
        # nums = [3, 4, 5]
        #
        # After visiting:
        # 3 -> {3: 0}
        # 4 -> {3: 0, 4: 1}
        # 5 -> {3: 0, 4: 1, 5: 2}
        HashMap = {}

        # enumerate() gives us both:
        # i = current index
        # n = current number
        #
        # Example:
        # nums = [3,4,5]
        #
        # i = 0, n = 3
        # i = 1, n = 4
        # i = 2, n = 5
        for i, n in enumerate(nums):

            # Find the number that would pair with the
            # current number to reach the target.
            #
            # Example:
            # target = 7
            # current number = 4
            #
            # difference = 7 - 4 = 3
            #
            # Now we're asking:
            # "Have we already seen a 3?"
            difference = target - n

            # Check if the partner number already exists
            # in the HashMap.
            #
            # This checks KEYS, not values.
            #
            # Example:
            # HashMap = {3:0, 5:2}
            #
            # if 3 in HashMap -> True
            # if 4 in HashMap -> False
            if difference in HashMap:

                # HashMap[difference]
                #
                # means:
                # "Get the VALUE stored at this KEY."
                #
                # Example:
                # HashMap = {3:0, 5:2}
                #
                # HashMap[3] returns 0
                #
                # So we return:
                # [index_of_partner, current_index]
                return [HashMap[difference], i]

            # Store the current number and its index
            # for future iterations.
            #
            # Example:
            # i = 2
            # n = 5
            #
            # HashMap[5] = 2
            #
            # Dictionary becomes:
            # {3:0, 4:1, 5:2}
            HashMap[n] = i
        # No solution found
        return []
