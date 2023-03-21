package org.example.study.TwoPointer.합이0인네정수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 시간제한 12초
 * 4000 * 4000 (두 배열 숫자 조합) 16000 000
 * 16000 000 * 25 (대충 3억) * 2 (대충 6억) 통과 가능
 *
 *
 * 두 배열 쌍 숫자 조합으로 나오는 숫자를 투포인터
 *
 * 한 배열에서 숫자 하나 잡고, 그 숫자랑 가능한 조합 다 찾기
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        long[] a = new long[n];
        long[] b = new long[n];
        long[] c = new long[n];
        long[] d = new long[n];

        for (int i = 0; i < n; i++) {
            String[] temp = br.readLine().split(" ");
            a[i] = Long.parseLong(temp[0]);
            b[i] = Long.parseLong(temp[1]);
            c[i] = Long.parseLong(temp[2]);
            d[i] = Long.parseLong(temp[3]);
        }

        long[] nA = new long[n*n];
        long[] nB = new long[n*n];


        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                nA[idx] = a[i]+b[j];
                nB[idx] = c[i]+d[j];
                idx++;
            }
        }

        Arrays.sort(nA);
        Arrays.sort(nB);

        int left = 0;
        int right = nB.length-1;

        long answer = 0;
        while (left < n*n && right >= 0) {
            long res = nA[left] + nB[right];
            if (res == 0) {
                long prevL = nA[left];
                long prevR = nB[right];

                long lN = 0;
                long lR = 0;
                while (left < n*n) {
                    if (nA[left] == prevL) {
                        lN++;
                        left++;
                        continue;
                    }
                    break;
                }

                while (right >= 0) {
                    if (nB[right] == prevR) {
                        lR++;
                        right--;
                        continue;
                    }
                    break;
                }
                answer += lN * lR;
            } else if (res > 0) {
                right--;
            } else {
                left++;
            }
        }

        System.out.println(answer);
    }
}
