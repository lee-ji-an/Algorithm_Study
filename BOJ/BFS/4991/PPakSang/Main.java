package org.example.bfs.로봇청소기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

/**
 * 비용: 더러운 곳 남은 횟수, 거리
 * 어떤
 */

public class Main {
    static int[] dirX = new int[] {1, -1, 0, 0};
    static int[] dirY = new int[] {0, 0, 1, -1};

    static char[][] map;
    static Set<Integer>[][] visited;

    static int w;
    static int h;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String temp[] = br.readLine().split(" ");
            w = Integer.parseInt(temp[0]);
            h = Integer.parseInt(temp[1]);

            if (w == 0 && h == 0) return;
            if (w == 1 && h == 1) {
                System.out.println(0);
                continue;
            }
            map = new char[h][w];
            visited = new Set[h][w];

            int dirty = 0;
            int startX = -1;
            int startY = -1;
            for (int i = 0; i < h; i++) {
                String line = br.readLine();
                for (int j = 0; j < w; j++) {
                    visited[i][j] = new HashSet<>();
                    char c = line.charAt(j);
                    if (c == '*') {
                        map[i][j] = (char)dirty++;
                        continue;
                    }
                    if (c == 'o') {
                        startX = i;
                        startY = j;
                        map[i][j] = '.';
                        continue;
                    }
                    map[i][j] = c;
                }
            }

            if (dirty == 0) {
                System.out.println(0);
                continue;
            }

            System.out.println(bfs(startX, startY, dirty));
        }
    }

    static int bfs(int sX, int sY, int dirty) {
        Queue<Position> q = new LinkedList<>();
        q.add(new Position(sX, sY, 0, dirty, 0));
        visited[sX][sY].add(0);

        while (q.size() > 0) {
            Position cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nX = cur.x + dirX[i];
                int nY = cur.y + dirY[i];

                if (checkRange(nX, nY) && map[nX][nY] != 'x') {
                    if (map[nX][nY] == '.') {
                        if (!visited[nX][nY].contains(cur.visited)) {
                            visited[nX][nY].add(cur.visited);
                            q.add(new Position(nX, nY, cur.cnt+1, cur.dirty, cur.visited));
                        }
                    } else {
                        if (!visited[nX][nY].contains(cur.visited)) {
                            visited[nX][nY].add(cur.visited);
                            if ((cur.visited & 1 << (int)map[nX][nY]) == 0){
                                if (cur.dirty - 1 == 0) return cur.cnt+1;
                                q.add(new Position(nX, nY, cur.cnt+1, cur.dirty-1, cur.visited | 1 << (int)map[nX][nY]));
                            }
                            else if ((cur.visited & 1 << (int)map[nX][nY]) > 0)
                                q.add(new Position(nX, nY, cur.cnt+1, cur.dirty, cur.visited));
                        }
                    }
                }
            }
        }

        return -1;
    }

    private static boolean checkRange(int nX, int nY) {
        if (nX < 0 || nX >= h) return false;
        if (nY < 0 || nY >= w) return false;
        return true;
    }

    static class Position {
        int x;
        int y;
        int cnt;
        int dirty;
        int visited;

        public Position(int x, int y, int cnt, int dirty, int visited) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.dirty = dirty;
            this.visited = visited;
        }
    }
}
