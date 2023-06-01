import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2616 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] passengers = new int[N];
        for(int i = 0; i < N; i++) passengers[i] = Integer.parseInt(st.nextToken());
        int limit = Integer.parseInt(br.readLine());

        int[][] dp = new int[3][N];
        int start = 0;
        dp[0][0] = passengers[0];
        int sum = dp[0][0];
        for(int i = 1; i < N; i++) {
            sum += passengers[i];
            dp[0][i] = Math.max(dp[0][i-1], sum);

            if(i - start == limit-1) {
                sum -= passengers[start++];
            }
        }

        for(int i = 1; i < 3; i++) {
            start = i-1;
            sum = passengers[i-1];

            for(int j = i; j < N; j++) {
                sum += passengers[j];

                dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1] + passengers[j]);
                if(j - limit >= 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j - limit] + sum);
                }

                if(j - start == limit-1) {
                    sum -= passengers[start++];
                }
            }
        }

        System.out.println(dp[2][N-1]);
    }
}
