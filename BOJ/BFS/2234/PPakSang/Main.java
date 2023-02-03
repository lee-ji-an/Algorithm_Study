package org.example.bfs.성곽;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

/**
 * 이 성에 있는 방의 개수
 * 가장 넓은 방의 넓이
 * 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
 *
 *
 * 각 공간 별 너비 (공간 번호, 너비)
 * 벽 찾으면 그 뒤에 공간 너비 합 -> 공간 번호 겹치면 패스
 *
 * 7 4
 * 11 6 11 6 3 10 6
 * 7 9 6 13 5 15 5
 * 1 10 12 7 13 7 5
 * 13 11 10 8 10 12 13
 *
 * 서 북 동 남
 * 1 2 4 8
 */

public class Main {
    static int[] dirX = new int[] {0, 1, 0, -1};
    static int[] dirY = new int[] {-1, 0, 1, 0};

    static boolean[][][] map;
    static int[][] visited;

    static int N;
    static int M;

    static Map<Integer, Integer> spaceSize = new HashMap<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        map = new boolean[M][N][4];
        visited = new int[M][N];

        for (int i = M-1; i >= 0; i--) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                int num = Integer.parseInt(temp[j]);
                for (int k = 0; k < 4; k++) {
                    if ((num & 1<<k) > 0) map[i][j][k] = true;
                }
            }
        }

        int spaceNum = 0;
        int maxSize = Integer.MIN_VALUE;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] == 0) {
                    int thisSize = bfs(i, j, ++spaceNum);
                    maxSize = Math.max(maxSize, thisSize);
                    spaceSize.put(spaceNum, thisSize);
                }
            }
        }

        int maxMergeSize = Integer.MIN_VALUE;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    int nX = i + dirX[k];
                    int nY = j + dirY[k];

                    if (map[i][j][k] && checkRange(nX, nY)) {
                        if (visited[i][j] == visited[nX][nY]) maxMergeSize = Math.max(maxMergeSize, spaceSize.get(visited[i][j]));
                        else maxMergeSize = Math.max(maxMergeSize, spaceSize.get(visited[i][j]) + spaceSize.get(visited[nX][nY]));
                    }
                }
            }
        }

        System.out.println(spaceNum);
        System.out.println(maxSize);
        System.out.println(maxMergeSize);
    }

    static int bfs(int sX, int sY, int s) {
        int result = 1;
        visited[sX][sY] = s;

        Queue<Position> q = new LinkedList<>();
        q.add(new Position(sX, sY));
        while (q.size() > 0) {
            Position cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                if (!map[cur.x][cur.y][i] && visited[nX][nY] == 0) {
                    result++;
                    visited[nX][nY] = s;
                    q.add(new Position(nX, nY));
                }
            }
        }
        return result;
    }

    static boolean checkRange(int x, int y) {
        if (x < 0 || x >= M) return false;
        if (y < 0 || y >= N) return false;
        return true;
    }

    static class Position {
        int x;
        int y;

        Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
