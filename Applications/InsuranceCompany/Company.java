//We import ArrayList, parse exception and HashMap tools
import java.text.ParseException;
import java.util.ArrayList;
import java.util.HashMap;

//For calculating possession of people that owns a company, we build a new class called
public class Company {
	//Variables for company information: owner's name, company's name and value
	private String ownerName;
	private String companyName;
	private long value;
	//Give a tag for information in this class: "COMPANY"
	static final String inputTag = "COMPANY";

	// Similar with Car and Home, they get value of one part
	Company(HashMap<String, ArrayList<Tag>> tags) throws ParseException {
		ownerName = tags.get("OWNER_NAME").get(0).getValue();
		companyName = tags.get("COMPANY_NAME").get(0).getValue();
		value = Long.parseLong(tags.get("VALUE").get(0).getValue());
    }

    //Methods for returning owner name, company name and value
	public String getOwnerName() {
		return ownerName;
	}

	public String getCompanyName() {
		return companyName;
	}

	public long getValue() {
		return value;
	}
	
	
}
