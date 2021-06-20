/*      Student Information
 *       -------------------
 *       Student Name: Dai, Jingze
 *       Student Number: 400201059
 *       Course Code: CS/SE 2XB3
 *       Lab Section: L03
 *
 *       I attest that the following code being submitted is my own individual work
 */
//Import Array and ArrayList tools
import java.util.Arrays;
import java.util.ArrayList;

public class Set {
    // Two kinds of different Object data: set for containing elements' set and count for elements' amount.
    String[] set;
    private int count = 0;

    // Constructor: User Input will be the string-typed array
    // At first when object created, this program builds a new array and then put all input elements to this array
    // At the same time, it counts for how many elements it has and store this number into variable count
    public Set(String[] input) {
        this.set = new String[input.length];
        for(int num = 0; num < input.length; num++){
            this.set[num] = input[num];
            count += 1;
        }
    }
    // Main Classes for Program Developer (Internal Testing is not available for readers and users)
    // To see Unit Testing Classes Please see Test_Set.java in the same folder
    public static void main(String[] args){
        // Create Two Set Objects here for internal Testing.
        Set test1 = new Set(new String[]{"a", "s", "d", "f"});
        Set test2 = new Set(new String[]{"s", "d", "f"});
        // Testing for all programs (Including external, un-required programs)
        System.out.println(test1.to_String());
        System.out.println(test2.to_String());
        System.out.println(test1.get_Count());
        System.out.println(test1.set_Contains("6"));
        System.out.println(test1.is_SubSet(test2));
        System.out.println(test1.is_Equal(test2));
        System.out.println(test1.set_Union(test2).to_String());
        System.out.println(test1.set_Intersection(test2).to_String());
        System.out.println(test1.set_Difference(test2).to_String());
        System.out.println(get_Coordinate("1","2"));
        System.out.println(test1.set_Product(test2).to_String());
    }

    //Set_Union method for getting union set of two sets
    public Set set_Union(Set input){
        //First we build an empty ArrayList then we put one set (current object) all element into this ArrayList
        ArrayList<String> elements_Set = new ArrayList<>(Arrays.asList(this.set).subList(0, this.count));
        //Then we use a loop, if an element in Input Object has already in this ArrayList, then we do nothing
        //Else, put the element inside ArrayList
        for (int i2 = 0; i2 < input.count; i2++){
            if(!this.set_Contains(input.set[i2])){
                elements_Set.add(input.set[i2]);
            }
        }
        //Then we build a new array for Output
        String[] Output = new String[elements_Set.size()];
        //We cannot output ArrayList, so we put everything inside this array
        for(int i3 = 0; i3 < elements_Set.size(); i3++){
            Output[i3] = elements_Set.get(i3);
        }
        //Then we use array that has all elements to build a set object and output it
        return new Set(Output);
    }

    //Set_Intersection Method for getting intersection sets in the
    public Set set_Intersection (Set input){
        //First build an new empty ArrayList for storing elements
        ArrayList<String> elements_Set = new ArrayList<>();
        //First we take a look at every element in the current object's set
        //If Input Object contains selected elements (both exists), then we put it into ArrayList
        for (int i4 = 0; i4 < this.count; i4++){
            if (input.set_Contains(this.set[i4])){
                elements_Set.add(this.set[i4]);
            }
        }
        //Then we put all elements in the new built array
        String[] Output = new String[elements_Set.size()];
        for (int i5 = 0; i5 < elements_Set.size(); i5++){
            Output[i5] = elements_Set.get(i5);
        }
        //When we get the output set, we use it to build an set object and output it
        return new Set(Output);
    }
    //Program set_difference for getting difference sets for two sets
    public Set set_Difference (Set input){
        //First build an new empty ArrayList for storing elements
        ArrayList<String> elements_Set = new ArrayList<>();
        //First we take a look at every element in the current object's set
        //If Input Object does not contain selected elements (another not exist), then we put it into ArrayList
        for (int i6 = 0; i6 < this.count; i6++){
            if (!input.set_Contains(this.set[i6])){
                elements_Set.add(this.set[i6]);
            }
        }
        //Then we put all ArrayList elements into new built arrays
        String[] Output = new String[elements_Set.size()];
        for (int i7 = 0; i7 < elements_Set.size(); i7++){
            Output[i7] = elements_Set.get(i7);
        }
        //After we build a new array we use it as input into building a new set object and return it
        return new Set(Output);
    }
    //Set product program for getting Cartesian product
    public Set set_Product(Set Input){
        //length for output product's set length
        int length = this.count * Input.count;
        //index shows the position (index) of the loop
        int index = 0;
        //Build a new array for set product
        String[] elements_Set = new String[length];
        //Nested Loop: calculating all its Cartesian Products and insert them into new array
        for(int j1 = 0; j1 < this.count; j1++){
            for(int j2 = 0; j2 < Input.count; j2++){
                elements_Set[index] = get_Coordinate(this.set[j1],Input.set[j2]);
                index += 1;
            }
        }
        //After getting an array for all elements in cartesian product, we use it to build an set object and output it
        return new Set(elements_Set);
    }
    //Subset program for checking whether current object is the subset of Input set object
    public boolean is_SubSet(Set Input){
        //build integer count to record how many elements in current object are included into
        int count = 0;
        //loops for check how many elements are included into
        for (int k1 = 0; k1 < this.count; k1 ++){
            if (Input.set_Contains(this.set[k1]) && this.set[k1] != null){
                count += 1;
            }
        }
        //Check whether all elements in the current object are included into Input object
        return count == this.count;
    }

    //is_Equal function for checking whether two sets are equal
    //If set 1 is the subset of set 2, and set 2 is subset of set 1, then set 1 equals set 2
    //Return true if equals, else return false
    public boolean is_Equal(Set Input){
        return this.is_SubSet(Input) && Input.is_SubSet(this);
    }

    //Check how many elements in the set object
    //Return integer amounts
    public int get_Count(){
        return this.count;
    }

    //to_String method for returning a new String for an given array
    //Return String form of those set objects
    public String to_String(){
        //For the requirement, we should print out a string with
        String output = Arrays.toString(this.set).replace("[","").replace("]","");
        return "{" + output + "}";
    }

    //Reminder: This is an extra method!!!
    //check whether element a is included into a set object
    //If yes, return true, else return false
    private boolean set_Contains(String Input){
        for (String s : this.set) {
            if (Input.equals(s)) {
                return true;
            }
        }
        return false;
    }
    //Reminder: This is an extra method!!!
    //For getting Cartesian Product, we need to get cartesian product's coordinate
    private static String get_Coordinate(String Input1, String Input2){
        return "(" + Input1 + "," + Input2 + ")";
    }
}
