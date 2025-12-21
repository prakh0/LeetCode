class Solution {
    public int maxDistance(String s, int k) {
        int result = 0;
        int north = 0, south = 0, east = 0, west = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == 'N') {
                north += 1;
            } else if (ch == 'S') {
                south += 1;
            } else if (ch == 'E') {
                east += 1;
            } else if (ch == 'W') {
                west += 1;
            }

            int x = Math.abs(north - south);
            int y = Math.abs(east - west);
            int manhattanDistance = x + y;
            int maxDistance = manhattanDistance + Math.min(2*k,i + 1 - manhattanDistance);
            result = Math.max(result,maxDistance);
        }
        return result; 
    }
}
