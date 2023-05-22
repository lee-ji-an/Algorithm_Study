package org.example.study.week20.다이어트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * G킬로그램은 성원이의 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것이다.
 *
 *  15 = (cur+prev)(cur-prev)
 *
 *  소인수 분해
 *  15 1
 *  5 3
 *
 *  cur = 두 개 더한 수/2
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<Integer> answer = new ArrayList<>();
        for (int i = 1; i*i < N; i++) {
            if (N % i != 0) continue;
            int sum = i+(N/i);
            if (sum % 2 != 0) continue;
            answer.add(sum/2);
        }

        if (answer.size() == 0) {
            System.out.println(-1);
            return;
        }

        answer.sort(Comparator.naturalOrder());
        for (Integer integer : answer) {
            System.out.println(integer);
        }
    }
}
