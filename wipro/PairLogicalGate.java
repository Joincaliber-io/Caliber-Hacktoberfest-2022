package com.college.wipro;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class PairLogicalGate {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        ArrayList<Integer> arr = new ArrayList<>();
        for (int i=0; i < n; i ++) {
            arr.add(s.nextInt());
        }

        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i : arr) {
            hashMap.put(i, 0);
        }

        for (int i : arr) {
            hashMap.put(i, hashMap.get(i)+1);
        }

        for (int key : hashMap.keySet()) {
            if (hashMap.get(key) < 2) {
                System.out.println(key);
            }
        }
    }
}
