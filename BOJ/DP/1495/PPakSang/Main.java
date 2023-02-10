package org.example.DP.기타리스트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * N
 * S
 * M
 *
 * 5 3 7
 *
 * 전 회차에서 만들 수 있는 모든 볼륨에 현재 경우 2가지(올린다, 내린다)로 볼륨 값 구하고 다음 회차 큐에 넣는다
 * 넣을 때 이미 넣은 케이스면 날리고
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        int N = Integer.parseInt(temp[0]);
        int S = Integer.parseInt(temp[1]);
        int M = Integer.parseInt(temp[2]);

        boolean[][] visited = new boolean[N][M+1];

        temp = br.readLine().split(" ");
        Queue<Integer> q = new LinkedList<>();

        q.add(S);
        for (int i = 0; i < N; i++) {
            int next = Integer.parseInt(temp[i]);
            int size = q.size();
            for (int j = 0; j < size; j++) {
                int prev = q.poll();
                if (prev+next <= M && !visited[i][prev+next]) {
                    visited[i][prev+next] = true;
                    q.add(prev+next);
                }
                if (prev-next >= 0 && !visited[i][prev-next]) {
                    visited[i][prev-next] = true;
                    q.add(prev-next);
                }
            }
        }

        for (int i = M; i >= 0; i--) {
            if (visited[N-1][i]) {
                System.out.println(i);
                return;
            }
        }
        System.out.println(-1);
    }
}
