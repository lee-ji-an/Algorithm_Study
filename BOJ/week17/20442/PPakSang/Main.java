package org.example.study.week17.크크루크크;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 *  k 를 만날때 까지 R 세기 + 기존 k 갯수
 *
 *  왼쪽 k 갯수 최대
 *  (k 갯수, 인덱스)
 *  오른쪽 k 갯수 최대
 *  (k 갯수, 인덱스)
 *  R 누적합
 *
 *  한 점에 대해 양 쪽 인덱스 얻고 i, j -> k 갯수 최솟값 + R[j] - R[i]
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        List<Integer> lK = new ArrayList<>();
        List<Integer> rK = new ArrayList<>();

        int cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'K') cnt++;
            else lK.add(cnt);
        }

        cnt = 0;
        for (int i = s.length()-1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == 'K') cnt++;
            else rK.add(cnt);
        }

        rK.sort(Comparator.reverseOrder());

        int left = 0;
        int right = rK.size()-1;


        int answer = 0;
        while (left <= right) {
            int lNum = lK.get(left);
            int rNum = rK.get(right);

            answer = Math.max(answer, right - left + 1 + 2*Math.min(rNum, lNum));
            if (lNum > rNum) {
                right--;
            } else {
                left++;
            }
        }

        System.out.println(answer);
    }
}
