class Solution {
    public boolean hasDuplicate(int[] nums) {

        // Using HashMap
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }

            seen.add(num);
        }
        return false;
    }
}