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
        int length = convertedNum.length();
        int i = 0;
        int j = 0;
        StringBuilder sb = new StringBuilder();
        while (i < length) {
            sb.append(convertedNum.charAt(j));
            if (++j < length && convertedNum.charAt(j) != '0') {
                continue;
            }
            if (isPrime(Long.parseLong(sb.toString()))) {
                answer++;
            }
            while (j < length && convertedNum.charAt(j) == '0') {
                j++;
            }
            i = j;
            sb = new StringBuilder();
        }
        
        return answer;
    }
}
