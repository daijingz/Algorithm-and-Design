//Here we import new array list for home HashMap method
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

class Home extends Insurable {
    private String postalCode;
    private Date buildDate;

    static final String inputTag = "HOME";

    Home(HashMap<String, ArrayList<Tag>> tags) throws ParseException {
        super(tags);
        //Adding .get(0) for getting value of postal code or build date and put them into variable
        postalCode = tags.get("POSTAL_CODE").get(0).getValue();
        buildDate = Utils.convertDate(tags.get("BUILD_DATE").get(0).getValue());
    }

    public String getPostalCode() {
        return postalCode;
    }

    public Date getBuildDate() {
        return buildDate;
    }

    public static String getInputTag() {
        return inputTag;
    }
}
