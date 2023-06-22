package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P21925 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for(int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());

        boolean[][] palindrome = new boolean[N][N];
        for(int i = 0; i < N-1; i++) {
            if(arr[i] == arr[i+1]) palindrome[i][i+1] = true;
        }

        for(int i = 0; i < N-1; i++) {
            if(!palindrome[i][i+1]) continue;
            for(int gap = 1; gap < N/2; gap++) {
                int left = i - gap;
                int right = i + 1 + gap;

                if(left < 0 || right >= N) break;

                if(arr[left] == arr[right]) palindrome[left][right] = true;
                else break;
            }
        }

        System.out.println(count(palindrome, 0, N) ? cnt : -1);
    }

    static int cnt = 0;
    static boolean count(boolean[][] palindrome, int idx, int N) {
        if(idx == N) return true;

        for(int next = idx+1; next < N; next++) {
            if(palindrome[idx][next]) {
                if(count(palindrome, next+1, N)) {
                    cnt++;
                    return true;
                }
            }
        }
        return false;
    }
}
