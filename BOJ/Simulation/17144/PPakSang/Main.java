package org.example.simulation.공기청정기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 미세먼지 확산
 * 현재 값 / 5
 * 4방
 *
 * ---
 *
 * 공기청정기 작동
 *
 *
 */

public class Main {
    static Cleaner[] cleaners;

    static int R;
    static int C;

    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        R = Integer.parseInt(temp[0]);
        C = Integer.parseInt(temp[1]);
        int T = Integer.parseInt(temp[2]);

        cleaners = new Cleaner[2];
        int[][] map = new int[R][C];

        int p = 0;
        for (int i = 0; i < R; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < C; j++) {
                int num = Integer.parseInt(temp[j]);
                if (num == -1) cleaners[p++] = new Cleaner(i, j);
                map[i][j] = num;
            }
        }

        int[] dirX1 = new int[]{0, -1, 0, 1};
        int[] dirY1 = new int[]{1, 0, -1, 0};

        int[] dirX2 = new int[]{0, 1, 0, -1};
        int[] dirY2 = new int[]{1, 0, -1, 0};

        for (int t = 0; t < T; t++) {
            map = spread(map);
            move(map, new int[][]{dirX1, dirY1}, cleaners[0].x, cleaners[0].y);
            move(map, new int[][]{dirX2, dirY2}, cleaners[1].x, cleaners[1].y);
        }

        int answer = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] > 0) answer += map[i][j];
            }
        }

        System.out.println(answer);
    }

    static void move(int[][] map, int[][] dirs, int sX, int sY) {
        int i = 0;
        int prev = map[sX][sY];
        while (i < 4) {
            int nX = sX + dirs[0][i];
            int nY = sY + dirs[1][i];

            if (!checkRange(nX, nY) || !onMoveLine(nX, nY) || isCleanerPosition(nX, nY)) {
                i++;
                continue;
            }
            sX = nX;
            sY = nY;
            int temp = map[nX][nY];
            map[nX][nY] = prev;
            prev = temp;
        }
    }

    static boolean isCleanerPosition(int nX, int nY) {
        if ((nX == cleaners[0].x && nY == cleaners[0].y) || (nX == cleaners[1].x && nY == cleaners[1].y)) return true;
        return false;
    }

    static int[][] spread(int[][] map) {
        int[][] result = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                int num = map[i][j];
                if (num > 0) {
                    int spreadNum = num/5;
                    int total = 0;
                    for (int idx = 0; idx < 4; idx++) {
                        int nX = i + dirX[idx];
                        int nY = j + dirY[idx];

                        if (checkRange(nX, nY) && !isCleanerPosition(nX, nY)) {
                            result[nX][nY] += spreadNum;
                            total += spreadNum;
                        }
                    }
                    result[i][j] += map[i][j] - total;
                }
            }
        }
        return result;
    }

    static boolean onMoveLine(int x, int y) {
        if (x == cleaners[0].x || x == cleaners[1].x) return true;
        if (y == 0 && (x <= cleaners[0].x || x >= cleaners[1].x)) return true;
        if (y == C-1 && (x <= cleaners[0].x || x >= cleaners[1].x)) return true;
        if (x == 0 || x == R-1) return true;

        return false;
    }

    static boolean checkRange(int x, int y) {
        if (x >= R || x < 0) return false;
        if (y >= C || y < 0) return false;
        return true;
    }

    static class Cleaner {
        int x;
        int y;

        public Cleaner(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
