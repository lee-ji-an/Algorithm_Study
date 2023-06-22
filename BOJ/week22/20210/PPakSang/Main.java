package org.example.study.week22.파일탐색기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<String> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr.add(br.readLine());
        }


        arr.sort((s1, s2) -> {
            int idx1 = 0;
            int idx2 = 0;
            while (s1.length() > idx1 && s2.length() > idx2) {
                CharInfo info1 = findNextChar(s1, idx1);
                CharInfo info2 = findNextChar(s2, idx2);
                String str1 = info1.str;
                String str2 = info2.str;

                if (info1.isNumeric && info2.isNumeric) {
                    if (str1.equals(str2)) {
                        idx1 += str1.length();
                        idx2 += str2.length();
                        continue;
                    }

                    // 3 > 12
                    int zeroCnt1 = 0;
                    int zeroCnt2 = 0;

                    for (int i = 0; i < str1.length(); i++) {
                        if (str1.charAt(i) == '0') {
                            zeroCnt1++;
                            if (i == str1.length()-1) {
                                str1 = "0";
                            }
                            continue;
                        }
                        str1 = str1.substring(i);
                        break;
                    }

                    for (int i = 0; i < str2.length(); i++) {
                        if (str2.charAt(i) == '0') {
                            zeroCnt2++;
                            if (i == str2.length()-1) {
                                str2 = "0";
                            }
                            continue;
                        }
                        str2 = str2.substring(i);
                        break;
                    }


                    int res = str1.compareTo(str2);
                    if (res == 0) {
                        return zeroCnt1 - zeroCnt2;
                    }


                    if (str1.length() != str2.length()) {
                        return str1.length() - str2.length();
                    }

                    return str1.compareTo(str2);
                }

                if (info1.isNumeric) {
                    return -1;
                }

                if (info2.isNumeric) {
                    return 1;
                }

                // 둘다 문자열일 때
                if (str1.equals(str2)) {
                    idx1++;
                    idx2++;
                    continue;
                }

                return calcChar(str1.charAt(0)) - calcChar(str2.charAt(0));
            }

            return s1.length() - s2.length();
        });

        for (String s : arr) {
            System.out.println(s);
        }
    }

    static int calcChar(char c) {
        if (Character.isUpperCase(c)) {
            return (c - 'A')*2;
        }
        return (c - 'a')*2 + 1;
    }

    static CharInfo findNextChar(String s, int start) {
        char c = s.charAt(start);
        CharInfo res = new CharInfo();

        if (Character.isDigit(c)) {
            int end = start;
           while (s.length() > end) {
               if (!Character.isDigit(s.charAt(end))) {
                   break;
               }
               end++;
           }
           res.isNumeric = true;
           res.str = s.substring(start, end);
            return res;
        }

        res.str = String.valueOf(c);
        return res;
    }

    static class CharInfo {
        String str;
        Boolean isNumeric = false;
    }
}
