package org.example.study.week20.미로만들기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

/**
 * 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.
 *
 * 단, 검은 방을 하나도 흰방으로 바꾸지 않아도 되는 경우는 0이 답이다.
 *
 * 8
 * 11100110
 * 11010010
 * 10011010
 * 11101100
 * 01000111
 * 00110001
 * 11011000
 * 11000111
 *
 * 검은방 다익스트라
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        char[][] map = new char[N][N];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            map[i] = line.toCharArray();
        }

        int[] dirX = {1, -1, 0, 0};
        int[] dirY = {0, 0, 1, -1};

        PriorityQueue<Pos> pq = new PriorityQueue<>((p1, p2) -> p1.cnt - p2.cnt);

        int[][] visited = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(visited[i], Integer.MAX_VALUE);
        }
        visited[0][0] = 0;
        pq.add(new Pos(0, 0, 0));

        while (pq.size() > 0) {
            Pos cur = pq.poll();

            for (int i = 0; i < 4; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                if (nX < 0 || nX >= N || nY < 0 || nY >= N) continue;

                int nextCnt = cur.cnt;
                if (map[nX][nY] == '0') nextCnt++;
                if (nX == N-1 && nY == N-1) {
                    System.out.println(nextCnt);
                    return;
                }

                if (visited[nX][nY] <= nextCnt) continue;
                visited[nX][nY] = nextCnt;

                pq.add(new Pos(nextCnt, nX, nY));
            }
        }
    }

    static class Pos {
        int cnt;
        int x;
        int y;

        Pos(int cnt, int x, int y) {
            this.cnt = cnt;
            this.x = x;
            this.y = y;
        }
    }
}
