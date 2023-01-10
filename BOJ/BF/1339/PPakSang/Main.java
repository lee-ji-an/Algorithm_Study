package org.example.단어수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * 알파벳 당 숫자 1개
 * 알파벳 패턴의 합이 최대가 되는 알파벳 쌍
 * 자릿수가 높은 알파벳부터 큰 숫자 주기
 * 숫자 수가 10개 이하라서 어차피 낮은 자리의 숫자가 역전할 일은 없다
 * 같은 자리의 알파벳이 여러개라면? 순열
 */

public class Main {
    static Map<Character, Integer> score = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            calcScore(s);
        }

        List<Integer> scores = new ArrayList<>();
        Set<Character> keys = score.keySet();
        for (Character key : keys) {
            scores.add(score.get(key));
        }
        scores.sort(Comparator.reverseOrder());

        int result = 0;
        int idx = 0;
        for (int i = 9; i > 9-scores.size(); i--) {
            result += scores.get(idx++)*i;
        }

        System.out.println(result);
    }

    static void calcScore(String s) {
        int strlen = s.length();

        for (int i = 0; i < strlen; i++) {
            char c = s.charAt(i);
            score.put(c, score.getOrDefault(c, 0) + (int)Math.pow(10, strlen-i-1));
        }
    }
}
