//Jingze Dai, 400201059, daij24
//Date: 01/04/2020
import org.junit.*;
import static org.junit.Assert.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Check_AvaRoads{
    //Read files scanner and everything
    private File file = new File("data/connectedCities.txt");
    private Scanner Reader;
    private String[] Line_File;

    //Constructor for building objects
    public Check_AvaRoads() throws FileNotFoundException {
        Reader = new Scanner(file);
        List<String> lines = new ArrayList<>();

        while (Reader.hasNext()) {
            lines.add(Reader.nextLine());
        }
        Line_File = lines.toArray(new String[0]);
    }

    //Junit Test cases on the routes for different cities.
    @Test
    public void test_Route(){
        //Assumption is this assignment only allows directed explicit roads.
        String[] Route1 = {"Boston", "Minneapolis"};
        String[] Route2 = {"Boston", "New York City", "Pittsburgh", "Columbus", "Chicago", "Minneapolis"};
        String[] Route3 = {"Dallas", "Houston", "New Orleans"};
        String[] Route4 = {"New Orleans", "Memphis", "Jacksonville"};
        String[] Route5 = {"Chicago", "St. Louis", "Memphis"};
        String[] Route6 = {"Las Vegas", "Phoenix", "Albuquerque", "Denver"};
        assertFalse(check_route(Route1, Line_File));
        assertTrue(check_route(Route2, Line_File));
        assertTrue(check_route(Route3, Line_File));
        assertFalse(check_route(Route4, Line_File));
        assertTrue(check_route(Route5, Line_File));
    }

    //Check whether whole route is available
    private static boolean check_route(String[] Routes, String[] lines){
        for(int i = 0; i < Routes.length - 1; i++){
            if(!check_connected(Routes[i], Routes[i+1], lines)){
                return false;
            }
        }
        return true;
    }

    //Check whether one edge is available
    private static boolean check_connected(String City1, String City2, String[] Lines){
        int i = 0;
        while(i < Lines.length){
            if(Lines[i].contains(City1) && Lines[i].contains(City2)){
                return true;
            } else {
                i++;
            }
        }
        return false;
    }
}
