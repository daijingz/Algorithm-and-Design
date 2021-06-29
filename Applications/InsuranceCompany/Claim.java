import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

class Claim {
    private String contractName;
    private long amount;
    private Date date;
    private boolean successful;
    private String InsurableID;

    static final String inputTag = "CLAIM";

    Claim(HashMap<String, ArrayList<Tag>> tags) throws ParseException {
    	//only one part is extracted and put into different values
        contractName = tags.get("CONTRACT_NAME").get(0).getValue();
        InsurableID = tags.get("INSURABLE_ID").get(0).getValue();
        date = Utils.convertDate(tags.get("DATE").get(0).getValue());
        amount = Long.parseLong(tags.get("AMOUNT").get(0).getValue());
    }

    public String getContractName() {
        return contractName;
    }

    public long getAmount() {
        return amount;
    }

    public Date getDate() {
        return date;
    }

    public boolean wasSuccessful() {
        return successful;
    }

    public void setSuccessful(boolean successful) {
        this.successful = successful;
    }

    public String getInsurableID() {
        return InsurableID;
    }
}
