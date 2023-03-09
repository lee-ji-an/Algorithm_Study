package org.example.bfs_dfs.맥주마시면서걷기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표
 *
 * 0 0
 * 1000 0
 * 1000 1000
 * 2000 1000
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            Position[] positions = new Position[N+2];
            boolean[] visited = new boolean[N+2];

            String[] temp = br.readLine().split(" ");
            positions[0] = new Position(Integer.parseInt(temp[0]), Integer.parseInt(temp[1]));
            for (int j = 0; j < N; j++) {
                temp = br.readLine().split(" ");
                positions[1+j] = new Position(Integer.parseInt(temp[0]), Integer.parseInt(temp[1]));
            }
            temp = br.readLine().split(" ");
            positions[N+1] = new Position(Integer.parseInt(temp[0]), Integer.parseInt(temp[1]));

            Queue<Position> q = new LinkedList<>();
            q.add(new Position(positions[0].x, positions[0].y));

            boolean flag = false;
            while (q.size() > 0) {
                Position cur = q.poll();

                for (int i = 1; i < N+2; i++) {
                    if (visited[i]) continue;
                    int xDiff = Math.abs(cur.x - positions[i].x);
                    int yDiff = Math.abs(cur.y - positions[i].y);
                    if (xDiff + yDiff > 1000) continue;

                    if (i == N + 1) {
                        flag = true;
                        break;
                    }
                    visited[i] = true;
                    q.add(positions[i]);
                }

                if (flag) {
                    break;
                }
            }

            if (flag) {
                System.out.println("happy");
            } else {
                System.out.println("sad");
            }
        }
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
