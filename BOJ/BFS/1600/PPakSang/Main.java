package org.example.bfs.말이되고픈원숭이;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 말 움직임으로 K 번, 말은 장애물도 뛰어넘을 수 있다. 8방
 * 그 외에는 동서남북 4빙
 *
 * 40000 * (8+4)
 *
 * 비용: 거리, 말 움직임 남은 횟수
 */

public class Main {

    static int[] horseX = new int[]{2, 2, 1, 1, -1, -1, -2, -2};
    static int[] horseY = new int[]{-1, 1, -2, 2, -2, 2, -1, 1};

    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};

    static int K;
    static int W;
    static int H;

    static int[][] visited;
    static boolean[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());

        String[] temp = br.readLine().split(" ");
        W = Integer.parseInt(temp[0]);
        H = Integer.parseInt(temp[1]);

        if (W == 1 && H == 1) {
            System.out.println(0);
            return;
        }

        visited = new int[H][W];
        map = new boolean[H][W];

        for (int i = 0; i < H; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < W; j++) {
                visited[i][j] = Integer.MAX_VALUE;
                if (temp[j].equals("1")) map[i][j] = true;
            }
        }

        System.out.println(bfs(0, 0));
    }

    static int bfs(int sX, int sY) {
        Queue<Position> q = new LinkedList<>();
        q.add(new Position(sX, sY, 0, 0));

        while (q.size() > 0) {
            Position cur = q.poll();

            if (cur.k != K) {
                for (int i = 0; i < 8; i++) {
                    int nX = cur.x + horseX[i];
                    int nY = cur.y + horseY[i];

                    if (rangeCheck(nX, nY) && !map[nX][nY]) {
                        if (nX == H-1 && nY == W-1) return cur.cnt + 1;
                        if (visited[nX][nY] > cur.k+1) {
                            visited[nX][nY] = cur.k+1;
                            q.add(new Position(nX, nY, cur.cnt+1, cur.k+1));
                        }
                    }
                }
            }

            for (int i = 0; i < 4; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                if (rangeCheck(nX, nY) && !map[nX][nY]) {
                    if (nX == H-1 && nY == W-1) return cur.cnt + 1;
                    if (visited[nX][nY] > cur.k) {
                        visited[nX][nY] = cur.k;
                        q.add(new Position(nX, nY, cur.cnt+1, cur.k));
                    }
                }
            }
        }

        return -1;
    }

    static class Position {
        int x;
        int y;
        int cnt;
        int k;

        Position (int x, int y, int cnt, int k) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.k = k;
        }
    }

    static boolean rangeCheck(int nX, int nY) {
        if (nX < 0 || nX >= H) return false;
        if (nY < 0 || nY >= W) return false;
        return true;
    }
}
