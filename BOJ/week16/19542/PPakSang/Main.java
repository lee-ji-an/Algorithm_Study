package org.example.study.week16.전단지돌리기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * 각 노드 별 자식의 깊이 확인
 * 깊이가 D 보다 크면 가고
 * 각각 탐색 거리 다 합하고 + 2(현재 노드까지 오는 경로) 해서 반환
 */

public class Main {
    static List<Integer>[] conn;
    static int D;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        int S = Integer.parseInt(temp[1]);
        D = Integer.parseInt(temp[2]);

        conn = new List[N+1];
        for (int i = 0; i <= N; i++) {
            conn[i] = new ArrayList<>();
        }

        for (int i = 0; i < N-1; i++) {
            temp = br.readLine().split(" ");
            int x = Integer.parseInt(temp[0]);
            int y = Integer.parseInt(temp[1]);

            conn[x].add(y);
            conn[y].add(x);
        }

        search(-1, S, 0);
        System.out.println(answer > 0 ? answer - 2 : answer);
    }

    static int answer = 0;
    static Result search(int prev, int cur, int depth) {
        boolean visit = D == 0;
        Result res = new Result(depth, false);

        for (int next : conn[cur]) {
            if (next == prev) continue;
            Result temp = search(cur, next, depth+1);

            if (temp.visit || temp.maxD - depth == D) {
                visit = true;
            }

            if (res.maxD < temp.maxD) {
                res = temp;
            }
        }

        if (visit) {
            answer += 2;
            res.visit = visit;
        }
        return res;
    }

    static class Result {
        int maxD;
        boolean visit;

        Result(int maxD, boolean visit) {
            this.maxD = maxD;
            this.visit = visit;
        }
    }

    static class Node {
        int num;
        int depth;
        int leafDepth;

        Node(int num, int depth, int leafDepth) {
            this.num = num;
            this.depth = depth;
            this.leafDepth = leafDepth;
        }
    }
}
