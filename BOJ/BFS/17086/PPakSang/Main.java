package org.example.bfs.아기상어2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 아기 상어로부터 BFS -> 끝났을 때 값이 안전거리 최대값
 */

public class Main {
    static boolean[][] visited;

    static int[] dirX = new int[] {1, 1, 0, -1, -1, -1, 0, 1};
    static int[] dirY = new int[] {0, 1, 1, 1, 0, -1, -1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        int N = Integer.parseInt(temp[0]);
        int M = Integer.parseInt(temp[1]);
        visited = new boolean[N][M];

        Queue<Position> q = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                if (temp[j].equals("1")) {
                    visited[i][j] = true;
                    q.add(new Position(i, j));
                }
            }
        }

        int cnt = -1;
        while (q.size() > 0) {
            cnt++;
            int size = q.size();
            for (int c = 0; c < size; c++) {
                Position cur = q.poll();

                for (int i = 0; i < 8; i++) {
                    int nX = cur.x + dirX[i];
                    int nY = cur.y + dirY[i];

                    if (nX < 0 || nX >= N || nY < 0 || nY >= M) continue;
                    if (visited[nX][nY]) continue;
                    visited[nX][nY] = true;
                    q.add(new Position(nX, nY));
                }
            }
        }

        System.out.println(cnt);
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
