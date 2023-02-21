import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P6603 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            if(k == 0) break;
            int[] arr = new int[k];
            for(int i = 0; i < k; i++) arr[i] = Integer.parseInt(st.nextToken());
            select(arr, 0, 0, new boolean[k]);
            System.out.println();
        }
    }

    static void select(int[] arr, int start, int r, boolean[] visited) {
        if(r == 6) {
            for(int i = 0; i < arr.length; i++) {
                if(visited[i]) System.out.print(arr[i] + " ");
            }
            System.out.println();
            return;
        }

        for(int i = start; i < arr.length; i++) {
            visited[i] = true;
            select(arr, i+1, r+1, visited);
            visited[i] = false;
        }
    }
}
