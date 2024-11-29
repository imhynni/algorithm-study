import java.util.*;

class Solution {
    static boolean isPrime(long num) {
        if (num < 2)
            return false;
        for (long i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0)
                return false;
        }
        return true;
    }
    
    public int solution(int n, int k) {
        int answer = 0;
        String convertedNum = Integer.toString(n, k);
        long[] nums = Arrays.stream(convertedNum.split("0"))
                            .filter(s -> !s.isEmpty())
                            .mapToLong(Long::parseLong)
                            .toArray();
        
        for (long num : nums) {
            if (isPrime(num)) {
                answer++;
            }
        }
        
        return answer;
    }
}
