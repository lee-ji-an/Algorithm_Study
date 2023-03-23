package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1507 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] weight = new int[N][N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) weight[i][j] = Integer.parseInt(st.nextToken());
        }

        int sum = 0;
        for(int i = 0; i < N-1; i++) {
            for(int j = i+1; j < N; j++) {
                int min = weight[i][j];
                boolean isMin = true;
                for(int k = 0; k < N; k++) {
                    if(k == i || k == j) continue;
                    int temp = weight[i][k] + weight[j][k];
                    if(temp == min) {
                        isMin = false;
                        break;
                    }
                    if(temp < min) {
                        System.out.println(-1);
                        return;
                    }
                }
                if(isMin) sum += min;
            }
        }

        System.out.println(sum);
    }
}
