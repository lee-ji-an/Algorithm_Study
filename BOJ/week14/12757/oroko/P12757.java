import java.io.*;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class P12757 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 초기화
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            map.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        // 명령
        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            switch (Integer.parseInt(st.nextToken())) {
                case 1: {
                    map.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
                    break;
                }
                case 2: {
                    int key = Integer.parseInt(st.nextToken());
                    key = selectKey(map, key, K);
                    if(key >= 0) map.put(key, Integer.parseInt(st.nextToken()));
                    break;
                }
                default: {
                    int key = Integer.parseInt(st.nextToken());
                    key = selectKey(map, key, K);
                    if(key >= 0) bw.write(String.valueOf(map.get(key)));
                    else if(key == -1) bw.write("-1");
                    else bw.write("?");
                    bw.newLine();
                }
            }
        }

        bw.flush();
    }


    static int selectKey(TreeMap<Integer, Integer> map, int target, int K) {
        if(map.containsKey(target)) return target;

        int minMax = map.lastKey() < target ? target + K + 1 : map.higherKey(target);
        int maxMin = map.firstKey() > target ? target + K + 1 : map.lowerKey(target);

        int gap1 = Math.abs(minMax - target);
        int gap2 = Math.abs(target - maxMin);

        if(gap1 <= K) {
            if(gap2 <= K) {
                return gap1 == gap2 ? -2 : (gap1 < gap2 ? minMax : maxMin);
            }
            return minMax;
        }
        return gap2 <= K ? maxMin : -1;
    }
}
