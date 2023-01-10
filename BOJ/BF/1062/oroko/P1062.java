import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] wordsBit;
    static int max = 0;
    public static int readable(int learn, int word) {
        return (word & learn) == word ? 1 : 0;
    }

    public static void comb(Character[] alphabets, int start, int r, boolean[] visited) {
        if(r == 0) {
            int learn = 0;
            for(int i = 0; i < 'z'-'a'+1; i++) {
                if(visited[i]) learn |= (1 << i);
            }

            int cnt = 0;
            for(int word : wordsBit) cnt += readable(learn, word);
            max = Math.max(max, cnt);
            return;
        }

        for(int i = start; i < alphabets.length; i++) {
            if(!visited[alphabets[i] - 'a']) {
                visited[alphabets[i] - 'a'] = true;
                comb(alphabets, i+1, r-1, visited);
                visited[alphabets[i] - 'a'] = false;
            }
        }
        if(r > 0) comb(alphabets, 0, 0, visited);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        String[] words = new String[N];
        wordsBit = new int[N];
        Set<Character> alphabets = new HashSet<>();
        for(int i = 0; i < N; i++) {
            words[i] = br.readLine();
            int bit = 0;
            for(int j = 0; j < words[i].length(); j++) {
                alphabets.add(words[i].charAt(j));
                bit |= (1 << words[i].charAt(j) - 'a');
            }
            wordsBit[i] = bit;
        }
        boolean[] visited = new boolean['z'-'a'+1];
        visited[0] = true;
        visited['n'-'a'] = true;
        visited['t'-'a'] = true;
        visited['i'-'a'] = true;
        visited['c'-'a'] = true;
        comb(alphabets.toArray(new Character[0]), 0, K-5, visited);
        System.out.println(max);
    }
}
