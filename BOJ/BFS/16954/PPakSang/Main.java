package org.example.bfs.움직이는미로탈출;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

/**
 * 이동 횟수(라운드) - 벽 위치 List
 * 내가 이동 했을 때 벽이 내려와서 갇히면 끝
 *
 * Map 최대 크기 64, 64 -> 8*2개(높이, 최악의 경우 벽이 다 사라지고 가장 아래에 있음) 다 저장해도 메모리는 신경X
 */


public class Main {
    static Map<Integer, char[][]> map = new HashMap<>();
    static int[] dirX = new int[]{1, -1, 0, 0, 1, 1, -1, -1, 0};
    static int[] dirY = new int[]{0, 0, 1, -1, -1, 1, 1, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[][] temp = new char[8][8];
        for (int i = 7; i >= 0; i--) {
            String line = br.readLine();
            for (int j = 0; j < 8; j++) {
                temp[i][j] = line.charAt(j);
            }
        }
        map.put(0, temp);
        System.out.println(bfs (0, 0));
    }

    static int bfs(int sX, int sY) {

        Queue<Position> q = new LinkedList<>();
        q.add(new Position(sX, sY, 0));

        while (q.size() > 0) {
            Position cur = q.poll();
            char[][] curMap = map.get(cur.cnt);
            char[][] nextMap;

            if (!map.containsKey(cur.cnt+1)) {
                 nextMap = new char[8][8];
                for (int y =0; y < 8; y++) {
                    for (int x = 1; x < 8; x++) {
                        nextMap[x-1][y] = curMap[x][y];
                    }
                }
                map.put(cur.cnt+1, nextMap);
            } nextMap = map.get(cur.cnt+1);


            for (int i = 0; i < 9; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                if (checkRange(nX, nY) && curMap[nX][nY] != '#') {
                    if (nX == 7 && nY == 7) return 1;
                    if (nextMap[nX][nY] == '#') continue;
                    q.add(new Position(nX, nY, cur.cnt + 1));
                }
            }

        }
        return 0;
    }
    static boolean checkRange(int x, int y) {
        if (x >= 8 || x < 0) return false;
        if (y >= 8 || y < 0) return false;
        return true;
    }

    static class Position {
        int x;
        int y;
        int cnt;

        Position (int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}
