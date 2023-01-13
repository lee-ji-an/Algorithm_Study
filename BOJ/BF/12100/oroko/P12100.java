package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P12100 {

    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int[][] map = new int[N][N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) map[i][j] = Integer.parseInt(st.nextToken());
        }

        int max = 0;
        for(int i = 0; i < 4; i++) max = Math.max(max, move(map,5, i));
        System.out.println(max);
    }

    static class Num {
        int num;
        boolean merged;
        Num(int num, boolean merged) {
            this.num = num;
            this.merged = merged;
        }
    }

    public static int move(int[][] origin, int r, int dir) {
        int[][] map = new int[N][N];
        for(int i = 0; i < N; i++) map[i] = Arrays.copyOf(origin[i], N);

        if(r == 0) {
            int max = 0;
            for(int i = 0; i < N; i++) max = Math.max(max, Arrays.stream(map[i]).max().getAsInt());
            return max;
        }

        Deque<Num> deq = new ArrayDeque<>();
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                switch (dir) {
                    case 0: makeDeq(map, j, i, deq); break;
                    case 1: makeDeq(map, i, N-j-1, deq); break;
                    case 2: makeDeq(map, N-j-1, i, deq); break;
                    case 3: makeDeq(map, i, j, deq);
                }
            }
            for(int j = 0; j < N; j++) {
                switch (dir) {
                    case 0: arrangeNums(map, j, i, deq); break;
                    case 1: arrangeNums(map, i, N-j-1, deq); break;
                    case 2: arrangeNums(map, N-j-1, i, deq); break;
                    case 3: arrangeNums(map, i, j, deq);
                }
            }
        }
        int max = 0;
        for(int i = 0; i < 4; i++) max = Math.max(max, move(map,r-1, i));
        return max;
    }

    public static void makeDeq(int[][] map, int i, int j, Deque<Num> deq) {
        if(map[i][j] == 0) return;
        if(deq.isEmpty()) deq.addLast(new Num(map[i][j], false));
        else {
            Num last = deq.getLast();
            if (last.num == map[i][j] && !last.merged) {
                deq.removeLast();
                deq.addLast(new Num(map[i][j] + map[i][j], true));
            }
            else deq.addLast(new Num(map[i][j], false));
        }
    }

    public static void arrangeNums(int[][] map, int i, int j, Deque<Num> deq) {
        if(!deq.isEmpty()) map[i][j] = deq.removeFirst().num;
        else map[i][j] = 0;
    }
}
