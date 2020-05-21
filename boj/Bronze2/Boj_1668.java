// 트로피 진열
// 하
// 탐색
// 11 / 20분

package boj.Bronze2;

import java.util.Scanner;

public class Boj_1668 {
    public static void main(String[] args){
        Scanner scin = new Scanner(System.in);
        int N = scin.nextInt(); // 트로피 개수
        scin.nextLine();
        int tro[] = new int[N];

        for (int i=0; i<N; i++){ // 트로피 입력
            tro[i] = scin.nextInt();
            scin.nextLine();
        }

        int leftCount = 0;
        int rightCount = 0;

        //왼쪽에서 보는 것 세기
        for (int i = 0, max=0; i<N; i++){
            if (tro[i]>max){
                leftCount++;
                max = tro[i];
            }
        }
        //오른쪽에서 보는 것 세기
        for(int i =N-1, max=0;i>=0;i--){
            if (tro[i]>max){
                rightCount++;
                max = tro[i];
            }
        }


        System.out.println(leftCount);
        System.out.println(rightCount);
        scin.close();

    }
    
}