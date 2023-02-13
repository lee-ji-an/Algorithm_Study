import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P2294 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < n; i++) set.add(Integer.parseInt(br.readLine()));
        int[] dp = new int[k+1]; // dp[i]는 i원을 만들기 위해 필요한 최소 갯수
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for(int coin : set) {
            for(int i = coin; i <= k; i ++) {
                if(i - coin >= 0 && dp[i - coin] < Integer.MAX_VALUE) dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        System.out.println(dp[k] == Integer.MAX_VALUE ? -1 : dp[k]);
    }

}
