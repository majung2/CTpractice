// 성 지키기
// 하
// 탐색
// 25 / 20분

package boj;

import java.util.Scanner;
import java.util.stream.IntStream;

public class Boj_1236 {
    public static void main(String[] args) {
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt();
        int M = scin.nextInt();
        scin.nextLine();

        int guards[][] = new int[N][M];
        int ans = 0; // 추가해야하는 경비원의 최솟값

        for (int i = 0; i < N; i++) {
            String data = scin.nextLine();
            for (int j = 0; j < M; j++) {
                if (data.charAt(j) == 'X') { // 경비원 있음
                    guards[i][j] = 1;
                } else {
                    guards[i][j] = 0;
                }
            }
        }

        // 가로줄 확인
        int noN = 0; // 경비원 없는 가로 줄 수
        for (int i = 0; i < N; i++) {
            if (!IntStream.of(guards[i]).anyMatch(x -> x == 1)) { // 경비원이 없는 줄
                noN++;
            }
        }
        // 세로줄 확인
        int noM = 0; // 경비원 없는 세로 줄 수
        for (int j = 0; j < M; j++) {
            int line = 0;
            for (int i = 0; i < N; i++) {
                if (guards[i][j] == 1)
                    line++;
            }
            if (line == 0)
                noM++;
        }

        ans = (noN>noM?noN:noM);
        System.out.println(ans);
        scin.close();
    }

}