import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P11058 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] dp = new long[N+1];    // i번 눌러서 출력할 수 있는 최대 A 개수
        /*
        추가 되는 개수
        * A) dp[i-1]에서 1개 추가
        * B) dp[i-3]을 버퍼에 넣어서 dp[i-3]에 (i-j-2)번 붙이기 */
        dp[0] = 0;
        for(int i = 1; i <= N; i++) {
            dp[i] = dp[i-1] + 1;
            for(int j = 2; j <= i-3; j++) {
                long buffer = dp[j];
                dp[i] = Math.max(dp[i],  buffer * (i-j-1));
            }
        }
        System.out.println(dp[N]);
    }
}
