import java.io.*;

public class P15989 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());
            int[] dp = new int[n+1];
            dp[0] = 1;
            for(int i = 1; i <= 3; i++) {
                for(int j = 1; j <= n; j++) {
                    if (j - i >= 0) dp[j] += dp[j - i];
                }
            }
            bw.append(String.valueOf(dp[n])).append("\n");
        }
        bw.flush();
    }
}
