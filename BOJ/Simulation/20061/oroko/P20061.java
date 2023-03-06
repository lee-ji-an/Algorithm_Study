import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P20061 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        boolean[][] blue = new boolean[4][6];
        boolean[][] green = new boolean[4][6];
        int score = 0;
        for(int n = 0; n < N; n++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            put(blue, t, x);
            put(green, (t == 1 ? 1 : (t == 2 ? 3 : 2)), y);

            score += checkFull(blue);
            score += checkFull(green);

            checkLight(blue);
            checkLight(green);
        }
        System.out.println(score);
        System.out.println(count(blue) + count(green));
    }

    // 위에서부터 탐색해서 막히면 멈추고 블록 놓기
    public static void put(boolean[][] board, int t, int row) {
        int i;

        switch (t) {
            case 1: {
                for(i = 0; i < 6; i++) {
                    if(board[row][i]) break;
                }
                board[row][i-1] = true;
                break;
            }
            case 2: {
                for(i = 0; i < 6; i++) {
                    if(board[row][i]) break;
                }
                board[row][i-1] = board[row][i-2] = true;
                break;
            }
            default: {
                for(i = 0; i < 6; i++) {
                    if(board[row][i] || board[row+1][i]) break;
                }
                board[row][i-1] = board[row+1][i-1] = true;
            }
        }
    }

    public static int checkFull(boolean[][] board) {
        int cnt = 0;
        int sj = 0;
        for(int j = 5; j >= 0; j--) {       // 뒤에서부터 탐색해서 가득찬 줄, 줄 수 찾기
            if(checkColumnFull(board, j)) {
                cnt++;
                sj = j;
            }
        }

        if(cnt == 0) return cnt;

        for(int j = sj-1; j >= 0; j--) {    // 가득찬 줄 중에 가장 윗 줄부터 가득찬 줄 수 만큼 밀기
            for(int i = 0; i < 4; i++) board[i][j+cnt] = board[i][j];
        }

        for(int i = 0; i < 4; i++) board[i][0] = false;     // 한 줄씩 밀렸으니 가장 윗 줄 비워주기
        return cnt;
    }

    private static boolean checkColumnFull(boolean[][] board, int j) {
        for(int i = 0; i < 4; i++) {
            if(!board[i][j]) return false;
        }

        return true;
    }

    public static void checkLight(boolean[][] board) {
        int cnt = 0;
        for(int j = 0; j < 2; j++) {    // 0, 1열 중에 몇 줄에 놓여 있는지 찾기
            for(int i = 0; i < 4; i++) {
                if(board[i][j]) {
                    cnt++;
                    break;
                }
            }
        }

        if(cnt == 0) return;

        for(int j = 5-cnt; j >= 0; j--) {   // 뒤에서부터 옮기기
            for(int i = 0; i < 4; i++) board[i][j+cnt] = board[i][j];
        }

        for(int j = 0; j < 2; j++) {    // 0, 1열 비우기
            for(int i = 0; i < 4; i++) board[i][j] = false;
        }
    }

    public static int count(boolean[][] board) {
        int cnt = 0;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 6; j++) {
                if(board[i][j]) cnt++;
            }
        }
        return cnt;
    }

}
