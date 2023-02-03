package org.example.bfs.새로운하노이탑;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

/**
 *
 * B
 * C
 * A
 *
 * 이전에 옮긴 곳, 각 스틱 별 현재 갯수
 *
 */

public class Main {
    static int[] total = new int[3];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stick[] sticks = new Stick[3];

        for (int i = 0; i < 3; i++) {
            sticks[i] = new Stick(new ArrayList<>(), new int[3]);
            String[] temp = br.readLine().split(" ");
            int n = Integer.parseInt(temp[0]);
            for (int j = 0; j < n; j++) {
                int plate = temp[1].charAt(j) - 'A';
                total[plate]++;
                sticks[i].addPlate(plate);
            }
        }


        System.out.println(bfs(sticks));
    }

    static int bfs(Stick[] sticks) {
        Queue<Game> q = new LinkedList<>();
        q.add(new Game(0, 0, sticks));
        Set<String> set = new HashSet<>();

        while (q.size() > 0) {
            Game cur = q.poll();

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 3; i++) {
                sb.append(cur.sticks[i].hashCode());
            }

            if (set.contains(sb.toString())) continue;
            set.add(sb.toString());

            for (int i = 0; i < 3; i++) {
                if (cur.cnt != 0 && cur.prev == i) continue;
                if (cur.sticks[i].status.size() == 0) continue;

                for (int j = 1; j < 3; j++) {
                    Game game = Game.newGame(cur);
                    int n = (i+j)%3;

                    int plate = game.sticks[i].getLastPlate();
                    game.sticks[n].addPlate(plate);

                    if (game.sticks[0].abc[0] == total[0]
                    && game.sticks[1].abc[1] == total[1]
                    && game.sticks[2].abc[2] == total[2]) return cur.cnt + 1;

                    game.prev = n;
                    game.cnt++;

                    String hashValue = game.hash();
                    if (set.contains(hashValue)) continue;
                    set.add(hashValue);
                    q.add(game);
                }
            }
        }
        return 0;
    }

    static class Game {
        int cnt;
        int prev;
        Stick[] sticks;

        String hash() {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 3; i++) {
                for (int plate : sticks[i].status) {
                    sb.append(plate);
                }
                sb.append(",");
            }
            return sb.toString();
        }

        static Game newGame(Game prev) {
            Stick[] sticks = new Stick[3];
            for (int i = 0; i < 3; i++) {
                sticks[i] = new Stick(prev.sticks[i].status, prev.sticks[i].abc);
            }
            return new Game(prev.cnt, prev.prev, sticks);
        }

        Game(int cnt, int prev, Stick[] sticks) {
            this.cnt = cnt;
            this.prev = prev;
            this.sticks = sticks;
        }
    }

    static class Stick {
        List<Integer> status;
        int[] abc;

        void addPlate(int c) {
            this.status.add(c);
            abc[c]++;
        }

        int getLastPlate() {
            int idx = this.status.size()-1;
            if (idx < 0) return -1;
            int num = status.remove(idx);
            abc[num]--;
            return num;
        }

        Stick (List<Integer>status, int[] abc) {
            this.status = new LinkedList<>(status);
            this.abc = Arrays.copyOf(abc, 3);
        }
    }
}
