package org.example.bfs.소수경로;

import java.beans.PropertyEditorSupport;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import javax.swing.text.Position;

/**
 * A -> B
 * A 의 각 자리 수를 바꿔서 B 를 만들어야 함
 * 각 시행마다 한 자리 수를 바꿈
 *
 * 한 자리 수를 바꾼 수 역시 소수에 포함돼야함
 *
 * 9999 까지의 소수만 남기고
 */

public class Main {
    static boolean[] primes = new boolean[10001];
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 2; i*i < 10000; i++) {
            if (primes[i]) continue;
            for (int j = i*i; j < 10000; j+=i) {
                primes[j] = true;
            }
        }

        for (int i = 0; i < T; i++) {
            String[] temp = br.readLine().split(" ");
            int from = Integer.parseInt(temp[0]);
            int to = Integer.parseInt(temp[1]);
            if (from == to) {
                System.out.println(0);
                continue;
            }
            int result = calc(from, to);
            System.out.println(result == -1 ? "Impossible" : result);
        }
    }

//    1033 1733 3733 3739 3779 8779 8179
    static int calc(int from, int to) {
        Queue<Integer> q = new LinkedList<>();
        q.add(from);
        visited = new boolean[10001];
        int result = 0;
        while (true) {
            int size = q.size();
            if (size == 0) break;


            while (size > 0){
                int num = q.poll();
                int temp = num;
                int num1 = calc2(num, temp%10, 1);
                temp /= 10;
                int num10 = calc2(num, temp%10, 10);
                temp /= 10;
                int num100 = calc2(num, temp%10, 100);
                temp /= 10;
                int num1000 = calc2(num, temp%10, 1000);

                for (int i = 1; i <= 9; i ++) {
                    int nextNum = num1000 + i*1000;
                    if (primes[nextNum] || visited[nextNum]) continue;
                    if (nextNum == to) return result+1;
                    visited[nextNum] = true;
                    q.add(nextNum);
                }

                if (getInteger(to, q, result, num100, 100) != null
                        || getInteger(to, q, result, num10, 10) != null
                        || getInteger(to, q, result, num1, 1) != null) return result+1;

                size--;
            }
            result++;
        }
        return -1;
    }

    private static Integer getInteger(int to, Queue<Integer> q, int result, int num, int digit) {
        for (int i = 0; i <= 9; i++) {
            int nextNum = num + i*digit;
            if (primes[nextNum] || visited[nextNum]) continue;;
            if (nextNum == to) return result;
            visited[nextNum] = true;
            q.add(nextNum);
        }
        return null;
    }

    static int calc2(int num, int digitNum, int digit) {
        return num - digitNum*digit;
    }


}
