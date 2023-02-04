package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P11048 {

    static int N, M;
    static int[][] map;
    static int[][] dist;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        dist = new int[N][M];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) map[i][j] = Integer.parseInt(st.nextToken());
            Arrays.fill(dist[i], -1);
        }
        System.out.println(candy(N-1, M-1));
    }

    static int[] dr = {-1, 0, -1};
    static int[] dc = {0, -1, -1};
    public static int candy(int i, int j) {
        if(i == 0 && j == 0) return map[0][0];
        if(dist[i][j] == -1) {
            dist[i][j] = 0;
            for (int k = 0; k < 3; k++) {
                int ni = i + dr[k];
                int nj = j + dc[k];
                if (0 <= ni && ni < N && 0 <= nj && nj < M) {
                    dist[i][j] = Math.max(dist[i][j], map[i][j] + candy(ni, nj));
                }
            }
        }
        return dist[i][j];
    }
}
