package org.example.BF.NQueen;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *  1 0 0 0
 *  0 0 0 0
 *
 *
 *  n번째 놓을 때
 *  num[i] 는 num[1] ~ num[i-1] 와 같으면 안되고, num[i]-k, num[i]+k 와 같으면 안된다
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        System.out.println(play(N, 1, new int[N+1]));
    }

    static int play(int N, int cur, int[] num) {
        if (cur == N+1) {
            return 1;
        }

        int result = 0;
        for (int i = 1; i <= N; i++) {
            boolean flag = true;
            for (int j = 1; j <= cur-1; j++) {
                int prev = num[cur-j];
                if (prev == i || prev-j == i || prev+j == i) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                num[cur] = i;
                result += play(N, cur+1, num);
            }
        }
        return result;
    }
}
