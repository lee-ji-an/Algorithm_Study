import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P17404 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] weight = new int[N][3];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 3; j++) weight[i][j] = Integer.parseInt(st.nextToken());
        }

        int answer = Integer.MAX_VALUE;
        int[][] dp = new int[N][3];
        for(int j = 0; j < 3; j++) dp[0][j] = weight[0][j];

        for(int i = 0; i < 3; i++) {    // 첫번째를 i로 고정 - 두번째와 마지막은 i를 뽑지마시오

            // 1열 뽑기
            dp[1][i] = Integer.MAX_VALUE;
            for(int j = 0; j < 3; j++) {
                if(i == j) continue;
                dp[1][j] = weight[0][i] + weight[1][j];
            }

            // 2열 ~ N-2열 뽑기
            for(int j = 2; j < N-1; j++) {
                dp[j][0] = weight[j][0] + Math.min(dp[j-1][1], dp[j-1][2]);
                dp[j][1] = weight[j][1] + Math.min(dp[j-1][0], dp[j-1][2]);
                dp[j][2] = weight[j][2] + Math.min(dp[j-1][1], dp[j-1][0]);
            }

            dp[N-1][i] = Integer.MAX_VALUE;
            // N-1열 뽑기
            for(int j = 0; j < 3; j++) {
                if(j == i) continue;
                dp[N-1][j] = Integer.MAX_VALUE;
                for(int k = 0; k < 3; k++) {
                    if(k == j) continue;
                    dp[N-1][j] = Math.min(dp[N-1][j], dp[N-2][k]);
                }
                dp[N-1][j] += weight[N-1][j];
            }

            answer = Math.min(
                    Math.min(answer, dp[N-1][0]),
                    Math.min(dp[N-1][1], dp[N-1][2]));
        }

        System.out.println(answer);
    }
}
