package org.example.study.week14.전설의JBNU;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main2 {


    static int N,M,K;
    static TreeMap<Integer, Integer> JBNU = new TreeMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            JBNU.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        for(int i=0; i<M; i++){
            JBNUSystem(new StringTokenizer(br.readLine()));
        }
    }

    public static void JBNUSystem(StringTokenizer st){
        int type = Integer.parseInt(st.nextToken());
        int key = Integer.parseInt(st.nextToken());
        int val;

        //1은 추가
        //2는 변경 -> 유일 key 없으면 무시
        //3은 데이터 출력 -> 없으면 1, 2개 이상은 ?
        switch (type){
            case 1: {
                val = Integer.parseInt(st.nextToken());
                JBNU.put(key, val);
                break;
            }

            case 2: {
                val = Integer.parseInt(st.nextToken());
                if(JBNU.containsKey(key)){
                    JBNU.put(key,val);
                    break;
                }
                int newKey = findSimilar(JBNU.ceilingKey(key), JBNU.floorKey(key), key);
                if(newKey >= 0){
                    JBNU.put(newKey,val);
                }
                break;
            }

            case 3:{
                if(JBNU.containsKey(key)){
                    System.out.println(JBNU.get(key));
                    break;
                }
                int newKey = findSimilar(JBNU.ceilingKey(key), JBNU.floorKey(key), key);
                if(newKey < 0){
                    if(newKey < -1){
                        System.out.println("?");
                    }
                    else{
                        System.out.println(-1);
                    }

                }
                else{
                    System.out.println(JBNU.get(newKey));
                }
                break;
            }
        }
    }

    static int findSimilar(Integer a, Integer b, int key){
        if(a == null){
            a = -K;
        }

        if(b == null){
            b = K;
        }

        int val1 = Math.abs(a-key);
        int val2 = Math.abs(-b+key);

        //만족 x
        if(val1 > K && val2 > K){
            return -1;
        }
        //2개 이상
        else if(val1 == val2){
            return -2;
        }
        //만족하는애
        else{
            return (val1 < val2) ? a : b;
        }
    }
}
