package org.example.study.tree.가장가까운공통조상;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * 2
 * 16
 * 1 14
 * 8 5
 * 10 16
 * 5 9
 * 4 6
 * 8 4
 * 4 10
 * 1 13
 * 6 15
 * 10 11
 * 6 7
 * 10 2
 * 16 3
 * 8 1
 * 16 12
 * 16 7
 * 5
 * 2 3
 * 3 4
 * 3 1
 * 1 5
 * 3 5
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());

            List<Integer>[] conn = new List[N+1];
            boolean[] hasParent = new boolean[N+1];
            orient = new Node[N+1];
            for (int j = 0; j <= N; j++) {
                conn[j] = new ArrayList<>();
            }

            for (int j = 0; j < N-1; j++) {
                String[] temp = br.readLine().split(" ");
                int n1 = Integer.parseInt(temp[0]);
                int n2 = Integer.parseInt(temp[1]);

                hasParent[n2] = true;
                conn[n1].add(n2);
            }

            int root = -1;
            for (int j = 1; j <= N; j++) {
                if (!hasParent[j]) {
                    root = j;
                    break;
                }
            }

            String[] temp = br.readLine().split(" ");
            int n1 = Integer.parseInt(temp[0]);
            int n2 = Integer.parseInt(temp[1]);

            if (n1 == root || n2 == root) {
                System.out.println(root);
                continue;
            }

            if (n1 == n2) {
                System.out.println(n1);
                continue;
            }

            dfs(root, conn, 1);



            Node n1Orients = orient[n1];
            Node n2Orients = orient[n2];

            int ii = n1Orients.depth;
            int jj = n2Orients.depth;

            while (ii >= 1 && jj >= 1) {
                int n1Orient = n1Orients.parent;
                int n2Orient = n2Orients.parent;

                if (n1Orient == n2Orient) {
                    System.out.println(n1Orient);
                    break;
                }

                if (n1Orient == n2) {
                    System.out.println(n2);
                    break;
                }

                if (n2Orient == n1) {
                    System.out.println(n1);
                    break;
                }

                if (ii > jj) {
                    n1Orients = orient[n1Orients.parent];
                    ii--;
                    continue;
                }
                n2Orients = orient[n2Orients.parent];
                jj--;
            }
        }
    }

    static Node[] orient;
    static void dfs(int parent, List<Integer>[] conn, int depth) {
        for (int child : conn[parent]) {
            orient[child] = new Node(parent, depth);
            dfs(child, conn, depth+1);
        }
    }

    static class Node {
        int parent;
        int depth;

        public Node(int parent, int depth) {
            this.parent = parent;
            this.depth = depth;
        }
    }
}
























