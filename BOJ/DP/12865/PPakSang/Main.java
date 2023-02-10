package org.example.DP.평범한배낭;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * N K
 * 4 7
 *
 * W V
 * 6 13
 * 4 8
 * 3 6
 * 5 12
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        int N = Integer.parseInt(temp[0]);
        int K = Integer.parseInt(temp[1]);

        int[][] visited = new int[N+1][K+1];
        Item[] items = new Item[N+1];

        for (int i = 1; i <= N; i++) {
            temp = br.readLine().split(" ");
            int w = Integer.parseInt(temp[0]);
            int v = Integer.parseInt(temp[1]);

            items[i] = new Item(w, v);
        }

        //가방 무게
        for (int i = 0; i <= K; i++) {
            // 물품 번호
            for (int j = 1; j <= N; j++) {
                Item cur = items[j];
                if (i-cur.w >= 0) visited[j][i] = Integer.max(visited[j-1][i-cur.w] + cur.v, visited[j-1][i]);
                else visited[j][i] = visited[j-1][i];
            }
        }

        System.out.println(visited[N][K]);
    }

    static class Item {
        int w;
        int v;

        public Item(int w, int v) {
            this.w = w;
            this.v = v;
        }
    }
}
