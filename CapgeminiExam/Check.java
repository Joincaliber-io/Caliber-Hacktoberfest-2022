package com.college.CapgeminiExam;

public class Check {

    public static boolean printChar(char c) {
        System.out.println(c);
        return true;
    }

    public static void main(String[] args) {
        int i = 0;
        for (printChar('A'); printChar('B')&&(i<2); printChar('C')) {
            i ++;
            printChar('D');
        }
    }
}
