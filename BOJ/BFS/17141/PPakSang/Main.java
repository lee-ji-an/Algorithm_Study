import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 바이러스 놓을 수 있는 칸 10
 * 바이러스 놓을 수 있는 갯수 M
 *
 * 빈칸 벽 바이러스
 * 0 1 2
 */

public class Main {
    static int[] dirX = new int[]{1, -1, 0, 0};
    static int[] dirY = new int[]{0, 0, 1, -1};
    static boolean[][] map;
    static List<Position> possiblePos = new ArrayList<>();

    static int N;
    static int answer = Integer.MAX_VALUE;
    static int blank = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        int M = Integer.parseInt(temp[1]);

        map = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            temp = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                int num = Integer.parseInt(temp[j]);
                if (num == 2) possiblePos.add(new Position(i, j));
                if (num == 1) map[i][j] = true;
                if (num == 0) blank++;
            }
        }

        blank = blank + possiblePos.size() - M;
        if (blank == 0) {
            System.out.println(0);
            return;
        }

        selectPos(-1, 0, M, new ArrayList<>());
        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);

    }

    static void selectPos(int prev, int cnt, int max, List<Position> result) {
        if (cnt == max) {
            answer = Math.min(answer, bfs(result));
            return;
        }

        List<Position> next = new ArrayList<>(result);
        for (int i = prev+1; i < possiblePos.size(); i++) {
            next.add(possiblePos.get(i));
            selectPos(i, cnt+1, max, next);
            next.remove(possiblePos.get(i));
        }
    }

    static int bfs (List<Position> virusPos) {
        int result = 0;
        int polluted = 0;
        boolean[][] visited = new boolean[N][N];

        Queue<Position> q = new LinkedList<>();
        for (Position virus : virusPos) {
            q.add(virus);
            visited[virus.x][virus.y] = true;
        }

        while (true) {
            int size = q.size();
            boolean flag = false;
            for (int j = 0; j < size; j++) {
                Position cur = q.poll();
                for (int i = 0; i < 4; i++) {
                    int nX = cur.x + dirX[i];
                    int nY = cur.y + dirY[i];

                    if (checkRange(nX, nY) && !map[nX][nY]) {
                        if (visited[nX][nY]) continue;
                        visited[nX][nY] = true;
                        q.add(new Position(nX, nY));
                        flag = true;
                        polluted++;
                        if (polluted == blank) return result+1;
                    }
                }
            }
            result++;
            if (!flag) break;
        }

        return Integer.MAX_VALUE;
    }

    static boolean checkRange(int x, int y) {
        if (x < 0 || x >= N) return false;
        if (y < 0 || y >= N) return false;
        return true;
    }
    static class Position {
        int x;
        int y;

        Position (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
