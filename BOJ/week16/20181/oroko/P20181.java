import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P20181 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] weight = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) weight[i] = Integer.parseInt(st.nextToken());

        int i = 0, j = 1;
        int sum = weight[i];
        long[] dp = new long[N+1];  // dp[k]는 (k-1)번째 먹이까지 먹었을 때의 최대 에너지
        while(j <= N) {
            if(sum >= K) {
                while(sum >= K) {
                    dp[j] = Math.max(dp[j], dp[i] + sum - K);   // j-1번째 먹이까지 먹었을 때 누적 만족도가 최소 만족도를 넘어가면 최대 에너지 갱신

                    sum -= weight[i];
                    i++;
                }
            }
            else {
                dp[j] = Math.max(dp[j], dp[j-1]);   // 누적이 최소가 안되면 갱신 못함 = 이전까지 먹었을 때의 최대 에너지랑 비교해서 갱신
                if(j == N) break;

                sum += weight[j];
                j++;
            }
        }

        System.out.println(dp[N]);
    }
}
