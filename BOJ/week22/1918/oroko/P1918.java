package baekjoon.study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P1918 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        List<String> list = new LinkedList<>();
        for(int i = 0; i < s.length(); i++) list.add(String.valueOf(s.charAt(i)));

        System.out.println(bracket(list));
    }

    // 괄호 제거하기
    static String bracket(List<String> list) {
        Deque<String> deq = new ArrayDeque<>();
        for (String ex : list) {
            if (ex.equals(")")) {
                String s;
                LinkedList<String> temp = new LinkedList<>();

                while (!(s = deq.removeLast()).equals("(")) {
                    temp.addFirst(s);
                }
                deq.addLast(bracket(temp));
                continue;
            }

            deq.addLast(ex);
        }

        List<String> newList = new LinkedList<>();
        while(!deq.isEmpty()) {
            newList.add(deq.removeFirst());
        }
        return arrange(newList);
    }

    // 괄호 없는 중위 표기식을 후위 표기식으로 만들기
    static String arrange(List<String> list) {
        process(list, "*", "/");
        process(list, "+", "-");

        return list.get(0);
    }

    // a+b => ab+
    static void process(List<String> list, String operator1, String operator2) {
        for(int i = 0; i < list.size(); i++) {
            if(list.get(i).equals(operator1) || list.get(i).equals(operator2)) {
                String operand1 = list.get(i-1);
                String operator = list.get(i);
                String operand2 = list.get(i+1);

                list.add(i, operand1 + operand2 + operator);

                list.remove(operand1);
                list.remove(operand2);
                list.remove(operator);

                i--;
            }
        }
    }
}
