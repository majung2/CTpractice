// 공유기 설치
// 중
// 이진 탐색 : 데이터가 클 때 탐색시
// X / 40분
// Silver 2

package boj.Silver2;

import java.util.Arrays;
import java.util.Scanner;

public class Boj_2110 {
    public static void main(String[] args){
        Scanner scin = new Scanner(System.in);

        int N = scin.nextInt(); // 집 개수
        int C = scin.nextInt(); // 공유기 개수
        int house[] = new int[N]; // 집 좌표

        for (int i =0 ; i<N ;i++){
            house[i] = scin.nextInt();
        }
        Arrays.sort(house); // 정렬

        int start = 1;
        int end = house[N-1]-house[0];
        int result = 0;

        while(start<=end){
            int mid = (start+end)/2; // mid는 갭 의미
            int value = house[0];
            int count = 1;

            for(int i =1;i<N;i++){
                if (house[i]>=value+mid){
                    value = house[i];
                    count++;
                }
            }

            if (count>=C){
                start = mid+1;
                result = mid;
            }else{
                end = mid-1;
            }
        }

        System.out.println(result);
        scin.close();
    }
    
}