package org.example.study.week15.일요일아침의데이트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

/**
 * 6 6
 * ......
 * g..F..
 * ......
 * ..g...
 * ......
 * ...S.g
 *
 * 만약 되도록 적게 지나가는 경우의 수가 여러개라면, 쓰레기 옆을 지나가는 칸의 개수를 최소로 해서 지나려고 한다.
 * 만약 어떤 칸이 비어있는데, 인접한 칸에 쓰레기가 있으면 쓰레기 옆을 지나는 것이다. 그리고, S와 F는 세지 않는다.
 *
 * 비용, 쓰레기를 지나는 횟수 / 쓰레기 옆을 지나가는 칸의 갯수
 * 이 두개가 작은 애 먼저 이동시키기, 이미 이동하려는 칸에 저 두개 비용이 더 작은 애가 있으면 가지도 않는다
 *
 */

public class Main {
    static int N;
    static int M;
    static boolean[][] adjMap;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        int endX = -1;
        int endY = -1;
        int startX = -1;
        int startY = -1;
        map = new char[N][M];
        costMap = new Cost[N][M];

        adjMap = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                char c = line.charAt(j);
                if (c == 'F') {
                    endX = i;
                    endY = j;
                }
                if (c == 'S') {
                    startX = i;
                    startY = j;
                }
                map[i][j] = c;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = 0; k < 4; k++) {
                    int nX = i + dirX[k];
                    int nY = j + dirY[k];

                    if (!inRange(nX, nY)) continue;
                    if (map[nX][nY] == 'g') {
                        adjMap[i][j] = true;
                        break;
                    }
                }
            }
        }

        play(startX, startY, endX, endY);
    }

    static char[][] map;
    static Cost[][] costMap;
    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, -1, 1};
    static void play(int sX, int sY, int eX, int eY) {
        PriorityQueue<Cost> pq = new PriorityQueue<>();
        costMap[sX][sY] = new Cost(sX, sY, 0, 0);
        pq.add(costMap[sX][sY]);

        while (pq.size() > 0) {
            Cost c = pq.poll();
            if (costMap[c.x][c.y] == null || costMap[c.x][c.y].compareTo(c) < 0) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nX = c.x + dirX[i];
                int nY = c.y + dirY[i];

                if (!inRange(nX, nY)) continue;
                if (map[nX][nY] == 'F') {
                    System.out.println(c.pass + " " + c.adj);
                    return;
                }

                int nPass = c.pass;
                int nAdj = c.adj;

                if (map[nX][nY] == 'g') nPass++;
                else if (adjMap[nX][nY]) nAdj++;

                Cost nCost = new Cost(nX, nY, nPass, nAdj);

                if (costMap[nX][nY] == null || costMap[nX][nY].compareTo(nCost) > 0) {
                    costMap[nX][nY] = nCost;
                    pq.add(nCost);
                }
            }
        }
    }

    static boolean inRange(int x, int y) {
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= M) return false;
        return true;
    }

    static class Cost implements Comparable<Cost>{
        //pass > adj
        int x;
        int y;
        int pass;
        int adj;

        @Override
        public int compareTo(Cost c) {
            if (this.pass == c.pass) {
                return this.adj - c.adj;
            }
            return this.pass - c.pass;
        }

        Cost(int x, int y, int pass, int adj) {
            this.x = x;
            this.y = y;
            this.pass = pass;
            this.adj = adj;
        }
    }
}
