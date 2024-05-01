class Solution {
    public boolean checkAlmostEquivalent(String word1, String word2) {
        int allowed = 3;
        Map<Character, Integer> mem1 = new HashMap<>();
        Map<Character, Integer> mem2 = new HashMap<>();

        for (char ch = 'a'; ch <= 'z'; ch += 1) {
            mem1.put(ch, mem1.getOrDefault(ch, 0));
            mem2.put(ch, mem2.getOrDefault(ch, 0));
        }
        for (char ch : word1.toCharArray()) {
            mem1.put(ch, mem1.get(ch) + 1);
        }
        for (char ch : word2.toCharArray()) {
            mem2.put(ch, mem2.get(ch) + 1);
        }
        for (Map.Entry<Character, Integer> entry : mem1.entrySet()) {
            char key = entry.getKey();
            int value1 = entry.getValue();
            int value2 = mem2.get(key);
            int diff = Math.abs(value1 - value2);
            if (diff > allowed) {
                return false;
            }
        }
        return true;
    }
}