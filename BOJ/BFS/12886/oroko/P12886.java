package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P12886 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] stone = new int[3];
        for(int i = 0; i < 3; i++) stone[i] = Integer.parseInt(st.nextToken());
        System.out.println(bfs(stone));
    }

    public static int bfs(int[] stone) {
        Queue<Play> q = new LinkedList<>();
        q.add(new Play(stone[0], stone[1], stone[2]));
        Set<Play> set = new HashSet<>();
        set.add(new Play(stone[0], stone[1], stone[2]));
        while(!q.isEmpty()) {
            Play p = q.remove();
            if(p.success()) return 1;
            Play p1 = new Play(p.stone[0]+p.stone[0], p.stone[1]-p.stone[0], p.stone[2]);
            if(!set.contains(p1)) {
                q.add(p1);
                set.add(p1);
            }
            Play p2 = new Play(p.stone[0]+p.stone[0], p.stone[1], p.stone[2]-p.stone[0]);
            if(!set.contains(p2)) {
                q.add(p2);
                set.add(p2);
            }
            Play p3 = new Play(p.stone[0], p.stone[1]+p.stone[1], p.stone[2]-p.stone[1]);
            if(!set.contains(p3)) {
                q.add(p3);
                set.add(p3);
            }
        }
        return 0;
    }

    static class Play {
        int[] stone;
        Play(int a, int b, int c) {
            stone = new int[]{a,b,c};
            Arrays.sort(stone);
        }
        public boolean success() {
            return stone[0] == stone[1] && stone[1] == stone[2];
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Play play = (Play) o;
            return Arrays.equals(stone, play.stone);
        }

        @Override
        public int hashCode() {
            return Arrays.hashCode(stone);
        }
    }
}
