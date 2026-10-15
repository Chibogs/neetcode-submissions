class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hash = new HashMap<>();

        for (int i=0; i < nums.length; i++){
            int n = nums[i];

            int difference = target - n;

            if(hash.containsKey(difference)){
                return new int[] {hash.get(difference), i};
            }
            
            hash.put(n, i);
        }
        return new int[]{};            
    }
}
