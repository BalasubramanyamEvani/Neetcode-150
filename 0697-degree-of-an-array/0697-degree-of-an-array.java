class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        Map<Integer, Integer> left = new HashMap<>();
        Map<Integer, Integer> right = new HashMap<>();
        int index = 0;
        int maxValue = Integer.MIN_VALUE;
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
            if (left.getOrDefault(num, null) == null) {
                left.put(num, index);
            }
            right.put(num, index);
            maxValue = Math.max(maxValue, counts.get(num));
            index += 1;
        }
        int minValue = nums.length;
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            int value = entry.getValue();
            int key = entry.getKey();
            if (value == maxValue) {
                int subArrayLength = right.get(key) - left.get(key) + 1;
                minValue = Math.min(minValue, subArrayLength);
            }
        }
        return minValue;
    }
}