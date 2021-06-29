import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

class Contract {
    private String contractName;
    private String customerName;
    private String planName;
    private Date startDate;
    private Date endDate;

    static final String inputTag = "CONTRACT";
    //Adding a method .get(0) to get one part of string input
    Contract(HashMap<String, ArrayList<Tag>> tags) throws ParseException {
        contractName = tags.get("CONTRACT_NAME").get(0).getValue();
        customerName = tags.get("CUSTOMER_NAME").get(0).getValue();
        planName = tags.get("PLAN_NAME").get(0).getValue();
        startDate = Utils.convertDate(tags.get("START_DATE").get(0).getValue());
        endDate = Utils.convertDate(tags.get("END_DATE").get(0).getValue());
    }
    //Methods for returning different data
    public String getCustomerName() {
        return customerName;
    }

    public String getPlanName() {
        return planName;
    }

    public Date getStartDate() {
        return startDate;
    }

    public Date getEndDate() {
        return endDate;
    }

    public String getContractName() {
        return contractName;
    }
}
