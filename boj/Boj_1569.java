// 새
// 하
// 탐색
// 10 / 20분
package boj;

import java.util.Scanner;

public class Boj_1569 {
    public static void main(String[] args) {
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt();
        int ans = 0;

        while (N > 0) {
            for (int i = 1; N - i >= 0; i++) {
                N -= i;
                ans++;
            }
        }

        System.out.println(ans);

    }

}