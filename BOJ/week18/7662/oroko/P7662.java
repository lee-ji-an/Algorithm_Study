import java.io.*;
import java.util.*;

public class P7662 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());

            PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());
            PriorityQueue<Integer> min = new PriorityQueue<>();
            Map<Integer, Integer> map = new HashMap<>();
            for(int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                char cmd = st.nextToken().charAt(0);
                int num = Integer.parseInt(st.nextToken());
                if(cmd == 'I') {
                    max.add(num);
                    min.add(num);
                    map.put(num, map.getOrDefault(num, 0) + 1);
                }
                else {
                    if(max.isEmpty()) continue;
                    if(num == 1) {
                        while(!max.isEmpty()) {
                            if(map.containsKey(max.peek())) {
                                int del = max.remove();
                                if(map.get(del) == 1) map.remove(del);
                                else map.put(del, map.get(del)-1);
                                break;
                            }
                            max.remove();
                        }
                    }
                    else {
                        while(!min.isEmpty()) {
                            if(map.containsKey(min.peek())) {
                                int del = min.remove();
                                if(map.get(del) == 1) map.remove(del);
                                else map.put(del, map.get(del)-1);
                                break;
                            }
                            min.remove();
                        }
                    }
                }
            }

            while(!max.isEmpty()) {
                if(map.containsKey(max.peek())) break;
                max.remove();
            }
            while(!min.isEmpty()) {
                if(map.containsKey(min.peek())) break;
                min.remove();
            }

            if(max.isEmpty()) bw.write("EMPTY\n");
            else {
                bw.write(String.valueOf(max.remove()));
                bw.write(" ");
                bw.write(String.valueOf(min.remove()));
                bw.newLine();
            }
        }

        bw.flush();
    }
}
