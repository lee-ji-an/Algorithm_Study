package org.example.BF.두동전;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/*
동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.


동전끼리 만나거나 10번 이상이면 끝

 */

public class Main {
    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};

    static int N;
    static int M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        List<Position> coins = new ArrayList<>();
        boolean[][] map = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                if (line.charAt(j) == '#') map[i][j] = true;
                else if (line.charAt(j) == 'o') coins.add(new Position(i, j));
            }
        }
        int answer = play(map, coins.get(0), coins.get(1), 1);
        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }

    static int play(boolean[][] map, Position c1, Position c2, int cnt) {
        if ((c1.x == c2.x && c1.y == c2.y) || cnt == 11) return Integer.MAX_VALUE;

        int result = Integer.MAX_VALUE;
        for (int i = 0; i < 4; i++) {
            int nX1 = c1.x + dirX[i];
            int nY1 = c1.y + dirY[i];
            boolean flag1 = false;
            if (inRange(nX1, nY1)) {
                if (map[nX1][nY1]) {
                    nX1 = c1.x;
                    nY1 = c1.y;
                }
            } else {
                flag1 = true;
            }

            int nX2 = c2.x + dirX[i];
            int nY2 = c2.y + dirY[i];
            boolean flag2 = false;
            if (inRange(nX2, nY2)) {
                if (map[nX2][nY2]) {
                    nX2 = c2.x;
                    nY2 = c2.y;
                }
            } else {
                flag2 = true;
            }

            if (flag1 ^ flag2) return cnt;
            if (!flag1 && !flag2) {
                result = Math.min(result, play(map, new Position(nX1, nY1), new Position(nX2, nY2), cnt+1));
            }
        }
        return result;
    }

    static boolean inRange(int x, int y) {
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= M) return false;
        return true;
    }

    static class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
