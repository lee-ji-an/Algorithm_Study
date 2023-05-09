package org.example.study.week18.이중우선순위큐;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            PriorityQueue<Num> min = new PriorityQueue<>((n1, n2) -> Integer.compare(n1.num, n2.num));
            PriorityQueue<Num> max = new PriorityQueue<>((n1, n2) -> Integer.compare(n2.num, n1.num));

            int K = Integer.parseInt(br.readLine());
            for (int j = 0 ; j < K; j++) {
                String[] temp = br.readLine().split(" ");
                int num = Integer.parseInt(temp[1]);

                if (temp[0].equals("I")) {
                    Num n = new Num(num, false);
                    max.add(n);
                    min.add(n);
                } else {
                    if (num == -1) {
                        while (min.size() > 0) {
                            Num mN = min.poll();
                            if (mN.selected) continue;
                            mN.selected = true;
                            break;
                        }
                    } else {
                        while (max.size() > 0) {
                            Num mN = max.poll();
                            if (mN.selected) continue;
                            mN.selected = true;
                            break;
                        }
                    }
                }
            }

            while (max.size() > 0) {
                Num mN = max.poll();
                if (mN.selected) continue;
                max.add(mN);
                break;
            }

            while (min.size() > 0) {
                Num mN = min.poll();
                if (mN.selected) continue;
                min.add(mN);
                break;
            }

            if (max.size() == 0) {
                System.out.println("EMPTY");
                continue;
            }

            System.out.println(max.poll().num + " " + min.poll().num);
        }
    }

    static class Num {
        int num;
        boolean selected;

        public Num(int num, boolean selected) {
            this.num = num;
            this.selected = selected;
        }
    }
}
