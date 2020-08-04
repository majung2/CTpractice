package JAVA;

import java.util.Arrays;

public class Hello {
    public static void main(String[] args){
        int[] array = {1,4,5,2,3};

        QuickSorter.quickSort(array);

        System.out.println(Arrays.toString(array));
    }
}