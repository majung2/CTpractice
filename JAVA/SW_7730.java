package JAVA;

import java.util.Scanner;

public class SW_7730 {
    static int N;
    static int M;
    static int[] trees;

    public static void main(final String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T; // 테스트 케이스 수
        T = sc.nextInt();
        sc.nextLine();

        for (int test_case = 1; test_case <= T; test_case++) {
            N = sc.nextInt(); // 나무 수
            M = sc.nextInt(); // 원하는 원목의 길이
            sc.nextLine();

            int start = 0;
            int end = 0;
            int mid = 0;
            int answer = 0;

            trees = new int[N]; // 나무들 높이 담을 배열
            for (int i = 0; i < N; i++) {
                trees[i] = sc.nextInt();
                if (trees[i] > end) {
                    end = trees[i];
                }
            }
            sc.nextLine();

            //정렬
            QuickSorter.quickSort(trees);

            while (start < end) {
                mid = (start + end) / 2;
                if (check(mid)) {
                    start = mid + 1;
                    answer = mid;
                } else {
                    end = mid;
                }
            }

            System.out.println("#" + test_case + " " + answer);
        }
        sc.close();

    }

    public static boolean check(int H) {
        long sum = 0;
        for (int tree : trees) {
            if (tree > H){
                sum += (tree-H);
            } else{
                break;
            }
        }
        if (sum >= M) return true;
        else return false;
    }

    
}

class QuickSorter {
    public static void quickSort(int[] arr) {
        sort(arr, 0, arr.length - 1);
    }

    private static void sort(int[] arr, int low, int high) {
        if (low >= high) return;

        int mid = partition(arr, low, high);
        sort(arr, low, mid - 1);
        sort(arr, mid, high);
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[(low + high) / 2];
        while (low <= high) {
            while (arr[low] > pivot) low++;
            while (arr[high] < pivot) high--;
            if (low <= high) {
                swap(arr, low, high);
                low++;
                high--;
            }
        }
        return low;
    }

    private static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
