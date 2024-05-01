class Solution {
    public boolean winnerOfGame(String colors) {
        int numA = 0;
        int numB = 0;
        int colorsSize = colors.length();
        for (int i = 1; i < colorsSize - 1; ++i) {
            Character curr = colors.charAt(i);
            Character prev = colors.charAt(i - 1);
            Character next = colors.charAt(i + 1);
            if (curr == prev && curr == next) {
                if (curr == 'A') {
                    numA += 1;
                } else {
                    numB += 1;
                }
            }
        }
        return numA > numB;
    }
}