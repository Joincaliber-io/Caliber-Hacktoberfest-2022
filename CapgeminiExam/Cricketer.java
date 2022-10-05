package com.college.CapgeminiExam;

import java.util.Scanner;

public class Cricketer {
    public static void findCricketerId(int[] array, int size, int score) {
        for (int i = 1; i < size; i += 2) {
            if (array[i] > score)
                System.out.println(array[i-1]);
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        int[] array = new int[n];

        for (int i = 0; i < n; i ++) {
            array[i] = s.nextInt();
        }

        int score = s.nextInt();

        findCricketerId(array, n, score);
    }
}
