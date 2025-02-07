import java.util.*;

class Solution {
    public int solution(String[][] relation) {
        int r = relation.length;
        int c = relation[0].length;
        HashSet<Integer> candidate = new HashSet<>();    
        
        Top: for (int i = 1; i < Math.pow(2, c); i++) {
            for (int candi : candidate) {
                if ((i & candi) == candi) {
                    continue Top;
                }
            }
            
            ArrayList<Integer> keys = new ArrayList<>();
            
            for (int j = 0; j < c; j++) {
                if (((1 << j) & i) != 0) {
                    keys.add(j);
                }
            }
            
            HashSet<String> rows = new HashSet<>();
            
            for (int x = 0; x < r; x++) {
                StringBuilder sb = new StringBuilder();
                for (int key : keys) {
                    sb.append(relation[x][key]);
                }
                rows.add(sb.toString());
            }
            
            if (rows.size() == r) {
                candidate.add(i);
            }
        }
        
        return candidate.size();
    }
}
