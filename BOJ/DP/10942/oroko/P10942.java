package baekjoon.study;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P10942 {

    static int[] arr;
    static boolean[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N+1];
        dp = new boolean[N+1][N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            dp[i][i] = true;    // 길이가 1일 때 팰린드롬
            if(i > 1 && arr[i-1] == arr[i]) dp[i-1][i] = true;  // 길이가 2일 때 팰린드롬인지 확인
        }
        for(int k = 2; k < N; k++) {    // 길이가 k+1일 때 팰린드롬인지 확인
            for(int i = 1; i <= N-k; i++) {
                int j = i + k;
                if(dp[i+1][j-1] && arr[i] == arr[j]) dp[i][j] = true;   // (i+1, j-1)이 팰린드롬이고 arr[i] == arr[j]이면 (i, j)도 팰린드롬
            }
        }

        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            bw.append((dp[S][E] ? '1' : '0')).append('\n');
        }
        bw.flush();
    }

}
