package org.example.study.싸지방에간준하;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Stack;

/**
 * 모든 사람은 싸지방에 들어왔을 때 비어있는 자리 중에서 번호가 가장 작은 자리에 앉는 것이 규칙
 *
 * 5
 * 20 50
 * 10 100
 * 30 120
 * 60 110
 * 80 90
 *
 * 1
 * 2
 * 3
 *
 * 2
 * 3
 *
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<Schedule> schedules = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            int s = Integer.parseInt(temp[0]);
            int e = Integer.parseInt(temp[1]);

            schedules.add(new Schedule(s, e));
        }

        schedules.sort((s1, s2) -> s1.s - s2.s);
        int cMax = 1;
        PriorityQueue<Integer> computers = new PriorityQueue<>();
        Map<Integer, Integer> used = new HashMap<>();

        PriorityQueue<Reserve> pq = new PriorityQueue<>((r1, r2) -> r1.sc.e - r2.sc.e);
        for (Schedule sc : schedules) {
            if (pq.isEmpty()) {
                pq.add(new Reserve(sc, cMax));
                used.put(cMax, used.getOrDefault(cMax, 0)+1);
                cMax++;
                continue;
            }

            // 현재 스케줄의 시작 시간 보다 더 빨리 종료되는 컴퓨터들 다 회수
            while (!pq.isEmpty() && pq.peek().sc.e < sc.s) {
                Reserve r = pq.poll();
                computers.add(r.num);
            }

            // 남은 컴퓨터 없으면, 한대 더 주고
            if (computers.isEmpty()) {
                pq.add(new Reserve(sc, cMax));
                used.put(cMax, used.getOrDefault(cMax, 0)+1);
                cMax++;
                continue;
            }

            int com = computers.poll();
            used.put(com, used.get(com)+1);
            pq.add(new Reserve(sc, com));
        }

        System.out.println(cMax-1);
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < cMax; i++) {
            sb.append(used.get(i));
            sb.append(" ");
        }
        System.out.println(sb);
    }

    static class Reserve {
        Schedule sc;
        int num;

        public Reserve(Schedule sc, int num) {
            this.sc = sc;
            this.num = num;
        }
    }

    static class Schedule {
        int s;
        int e;

        public Schedule(int s, int e) {
            this.s = s;
            this.e = e;
        }
    }
}
