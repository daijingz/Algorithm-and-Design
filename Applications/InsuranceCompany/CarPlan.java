import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

class CarPlan extends Plan {
    static final String inputTag = "CAR_PLAN";
    ArrayList<RangeCriterion> mileageCriterion = new ArrayList<>();

    CarPlan(HashMap<String, ArrayList<Tag>> tags) {
        super(tags);
        if (tags.get("CAR.MILEAGE") != null) {
        	ArrayList<Tag> T = tags.get("CAR.MILEAGE");
        	//This loop we used to create and add new Criterion
        	for(Tag t: T) {
        		RangeCriterion temp = new RangeCriterion();
        		temp.addCriterion(t);
        		mileageCriterion.add(temp);
        	}
        }
    }

    @Override
    boolean isEligible(Insurable insurable, Date date) {
        //check whether is is instance of Car
        if (!(insurable instanceof Car)) {
            return false;
        }
        Car ca_R = (Car) insurable;
        //check whether tmp is in the range, if not in the range return false
        for (RangeCriterion tmp: mileageCriterion) {
        	if(!tmp.isInRange(ca_R.getMileage())){
        	    return false;
            }
        } //otherwise it returns true
        return true;
    }

    @Override
    ArrayList<? extends Insurable> getInsuredItems(Customer customer, Database database) {
        return database.getCarsByOwnerName(customer.getName());
    }

    @Override
    Insurable getInsuredItem(String insurableID, Database database) {
        return database.getCarByPlateNumber(insurableID);
    }

}
