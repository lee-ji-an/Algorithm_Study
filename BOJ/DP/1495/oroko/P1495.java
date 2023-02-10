package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1495 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] gap = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++) gap[i] = Integer.parseInt(st.nextToken());
        boolean[][] volume = new boolean[N+1][M+1]; // i번째 볼륨까지 고려했고, 볼륨 j로 연주할 수 있는가
        volume[0][S] = true;
        for(int i = 1; i <= N; i++) {
            for(int j = 0; j <= M; j++) {
                if(volume[i-1][j]) {
                    if(j + gap[i] <= M) volume[i][j + gap[i]] = true;
                    if(j - gap[i] >= 0) volume[i][j - gap[i]] = true;
                }
            }
        }
        int max = -1;
        for(int i = 0; i <= M; i++) {
            if(volume[N][i]) max = i;
        }
        System.out.println(max);
    }
}
