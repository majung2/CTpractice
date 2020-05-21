// 문서 검색
// 하
// 탐색
// 25 / 20분 

package boj.Silver4;

import java.util.Scanner;

public class Boj_1543 {
    public static void main(String[] args) {
        Scanner scin = new Scanner(System.in);
        String doc = scin.nextLine();
        String word = scin.nextLine();
        scin.close();

        int result = 0;
        int count = 0;
        int len = word.length();

        for (int j = 0; j <= doc.length() - len; j++) {
            count = 0;
            for (int i = j; i <= doc.length() - len;) {
                if (doc.substring(i, i + len).equals(word)) {
                    count++;
                    i += len;
                } else {
                    i++;
                }
            }
            result = (result > count) ? result : count;
        }
        System.out.println(result);
    }

}