package com.college.wipro;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class NumberOfInternID {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int n = s.nextInt();

        ArrayList<String> arrayList = new ArrayList<>();

        List<String> volunteerApplicationId = List.of("A", "E", "I", "O", "U");

        for (int i=0; i < n; i ++) {
            arrayList.add(s.next());
        }

        int numOfInterns = 0;
        for (String str : arrayList) {
            if (!volunteerApplicationId.contains(str.toUpperCase())) {
                numOfInterns ++;
            }
        }

        System.out.println(numOfInterns);
    }
}
