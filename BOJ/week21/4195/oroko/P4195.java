import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class P4195 {

    static Map<String, String> root;
    static Map<String, Integer> cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            root = new HashMap<>();
            cnt = new HashMap<>();
            for(int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String f1 = st.nextToken();
                String f2 = st.nextToken();
                if(!root.containsKey(f1)) {
                    root.put(f1, f1);
                    cnt.put(f1, 1);
                }
                if(!root.containsKey(f2)) {
                    root.put(f2, f2);
                    cnt.put(f2, 1);
                }
                union(f1, f2);
                bw.write(String.valueOf(cnt.get(find(f1))));
                bw.newLine();
            }

        }
        bw.flush();
    }

    static String find(String f) {
        if(root.get(f).equals(f)) return f;

        String fRoot = find(root.get(f));
        root.put(f, fRoot);
        cnt.put(fRoot, cnt.get(fRoot) + cnt.get(f));
        cnt.put(f, 0);
        return fRoot;
    }

    static void union(String f1, String f2) {
        String r1 = find(f1);
        String r2 = find(f2);
        if(r1.equals(r2)) return;

        root.put(r1, r2);
        cnt.put(r2, cnt.get(r1) + cnt.get(r2));
        cnt.put(r1, 0);
    }
}
