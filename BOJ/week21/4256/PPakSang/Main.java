package org.example.study.week21.트리;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 다음 줄에는 BT를 전위 순회한 결과, 그 다음 줄에는 중위 순회한 결과가 주어진다.
 *
 * 전위: 나 - 좌 - 우
 * 중위: 좌 - 나 - 우
 * 후위: 좌 - 우 - 나
 *
 * 전위 순회하면 3,6,5,4,8,7,1,2, 중위 순회하면 5,6,8,4,3,1,2,7이 된다. 이를 이용해 후위 순회하면 5,8,4,6,2,1,7,3
 *
 * 5 6 8 4, 3, 1 2 7
 *            3
 *  6      1, 2, 7
 *5   4
 *  8
 *
 * 전위 순회 idx 기준으로 나누기 -> 나누기 함수 리턴값은 노드 헤더
 *
 * 2
 * 4
 * 3 2 1 4
 * 2 3 4 1
 * 8
 * 3 6 5 4 8 7 1 2
 * 5 6 8 4 3 1 2 7
 */

public class Main {
    static int idx;
    static int[] preorder;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int num = Integer.parseInt(br.readLine());
            idx = -1;

            preorder = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            List<Integer> collect = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt)
                    .collect(Collectors.toList());

            Node node = distribute(collect);
            print(node);
            System.out.println();
        }
    }

    static void print(Node node) {
        if (node == null) return;
        print(node.left);
        print(node.right);
        System.out.print(node.num + " ");
    }

    static Node distribute(List<Integer> nodes) {
        if (nodes.size() == 0) return null;
        idx++;
        int cur = preorder[idx];
        Node node = new Node(cur);

        int k = 0;
        for (int i = 0; i < nodes.size(); i++) {
            if (nodes.get(i) == cur) {
                k = i;
                break;
            }
        }

        node.left = distribute(nodes.subList(0, k));
        if (k+1 < nodes.size()) {
            node.right = distribute(nodes.subList(k+1, nodes.size()));
        }
        return node;
    }

    static class Node {
        int num;
        Node left;
        Node right;

        Node(int num) {
            this.num = num;
        }
    }
}
