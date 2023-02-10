package org.example.DP.뮤탈리스크;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 9 3 1
 *
 *
 *54 18 6
 *
 * 3 6 9
 *
 *
 */

public class Main {

    static int N;
    static int[] selected;
    static int[] attack;

    static Queue<SCV> q;
    static boolean[][][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        attack = new int[]{9, 3, 1};
        visited = new boolean[61][61][61];

        selected = new int[N];

        q = new LinkedList<>();
        q.add(new SCV(temp));

        int result = 0;
        while (q.size() > 0) {
            result++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                SCV cur = q.poll();
                if (permutation(0, N, cur)) {
                    System.out.println(result);
                    return;
                }
            }
//            System.out.println();
        }
    }

    public static boolean permutation(int cur, int max, SCV scv) {
        if (cur == max) {
            int[] result = new int[3];
            for (int i = 0; i < N; i++) {
                int next = scv.abc[i] - attack[selected[i]];
                result[i] = Math.max(next, 0);
            }

            if (visited[result[0]][result[1]][result[2]]) return false;
            if (result[0] == 0 && result[1] == 0 & result[2] == 0) return true;
            visited[result[0]][result[1]][result[2]] = true;
            q.add(new SCV(new int[]{result[0], result[1], result[2]}));

//            System.out.println(String.format("(%d, %d, %d)", result[0], result[1], result[2]));
            return false;
        }

        for (int i = 0; i < N; i++) {
            if (selected[i] != 0) continue;
            selected[i] = cur;
            if (permutation(cur+1, max, scv)) return true;
            selected[i] = 0;
        }
        return false;
    }

    static class SCV{
        int[] abc;

        SCV (int[] abc) {
            this.abc = abc;
        }
    }
}
