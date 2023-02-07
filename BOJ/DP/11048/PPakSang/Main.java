package org.example.DP.이동하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 대각선 이동은 우측, 위 이동으로 커버
 * 한 칸에 대해서 2 가지 방향으로 오는 경우 생각해야함 백만 * 2 = 2백만
 *
 *
 */

public class Main {

    static int N;
    static int M;

    static int[][] map;
    static int[][] visited;

    static int[] dirX = new int[] {1, 0};
    static int[] dirY = new int[] {0, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        map = new int[N][M];
        visited = new int[N][M];

        for (int i = 0; i < N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int max = 0;
                for (int k = 0; k < 2; k++) {
                    int nX = i - dirX[k];
                    int nY = j - dirY[k];
                    if (rangeCheck(nX, nY)) {
                        max = Math.max(max, map[nX][nY]);
                    }
                }
                map[i][j] += max;
            }
        }

        System.out.println(map[N-1][M-1]);
    }

//    static void bfs(int sX, int sY, int sCnt) {
//        Queue<Pos> q = new LinkedList<>();
//        q.add(new Pos(sX, sY, sCnt));
//
//        while (q.size()>0) {
//            Pos cur = q.poll();
//
//            for (int i = 0; i < 2; i++) {
//                int nX = cur.x + dirX[i];
//                int nY = cur.y + dirY[i];
//
//                if (rangeCheck(nX, nY) && visited[nX][nY] < cur.cnt + map[nX][nY]) {
//                    visited[nX][nY] = cur.cnt + map[nX][nY];
//                    System.out.println(visited[nX][nY]);
//                    q.add(new Pos(nX, nY, cur.cnt + map[nX][nY]));
//                }
//            }
//        }
//    }
    static boolean rangeCheck(int x, int y) {
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= M) return false;
        return true;
    }

    static class Pos {
        int x;
        int y;
        int cnt;

        Pos (int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}
