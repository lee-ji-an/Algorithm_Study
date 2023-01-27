package org.example.bfs.벽부수고이동하기3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * bfs, 이동 좌표에 마킹
 * 벽 부수고 이동한 것인가, 아닌가
 * 낮에는 부술 수 있고, 밤에는 못 부순다
 *
 * 각 이동마다 낮/밤, 부숨/안부숨, 카운트, 위치
 *
 * 가만히 있을 수 있다 -> 낮에는 부술 수 있으니 움직이는게 최선 / 밤은 한번 기다렸다가 부수는게 최선인 경우가 있을 수 있으니 다 고려
 *
 * 비용
 * 1. 덜 부수고 왔다
 * 2. 더 적은 거리를 왔다(BFS 로 해결)
 * 3. 낮/밤
 *
 * * 밤 crash:4 -> 낮 crash:4 는 (밤 crash:4) 보다 좋을 수 있다
 */

public class Main {

    static int[] dirX = {1, -1, 0, 0};
    static int[] dirY = {0, 0, 1, -1};

    static int N;
    static int M;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        K = Integer.parseInt(temp[2]);

        int[][] map = new int[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(Character.toString(line.charAt(j)));
            }
        }

        System.out.println(bfs(map));
    }

    static int bfs(int[][] map) {
        int[][] visited2 = new int[N][M];

        for (int i = 0; i < N*M; i++) {
            visited2[i/M][i%M] = 11;
        }

        Queue<Position> q = new LinkedList<>();
        q.add(new Position(0, 0, 1, 0, false));

        while (q.size() > 0) {
            Position cur = q.poll();

            boolean flag = false;
            for (int i = 0; i < 4; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                if (checkRange(nX, nY)) {
                    if (map[nX][nY] == 1) {
                        if (cur.crash == K) continue;
                        if (cur.time) {
                            if (visited2[nX][nY] > cur.crash+1) flag = true;
                            continue;
                        }
                        if (cur.crash+1 >= visited2[nX][nY]) continue;
                        visited2[nX][nY] = cur.crash+1;
                        q.add(new Position(nX, nY, cur.cnt+1, cur.crash+1, true));
                    } else {
                        if (nX == N-1 && nY == M-1) return cur.cnt+1;
                        if (cur.crash >= visited2[nX][nY] && !cur.time) continue;
                        if (cur.crash > visited2[nX][nY] && cur.time) continue;

                        visited2[nX][nY] = cur.crash;
                        q.add(new Position(nX, nY, cur.cnt+1, cur.crash, !cur.time));
                    }
                }
            }
            if (cur.time && flag) q.add(new Position(cur.x, cur.y, cur.cnt+1, cur.crash, false));
        }

        return (N == 1 && M == 1) ? 1 : -1;
    }

    static class Position {
        int x;
        int y;
        int cnt;
        int crash;
        boolean time;

        Position(int x, int y, int cnt, int crash, boolean time) {
            this.x = x;
            this.y = y;
            this.crash = crash;
            this.cnt = cnt;
            this.time = time;
        }
    }

    static boolean checkRange(int x, int y) {
        if (x >= N || x < 0) return false;
        if (y >= M || y < 0) return false;

        return true;
    }
}
