class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }
        // Step 2: Declare the two HashMaps
        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> countT = new HashMap<>();

        // Step 3: Populate the frequency maps
        for (int i = 0; i < s.length(); i++) {
            char charS = s.charAt(i);
            char charT = t.charAt(i);

            countS.put(charS, 1 + countS.getOrDefault(charS, 0));
            countT.put(charT, 1 + countT.getOrDefault(charT, 0));
        }

        // Step 4: Compare maps (Java's .equals() checks if keys and values match)
        return countS.equals(countT);
    }
}
