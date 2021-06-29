import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

class Customer {
    private String name;
    private Date dateOfBirth;
    private long income;
    //build a new kind of database
    private Database database;
    static final String inputTag = "CUSTOMER";

    //HashMap Method by using .get(0) to define initial value of different variables
    Customer(HashMap<String, ArrayList<Tag>> tags, Database db) throws ParseException {
    	database=db;
        name = tags.get("NAME").get(0).getValue();
        dateOfBirth = Utils.convertDate(tags.get("DATE_OF_BIRTH").get(0).getValue());
        income = Long.parseLong(tags.get("INCOME").get(0).getValue());
    }
    //Methods for getting values on different variables
    public String getName() {
        return name;
    }

    public Date getDateOfBirth() {
        return dateOfBirth;
    }

    public long getIncome() {
        return income;
    }

    public static String getInputTag() {
        return inputTag;
    }
    
    public long getWealth()
    {
    	return database.getCustomerWealth(name);
    }
}
