package org.example.bfs.연구실;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 64 63 62 / 3 2 1 = 4만
 *
 * 2 3
 * 0 1 2 3,4,5 (0,0), (0,1), (0,2) (1,0), (1,1), (1,2)
 *
 * 3 2
 * 0, 1, 2, 3, 4, 5 (0,0) (0,1), (1,0), (1,1)
 *
 * 0 0 0 1 1 1
 * 0 1 2 0 1 2
 *
 * 2로 나눈 몫, 2로 나눈 나머지
 *
 */

public class Main {
    static List<Position> virusPos;
    static int safeZoneNums = 0;

    static int[] dirX = {1, -1, 0, 0};
    static int[] dirY = {0, 0, 1, -1};

    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        int[][] map = new int[N][M];

        virusPos = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
                if (map[i][j] == 2) {
                    virusPos.add(new Position(i, j));
                } else if (map[i][j] == 0) {
                    safeZoneNums++;
                }
            }
        }

        int answer = Integer.MIN_VALUE;
        int[][] newMap = copyMap(map);
        for (int i = 0; i < N*M; i++) {
            if (newMap[i/M][i%M] != 0) continue;
            newMap[i/M][i%M] = 1;
            for (int j = i+1; j < N*M; j++) {
                if (newMap[j/M][j%M] != 0) continue;
                newMap[j/M][j%M] = 1;
                for (int k = j+1; k < N*M; k++) {
                    if (newMap[k/M][k%M] != 0) continue;
                    newMap[k/M][k%M] = 1;
                    answer = Math.max(answer, safeZoneNums - bfs(newMap));
                    newMap[k/M][k%M] = 0;
                }
                newMap[j/M][j%M] = 0;
            }
            newMap[i/M][i%M] = 0;
        }
        System.out.println(answer - 3);
    }

    static int bfs(int[][] oldMap) {
        int[][] map = copyMap(oldMap);
        int cnt = 0;
        Queue<Position> q = new LinkedList<>(virusPos);

        while (q.size() > 0) {
            Position virus = q.poll();

            for (int i = 0; i < 4; i++) {
                int nX = virus.x + dirX[i];
                int nY = virus.y + dirY[i];

                if (checkRange(nX, nY)
                && map[nX][nY] == 0) {
                    map[nX][nY] = 2;
                    q.add(new Position(nX, nY));
                    cnt++;
                }
            }
        }

        return cnt;
    }

    static boolean checkRange(int x, int y) {
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= M) return false;
        return true;
    }

    static int[][] copyMap(int[][] oldMap) {
        int[][] newMap = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                newMap[i][j] = oldMap[i][j];
            }
        }

        return newMap;
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
