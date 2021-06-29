import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

class Car extends Insurable {

    private String make;
    private String model;
    private Date purchaseDate;
    private String plateNumber;
    private long mileage;

    static final String inputTag = "CAR";

    Car(HashMap<String, ArrayList<Tag>> tags) throws ParseException {
        super(tags);
        //Find first part of the string inputs and put them into variables
        make = tags.get("MAKE").get(0).getValue();
        model = tags.get("MODEL").get(0).getValue();
        plateNumber = tags.get("PLATE_NUMBER").get(0).getValue();
        purchaseDate = Utils.convertDate(tags.get("PURCHASE_DATE").get(0).getValue());
        mileage = Long.parseLong(tags.get("MILEAGE").get(0).getValue());
    }

    public String getOwnerName() {
        return ownerName;
    }

    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public Date getPurchaseDate() {
        return purchaseDate;
    }

    public long getMileage() {
        return mileage;
    }

    public static String getInputTag() {
        return inputTag;
    }

    public String getPlateNumber() {
        return plateNumber;
    }
}

