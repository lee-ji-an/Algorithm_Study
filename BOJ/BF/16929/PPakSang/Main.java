package org.example.Graph.TwoDots;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 50 * 50 = 2500
 * 2500 * 2500 (한 점 잡고 모두 도는 것을 모든 점에 대해서 반복)
 * 6250000
 * YYYR
 * BYBY
 * BBBY
 * BBBY
 *
 * 기존 탐색 위치 제외하고 삼방탐색 -> visited 있으면 사이클 존재
 * 다음 탐색 시작 점은 visited 가 아닌 곳부터
 */

public class Main {
    static int[] dirX = {1, 0, -1, 0};
    static int[] dirY = {0, 1, 0, -1};

    static char[][] map;
    static boolean[][] visited;

    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        map = new char[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j]) {
                    visited[i][j] = true;
                    if (calc(i, j, i, j)) {
                        System.out.println("Yes");
                        return;
                    };
                }
            }
        }

        System.out.println("No");
    }

    static boolean calc(int prevX, int prevY, int curX, int curY) {
        for (int i = 0; i < 4; i++) {
            int nX = curX + dirX[i];
            int nY = curY + dirY[i];

            if (checkRange(nX, nY)
                    && (prevX != nX || prevY != nY)
                    && map[curX][curY] == map[nX][nY]) {

                if (visited[nX][nY]) return true;
                visited[nX][nY] = true;
                if(calc(curX, curY, nX, nY)) return true;
            }
        }

        return false;
    }

    static boolean checkRange(int x, int y) {
        if (x >= N || x < 0) return false;
        if (y >= M || y < 0) return false;
        return true;
    }
}
