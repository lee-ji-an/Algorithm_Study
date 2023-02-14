package org.example.DP.크리보드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 화면에 A를 출력한다.
 * Ctrl-A: 화면을 전체 선택한다 + Ctrl-C: 전체 선택한 내용을 버퍼에 복사한다
 * Ctrl-V: 버퍼가 비어있지 않은 경우에는 화면에 출력된 문자열의 바로 뒤에 버퍼의 내용을 붙여넣는다.
 *
 * 현재 갯수 A
 * 버퍼 B
 * 타이핑 1 -> A + 1
 * 선택, 복사, 붙임 3 -> A + (B+A)
 * (0, 0)
 * 1 (1, 0)
 * 2 (2, 0)
 * 3 (3, 0) 1
 * 4 (4, 0) (2, 2) 2
 * 5 (5, 0) (3, 3) 3
 * 6 (6, 3)
 * 7 (9, 3) (8, 4) (5, 5)
 * 8 (12, 4) (10, 5) (6, 6)
 * 9 (16, 4) (15, 5) (12, 6) (9, 9)
 * 10 (20, 4) (20, 5) (18, 9)
 * 11
 * 타이핑 vs 붙임 -> B > 0
 *
 *
 *
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        long[] sum = new long[101];
        for (int i = 1; i <= 6; i++) {
            sum[i] = i;
        }

        for (int i = 7; i <= n; i++) {
            sum[i] = Math.max(sum[i-3]*2, Math.max(sum[i-4]*3, sum[i-5]*(4)));
        }

        System.out.println(sum[n]);
    }
}
