package org.example.study.week14.시간관리하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * 끝나는 시간이 빠른애 먼저?
 *
 * 3 5
 * 3 7
 *
 * 15
 * 14
 * 15
 * 14
 *
 * 최대한 늦게 끝내기
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<Schedule> schedules = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            int start = Integer.parseInt(temp[0]);
            int end = Integer.parseInt(temp[1]);

            schedules.add(new Schedule(start, end));
        }
        schedules.sort((s1, s2) -> s2.end - s1.end);

        int cur = Integer.MAX_VALUE;
        for (Schedule s : schedules) {
            if (cur < 0) break;

            if (cur >= s.end) {
                cur = s.end - s.start;
                continue;
            }

            cur -= s.start;
        }

        System.out.println(cur < 0 ? -1 : cur);
    }
    static class Schedule {
        int start;
        int end;

        public Schedule(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}
