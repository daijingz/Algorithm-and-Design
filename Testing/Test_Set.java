/*      Student Information
*       -------------------
*       Student Name: Dai, Jingze
*       Student Number: 400201059
*       Course Code: CS/SE 2XB3
*       Lab Section: L03
*
*       I attest that the following code being submitted is my own individual work
*/
//Import File Writers and other classes for using.
import java.util.Arrays;
import java.util.Scanner;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Test_Set{
    //10 tests cases for unit testing (initially at empty)
    private static Set test_Case1;
    private static Set test_Case2;
    private static Set test_Case3;
    private static Set test_Case4;
    private static Set test_Case5;
    private static Set test_Case6;
    private static Set test_Case7;
    private static Set test_Case8;
    private static Set test_Case9;
    private static Set test_Case10;
    // number on value 0 or 1: to check whether tests are passed or not
    private static int t1, t2, t3, t4, t5, t6, t7, t8;

    public static void main(String[] args) throws IOException {
        //Read files by using File and Scanner.
        File file_Input = new File("C:\\Users\\david\\IdeaProjects\\Pracitce\\src\\input.txt");
        Scanner keyboard = new Scanner(file_Input);
        FileWriter Writer = new FileWriter("C:\\Users\\david\\IdeaProjects\\Pracitce\\src\\output.txt");
        //This test program check for 10 test cases and they are in text file first 10 lines.
        String test_String1 = keyboard.nextLine();
        String test_String2 = keyboard.nextLine();
        String test_String3 = keyboard.nextLine();
        String test_String4 = keyboard.nextLine();
        String test_String5 = keyboard.nextLine();
        String test_String6 = keyboard.nextLine();
        String test_String7 = keyboard.nextLine();
        String test_String8 = keyboard.nextLine();
        String test_String9 = keyboard.nextLine();
        String test_String10 = keyboard.nextLine();
        // Then we transfer them into string-typed arrays (Put all elements in)
        String[] test_Set1 = test_String1.split(",");
        String[] test_Set2 = test_String2.split(",");
        String[] test_Set3 = test_String3.split(",");
        String[] test_Set4 = test_String4.split(",");
        String[] test_Set5 = test_String5.split(",");
        String[] test_Set6 = test_String6.split(",");
        String[] test_Set7 = test_String7.split(",");
        String[] test_Set8 = test_String8.split(",");
        String[] test_Set9 = test_String9.split(",");
        String[] test_Set10 = test_String10.split(",");
        //We uses those created sets to build new set object and give values for those created test cases
        test_Case1 = new Set(test_Set1);
        test_Case2 = new Set(test_Set2);
        test_Case3 = new Set(test_Set3);
        test_Case4 = new Set(test_Set4);
        test_Case5 = new Set(test_Set5);
        test_Case6 = new Set(test_Set6);
        test_Case7 = new Set(test_Set7);
        test_Case8 = new Set(test_Set8);
        test_Case9 = new Set(test_Set9);
        test_Case10 = new Set(test_Set10);

        //Printing out first line
        System.out.println("Entering testUnion...");
        //Write first line to output.txt
        //First line of output.txt(initially at empty) should be "Entering testUnion"
        //Then change to next line
        Writer.write("Entering testUnion...");
        Writer.append('\n');
        //Run all the test programs
        test_Set_Union();
        test_Set_Intersection();
        test_Set_Difference();
        test_Set_Product();
        test_Is_Subset();
        test_Is_Equal();
        test_Get_Count();
        test_To_String();

        //check whether first test program passed or failed
        //write pass/fail string into output.txt iff first test program pass/fail
        if (t1 == 1){
            Writer.write("Set_Union Tests Passed");
            Writer.append('\n');
        } else if (t1 == 0){
            Writer.write("Set_Union Tests Failed");
            Writer.append('\n');
        }

        //check whether second test program passed or failed
        //write pass/fail string into output.txt iff second test program pass/fail
        if (t2 == 1){
            Writer.write("Set_Intersection Tests Passed");
            Writer.append('\n');
        } else if (t2 == 0){
            Writer.write("Set_Intersection Tests Failed");
            Writer.append('\n');
        }

        //check whether third test program passed or failed
        //write pass/fail string into output.txt iff third test program pass/fail
        if (t3 == 1){
            Writer.write("Set_Difference Tests Passed");
            Writer.append('\n');
        } else if (t3 == 0){
            Writer.write("Set_Difference Tests Failed");
            Writer.append('\n');
        }

        //check whether four test program passed or failed
        //write pass/fail string into output.txt iff four test program pass/fail
        if (t4 == 1){
            Writer.write("Set_Product Tests Passed");
            Writer.append('\n');
        } else if (t4 == 0){
            Writer.write("Set_Product Tests Failed");
            Writer.append('\n');
        }

        //check whether five test program passed or failed
        //write pass/fail string into output.txt iff five test program pass/fail
        if (t5 == 1){
            Writer.write("Is_Subset Tests Passed");
            Writer.append('\n');
        } else if (t5 == 0){
            Writer.write("Is_Subset Tests Failed");
            Writer.append('\n');
        }

        //check whether six test program passed or failed
        //write pass/fail string into output.txt iff six test program pass/fail
        if (t6 == 1){
            Writer.write("Is_Equal Tests Passed");
            Writer.append('\n');
        } else if (t6 == 0){
            Writer.write("Is_Equal Tests Failed");
            Writer.append('\n');
        }

        //check whether seven test program passed or failed
        //write pass/fail string into output.txt iff seven test program pass/fail
        if (t7 == 1){
            Writer.write("Get_Count Tests Passed");
            Writer.append('\n');
        } else if (t7 == 0){
            Writer.write("Get_Count Tests Failed");
            Writer.append('\n');
        }

        //check whether eighth test program passed or failed
        //write pass/fail string into output.txt iff eighth test program pass/fail
        if (t8 == 1){
            Writer.write("To_String Tests Passed");
            Writer.append('\n');
        } else if (t8 == 0){
            Writer.write("To_String Tests Failed");
            Writer.append('\n');
        }
        //Print out last line in the output line
        System.out.println("testUnion complete.");
        //Write Last line in the output.txt
        Writer.write("testUnion complete.");
        Writer.close();
    }

    //Programs for checking set_Union is work well as expectations or not
    private static void test_Set_Union(){
        //Create new (set object) test results for unit testing
        Set result1 = test_Case1.set_Union(test_Case2);
        Set result2 = test_Case3.set_Union(test_Case4);
        Set result3 = test_Case5.set_Union(test_Case6);
        Set result4 = test_Case7.set_Union(test_Case8);
        //Check whether the result is matched or not
        //if not match, t1 value is still 0
        if(!Arrays.equals(result1.set, (new String[]{"a", "s", "d", "f"}))){
            System.out.println("Set_Union Tests Failed");
        } else if (!Arrays.equals(result2.set, (new String[]{"s", "d", "a", "f"}))){
            System.out.println("Set_Union Tests Failed");
        } else if (!Arrays.equals(result3.set, (new String[]{"a", "s", "d", "f", "g", "h", "j", "k", "l"}))){
            System.out.println("Set_Union Tests Failed");
        } else if (!Arrays.equals(result4.set, (new String[]{"o", "p", "s", "d", "g", "as", "ad", "ag", "cv", "cb"}))){
            System.out.println("Set_Union Tests Failed");
        } else {
            //if match, then t1 value will be 1
            //And print out this program passed
            System.out.println("Set_Union Tests Passed");
            t1 = 1;
        }
    }

    //Programs for checking set_Intersection is work well as expectations or not
    private static void test_Set_Intersection(){
        //Create new (set object) test results for unit testing
        Set result1 = test_Case9.set_Intersection(test_Case10);
        Set result2 = test_Case3.set_Intersection(test_Case4);
        Set result3 = test_Case5.set_Intersection(test_Case6);
        Set result4 = test_Case7.set_Intersection(test_Case8);
        //Check whether the result is matched or not
        //if not match, t1 value is still 0
        if(!Arrays.equals(result1.set, (new String[]{}))){
            System.out.println("Set_Intersection Tests Failed");
        } else if (!Arrays.equals(result2.set, (new String[]{"s", "d", "a"}))){
            System.out.println("Set_Intersection Tests Failed");
        } else if (!Arrays.equals(result3.set, (new String[]{"a", "s", "d", "f"}))){
            System.out.println("Set_Intersection Tests Failed");
        } else if (!Arrays.equals(result4.set, (new String[]{}))){
            System.out.println("Set_Intersection Tests Failed");
        } else {
            //if match, then t2 value will be 1
            //And print out this program passed
            System.out.println("Set_Intersection Tests Passed");
            t2 = 1;
        }
    }

    //Programs for checking set_Difference is work well as expectations or not
    private static void test_Set_Difference(){
        //Create new (set object) test results for unit testing
        Set result1 = test_Case2.set_Difference(test_Case3);
        Set result2 = test_Case8.set_Difference(test_Case9);
        Set result3 = test_Case7.set_Difference(test_Case4);
        Set result4 = test_Case6.set_Difference(test_Case1);
        //Check whether the result is matched or not
        //if not match, t1 value is still 0
        if(!Arrays.equals(result1.set, (new String[]{"f"}))){
            System.out.println("Set_Difference Tests Failed");
        } else if (!Arrays.equals(result2.set, (new String[]{"cv", "cb"}))){
            System.out.println("Set_Difference Tests Failed");
        } else if (!Arrays.equals(result3.set, (new String[]{"o", "p", "g"}))){
            System.out.println("Set_Difference Tests Failed");
        } else if (!Arrays.equals(result4.set, (new String[]{"j", "k", "l"}))){
            System.out.println("Set_Difference Tests Failed");
        } else {
            //if match, then t3 value will be 1
            //And print out this program passed
            System.out.println("Set_Difference Tests Passed");
            t3 = 1;
        }
    }

    //Programs for checking set_Product is work well as expectations or not
    private static void test_Set_Product(){
        //Create new (set object) test results for unit testing
        Set result1 = test_Case2.set_Product(test_Case3);
        Set result2 = test_Case1.set_Product(test_Case9);
        Set result3 = test_Case4.set_Product(test_Case7);
        Set result4 = test_Case4.set_Product(test_Case1);
        //Expected Result for test cases
        String[] set1 = new String[]{"(s,s)", "(s,d)", "(s,a)", "(d,s)", "(d,d)", "(d,a)", "(f,s)", "(f,d)", "(f,a)"};
        String[] set2 = new String[]{"(a,as)", "(a,ad)", "(a,ag)", "(s,as)", "(s,ad)",
                                        "(s,ag)", "(d,as)", "(d,ad)", "(d,ag)", "(f,as)", "(f,ad)", "(f,ag)"};
        String[] set3 = new String[]{"(s,o)", "(s,p)", "(s,s)", "(s,d)", "(s,g)", "(a,o)", "(a,p)", "(a,s)", "(a,d)",
                "(a,g)", "(f,o)", "(f,p)", "(f,s)", "(f,d)", "(f,g)", "(d,o)", "(d,p)", "(d,s)", "(d,d)", "(d,g)"};
        String[] set4 = new String[]{"(s,a)", "(s,s)", "(s,d)", "(s,f)", "(a,a)", "(a,s)", "(a,d)", "(a,f)", "(f,a)",
                "(f,s)", "(f,d)", "(f,f)", "(d,a)", "(d,s)", "(d,d)", "(d,f)"};
        //Check whether the result is matched or not
        //if not match, t1 value is still 0
        if(!Arrays.equals(result1.set, (set1))){
            System.out.println("Set_Product Tests Failed");
        } else if (!Arrays.equals(result2.set, (set2))){
            System.out.println("Set_Product Tests Failed");
        } else if (!Arrays.equals(result3.set, (set3))){
            System.out.println("Set_Product Tests Failed");
        } else if (!Arrays.equals(result4.set, (set4))){
            System.out.println("Set_Product Tests Failed");
        } else {
            System.out.println("Set_Product Tests Passed");
            //if match, then t4 value will be 1
            //And print out this program passed
            t4 = 1;
        }
    }

    //Check program Is_Subset whether it works
    private static void test_Is_Subset(){
        if (test_Case2.is_SubSet(test_Case3)){
            System.out.println("Is_Subset Tests Failed");
        } else if (!test_Case3.is_SubSet(test_Case1)){
            System.out.println("Is_Subset Tests Failed");
        } else if (!test_Case1.is_SubSet(test_Case6)){
            System.out.println("Is_Subset Tests Failed");
        } else if (test_Case9.is_SubSet(test_Case10)){
            System.out.println("Is_Subset Tests Failed");
        } else {
            System.out.println("Is_Subset Tests Passed");
            t5 = 1;
        }
    }

    //check program Is_equal whether it works
    public static void test_Is_Equal(){
        if(test_Case9.is_Equal(test_Case8)){
            System.out.println("Is_Equal Tests Failed");
        } else if (test_Case4.is_Equal(test_Case5)){
            System.out.println("Is_Equal Tests Failed");
        } else if (test_Case3.is_Equal(test_Case6)){
            System.out.println("Is_Equal Tests Failed");
        } else if (test_Case2.is_Equal(test_Case7)){
            System.out.println("Is_Equal Tests Failed");
        } else {
            System.out.println("Is_Equal Tests Passed");
            t6 = 1;
        }
    }

    //Check program get_Count whether it works
    private static void test_Get_Count(){
        if(test_Case9.get_Count() != 3){
            System.out.println("Get_Count Tests Failed");
        } else if (test_Case10.get_Count() != 6){
            System.out.println("Get_Count Tests Failed");
        } else if (test_Case4.get_Count() != 4){
            System.out.println("Get_Count Tests Failed");
        } else if (test_Case7.get_Count() != 5){
            System.out.println("Get_Count Tests Failed");
        } else {
            System.out.println("Get_Count Tests Passed");
            t7 = 1;
        }
    }

    //Check program To_String whether it works
    private static void test_To_String(){
        if(!test_Case1.to_String().equals("{a, s, d, f}")){
            System.out.println("To_String Tests Failed");
        } else if (!test_Case2.to_String().equals("{s, d, f}")){
            System.out.println("To_String Tests Failed");
        } else if (!test_Case3.to_String().equals("{s, d, a}")){
            System.out.println("To_String Tests Failed");
        } else if (!test_Case4.to_String().equals("{s, a, f, d}")){
            System.out.println("To_String Tests Failed");
        } else {
            System.out.println("To_String Tests Passed");
            t8 = 1;
        }
    }
}
