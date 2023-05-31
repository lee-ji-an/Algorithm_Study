package org.example.study.week21.친구네트워크;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * 동적 유니온 파인드
 *
 * 해당 멤버가 네트워크에 없으면 새로운 번호 부여 -> 그 번호의 우두머리
 *
 * 1: a
 * 1: b
 * 3: c
 * 4: d
 *
 * a, b
 *
 *
 * 1 2 3 4
 *
 * 두 아이 병합, 그 번호의 우두머리가 아니면
 */

public class Main {
    static int cnt;
    static Map<Integer, String> id;
    static Map<String, Integer> group;
    static Map<Integer, Integer> size;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            id = new HashMap<>();
            group = new HashMap<>();
            size = new HashMap<>();
            cnt = 0;

            int R = Integer.parseInt(br.readLine());
            for (int k = 0; k < R; k++) {
                String[] temp = br.readLine().split(" ");
                String name1 = temp[0];
                String name2 = temp[1];

                System.out.println(union(name1, name2));
            }
        }
    }

    static int getGroup(String name) {
        int groupNum;
        if (!group.containsKey(name)) {
            groupNum = cnt++;
            group.put(name, groupNum);
            id.put(groupNum, name);
            size.put(groupNum, 1);
        } else {
            groupNum = find(name);
        }
        return groupNum;
    }

    static int find(String name) {
        int g = group.get(name);
        String owner = id.get(g);

        // 내 원래 id 랑 달라졌을 때
        if (owner.equals(name)) return g;
        int nId = find(owner);
        group.put(name, nId);
        return nId;
    }

    static int union(String name1, String name2) {
        int g1 = getGroup(name1);
        int g2 = getGroup(name2);

        if (g1 == g2) {
            return size.get(g1);
        }

        int total = size.get(g1) + size.get(g2);
        group.put(id.get(g2), g1);
        size.put(g1, total);
        size.put(g2, 0);
        return total;
    }
}
