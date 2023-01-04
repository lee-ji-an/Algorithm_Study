package org.example.스타트와링크;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1, 2, 3, 4... N 명
 * N/2 명씩 팀 결성
 * N/2 명 팀 결성되면 팀별 점수 합산
 * 팀 간 점수 차
 *
 * nC n/2
 *
 * 123, 124, 125, ...
 * 12, 13, 23
 */

public class Main {
    static Integer[][] score;
    static boolean[] team;
    static Integer answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        score = new Integer[N][N];
        team = new boolean[N];

        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");
            score[i] = Arrays.stream(temp).map(Integer::parseInt).toArray(Integer[]::new);
        }

        combination(N/2, 0, 0);

        System.out.println(answer);
    }

    static void combination(int maxCnt, int cnt, int cur) {
        if (cnt == maxCnt) {
            answer = Math.min(answer, calcScore());
            return;
        }

        for (int i = cur; i < maxCnt*2; i++) {
            team[i] = true;
            combination(maxCnt, cnt+1, i+1);
            team[i] = false;
        }
    }

    static Integer calcScore() {
        List<Integer> team1 = new ArrayList<>();
        List<Integer> team2 = new ArrayList<>();

        for (int i = 0; i < team.length; i++) {
            if (team[i]) {
                team1.add(i);
            } else {
                team2.add(i);
            }
        }

        return Math.abs(calcTeamScore(team1) - calcTeamScore(team2));
    }

    static Integer calcTeamScore(List<Integer> team) {
        int total = 0;

        for (int i = 0; i < team.size(); i++) {
            for (int j = i+1; j < team.size(); j++) {
                int p1 = team.get(i);
                int p2 = team.get(j);
                total += score[p1][p2] + score[p2][p1];
            }
        }
        return total;
    }
}
