package com.college.acsenture;

import java.util.ArrayList;
import java.util.Scanner;

public class RelativePrime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(findRelativePrime(n));
    }

    private static int findRelativePrime(int n) {
        ArrayList<Integer> primeNumberList = givePrimeNumberBySieveAlgorithm(n);
        int count = 0;
        for (int x : primeNumberList) {
            if (gcd(x, n) == 1) count ++;
        }
        return count;
    }

    public static ArrayList<Integer> givePrimeNumberBySieveAlgorithm(int max) {
        ArrayList<Integer> primeNumberList = new ArrayList<>();
        int[][] sieveArray = new int[max-2][2];

        int count = 2;
        for (int i=0; i < max-2; i++) {
            sieveArray[i][0] = count;
            sieveArray[i][1] = 0;
            count ++;
        }

        primeNumberList.add(1);
        for (int i=0; i < sieveArray.length; i++) {
            if(sieveArray[i][1] == 0) {
                primeNumberList.add(sieveArray[i][0]);
                for(int j=sieveArray[i][0]+sieveArray[i][0]-2; j < sieveArray.length; j += sieveArray[i][0]) {
                    sieveArray[j][1] = 1;
                }
            }
        }
        return primeNumberList;
    }

    private static int gcd(int a, int b) {
        for (int i = Math.min(a, b); i > 1; i--) {
            if (a % i == 0 && b % i == 0)
                return i;
        }

        return 1;
    }
}
