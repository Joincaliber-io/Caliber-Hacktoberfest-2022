package com.college.wipro;

import java.util.Scanner;

public class RollNumberGen {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int regNo = s.nextInt();
        int rollNo = convertRegNoToRollNo(regNo);
        System.out.println(rollNo);
    }

    private static int convertRegNoToRollNo(int regNo) {
        String regStr = String.valueOf(regNo);
        String rollStr = "";
        for (int i=0; i+2 < regStr.length(); i += 2) {
            if (regStr.charAt(i) >= regStr.charAt(i+1)) {
                rollStr += regStr.charAt(i);
            } else {
                rollStr += regStr.charAt(i + 1);
            }
        }
        if (regStr.length() % 2 != 0) {
            rollStr += regStr.charAt(regStr.length() - 1);
        } else {
            if (regStr.charAt(regStr.length() - 1) >= regStr.charAt(regStr.length() - 2)) {
                rollStr += regStr.charAt(regStr.length() - 1);
            } else {
                rollStr += regStr.charAt(regStr.length() - 2);
            }
        }
        return Integer.parseInt(rollStr);
    }
}
