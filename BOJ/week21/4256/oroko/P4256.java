import java.io.*;
import java.util.StringTokenizer;

public class P4256 {

    static int[] preorder;
    static int[] inorder;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());

            preorder = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i = 0; i < N; i++) preorder[i] = Integer.parseInt(st.nextToken());

            inorder = new int[N];
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < N; i++) inorder[i] = Integer.parseInt(st.nextToken());

            p = 0;
            search(0, N-1, bw);
            bw.newLine();
        }
        bw.flush();
    }

    static int p;
    static void search(int left, int right, BufferedWriter bw) throws IOException {
        if(left >= right) {
            bw.write(inorder[left] + " ");
            return;
        }

        int root = -1;
        for(int i = left; i <= right; i++) {
            if(inorder[i] == preorder[p]) {
                root = i;
                break;
            }
        }

        if(root-1 >= left) {
            p++;
            search(left, root-1, bw);
        }
        if(root+1 <= right) {
            p++;
            search(root+1, right, bw);
        }
        search(root, root, bw);
    }
}
