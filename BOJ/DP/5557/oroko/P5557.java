import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P5557 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());
        long[][] dp = new long[N][21];
        Set<Integer> set = new HashSet<>();
        set.add(arr[1]);
        dp[1][arr[1]] = 1;
        for(int i = 2; i < N; i++) {
            Set<Integer> temp = new HashSet<>();
            for(int num : set) {
                // 더해보기
                int sum = num + arr[i];
                if(0 <= sum && sum <= 20) {
                    temp.add(sum);
                    dp[i][sum] += dp[i-1][num];
                }

                // 빼보기
                int diff = num - arr[i];
                if(0 <= diff && diff <= 20) {
                    temp.add(diff);
                    dp[i][diff] += dp[i-1][num];
                }
            }
            set = temp;
        }
        System.out.println(dp[N-1][target]);
    }
}
