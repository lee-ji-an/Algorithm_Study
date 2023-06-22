package baekjoon.study;

import java.io.*;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class P20210 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        FileName[] fileNames = new FileName[N];
        for(int i = 0; i < N; i++) {
            fileNames[i] = new FileName(br.readLine());
        }

        Arrays.sort(fileNames, (o1, o2) -> {
            for(int i = 0; i < o1.group.size() && i < o2.group.size(); i++) {
                String val1 = o1.group.get(i);
                String val2 = o2.group.get(i);
                if(val1.equals(val2)) continue;

                boolean val1IsDigit = Character.isDigit(val1.charAt(0));
                boolean val2IsDigit = Character.isDigit(val2.charAt(0));

                // 둘 다 숫자열
                if(val1IsDigit && val2IsDigit) {
                    BigInteger num1 = new BigInteger(val1);
                    BigInteger num2 = new BigInteger(val2);

                    if(num1.equals(num2)) return Integer.compare(val1.length(), val2.length());
                    return num1.compareTo(num2);
                }

                // val1만 숫자열
                if(val1IsDigit) return -1;
                // val2만 숫자열
                if(val2IsDigit) return 1;

                // 둘 다 알파벳
                for(int j = 0; j < val1.length() && j < val2.length(); j++) {
                    char c1 = val1.charAt(j);
                    char c2 = val2.charAt(j);
                    if(c1 == c2) continue;

                    char uc1 = Character.toUpperCase(c1);
                    char uc2 = Character.toUpperCase(c2);

                    if(uc1 == uc2) return Character.compare(c1, c2);
                    return Character.compare(uc1, uc2);
                }

                return Integer.compare(val1.length(), val2.length());
            }

            return Integer.compare(o1.group.size(), o2.group.size());
        });

        for(FileName f : fileNames) {
            bw.write(f.s);
            bw.newLine();
        }

        bw.flush();
    }

    static class FileName {
        String s;
        List<String> group = new ArrayList<>();

        FileName(String s) {
            this.s = s;

            int i = 0;
            StringBuilder sb = new StringBuilder();

            while(i < s.length()) {
                if(Character.isDigit(s.charAt(i))) {
                    while (i < s.length() && Character.isDigit(s.charAt(i))) {
                        sb.append(s.charAt(i++));
                    }
                }
                else {
                    while(i < s.length() && !Character.isDigit(s.charAt(i))) {
                        sb.append(s.charAt(i++));
                    }
                }

                group.add(sb.toString());
                sb.setLength(0);
            }
        }
    }
}
