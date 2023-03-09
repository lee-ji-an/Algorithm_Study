package org.example.bfs_dfs.토마토3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static int[] dirX = new int[]{0, 0, 1, -1, 0, 0};
    static int[] dirY = new int[]{1, -1, 0, 0, 0, 0};
    static int[] dirZ = new int[]{0, 0, 0, 0, 1, -1};

    static int M;
    static int N;
    static int H;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        M = Integer.parseInt(temp[0]);
        N = Integer.parseInt(temp[1]);
        H = Integer.parseInt(temp[2]);

        int[][][] tomato = new int[H][N][M];

        int rawCnt = 0;
        Queue<Position> q = new LinkedList<>();
        for (int h = 0; h < H; h++) {
            for (int i = 0; i < N; i++) {
                temp = br.readLine().split(" ");
                for (int j = 0; j < M; j++) {
                    tomato[h][i][j] = Integer.parseInt(temp[j]);
                    if (tomato[h][i][j] == 1) {
                        q.add(new Position(h, i, j));
                    }
                    if (tomato[h][i][j] == 0) {
                        rawCnt++;
                    }
                }
            }
        }

        if (rawCnt == 0) {
            System.out.println(0);
            return;
        }

        int result = 0;
        while(true) {
            int size = q.size();
            if (size == 0 || rawCnt == 0) { break; }

            result++;
            for (int i = 0; i < size; i++) {
                Position cur = q.poll();

                for (int j = 0; j < 6; j++) {
                    int nZ = cur.z + dirZ[j];
                    int nX = cur.x + dirX[j];
                    int nY = cur.y + dirY[j];

                    if (!inRange(nZ, nX, nY) || tomato[nZ][nX][nY] != 0) {
                        continue;
                    }
                    tomato[nZ][nX][nY] = 1;
                    rawCnt--;
                    q.add(new Position(nZ, nX, nY));
                }
            }
        }

        if (rawCnt == 0) {
            System.out.println(result);
            return;
        }

        System.out.println(-1);
    }

    static boolean inRange(int z, int x, int y) {
        if (z < 0 || z >= H) return false;
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= M) return false;
        return true;
    }

    static class Position {
        int z;
        int x;
        int y;

        public Position(int z, int x, int y) {
            this.z = z;
            this.x = x;
            this.y = y;
        }
    }
}
