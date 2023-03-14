package org.example.study.greedy.우체국;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * 특정 집 기준 누적합 비교
 *
 * 덜 멀어지고 더 가까워지는 지점 찾기
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        long[] prefixSum = new long[N+1];

        List<House> houses = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split(" ");

            int location = Integer.parseInt(temp[0]);
            int population = Integer.parseInt(temp[1]);

            houses.add(new House(i+1, location, population));
        }

        houses.sort((h1, h2) -> {
            if (h1.location == h2.location) {
                return h1.num - h2.num;
            }
            return h1.location - h2.location;
        });

        for (int i = 1; i <= houses.size(); i++) {
            House house = houses.get(i-1);
            prefixSum[i] = prefixSum[i-1] + house.population;
        }

        if (N == 1) {
            System.out.println(houses.get(0).location);
            return;
        }

        for (int i = 1; i <= N; i++) {
            long left = prefixSum[i];
            long right = prefixSum[N] - prefixSum[i];

            if (left >= right) {
                System.out.println(houses.get(i-1).location);
                return;
            }
        }
    }

    static class House {
        int num;
        int location;
        int population;

        public House(int num, int location, int population) {
            this.location = location;
            this.population = population;
        }
    }
}
