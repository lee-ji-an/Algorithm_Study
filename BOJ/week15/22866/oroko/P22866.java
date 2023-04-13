import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class P22866 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        Building[] buildings = new Building[N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Building> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o2.h, o1.h));
        for(int i = 1; i <= N; i++) {
            buildings[i] = new Building(i, Integer.parseInt(st.nextToken()));
            pq.add(buildings[i]);
        }

        TreeMap<Integer, Integer> left = new TreeMap<>();
        TreeMap<Integer, Integer> right = new TreeMap<>();
        int[] cnt = new int[N+1];
        int[] nearBuilding = new int[N+1];

        for(int i = 1; i <= N; i++) {
            Building building = pq.remove();
            Integer l = left.lowerKey(building.id); // 왼쪽에서 볼 수 있는 가장 가까운 건물 번호
            Integer r = right.higherKey(building.id);   // 오른쪽에서 볼 수 있는 가장 가까운 건물 번호
            int sum = 0;

            if(l != null) {
                int l_val = left.get(l);
                if(buildings[l].h == building.h) l = nearBuilding[l];
                else l_val++;
                sum += l_val;
                left.put(building.id, l_val);
            } else {
                left.put(building.id, 0);
            }

            if(r != null) {
                int r_val = right.get(r);
                if(buildings[r].h == building.h) r = nearBuilding[r];
                else r_val++;
                sum += r_val;
                right.put(building.id, r_val);
            } else {
                right.put(building.id, 0);
            }

            cnt[building.id] = sum;

            if(l == null) {
                if(r != null) nearBuilding[building.id] = r;    // r만 있음
                // 둘다 null
            }
            else {
                if(r != null) {     // 둘다 null이 아님
                    int gap1 = building.id-l;
                    int gap2 = r-building.id;
                    if(gap1 == gap2) nearBuilding[building.id] = l;
                    else nearBuilding[building.id] = gap1 < gap2 ? l : r;
                }
                else nearBuilding[building.id] = l;     // l만 있음
            }
        }

        for(int j = 1; j <= N; j++) {
            bw.write(String.valueOf(cnt[j]));
            if(cnt[j] > 0) {
                bw.write(" ");
                bw.write(String.valueOf(nearBuilding[j]));
            }
            bw.newLine();
        }
        bw.flush();
    }

    static class Building {
        int id, h;

        public Building(int id, int h) {
            this.id = id;
            this.h = h;
        }
    }
}
