import java.time.LocalDate;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

abstract class Plan {
    String name;
    long premium;
    long maxCoveragePerClaim;
    long deductible;
    ArrayList<RangeCriterion> customerAgeCriterion = new ArrayList<>();
    ArrayList<RangeCriterion> customerIncomeCriterion = new ArrayList<>();
    //Build a new array list for storing data on customer's possessions.
    ArrayList<RangeCriterion> custmerWealthCriterion = new ArrayList<>();
    
    Plan(HashMap<String, ArrayList<Tag>> tags) {
        //Moving all non-empty "CUSTOMER.WEALTH" objects to array list T
    	if(tags.get("CUSTOMER.WEALTH") != null) {
        	ArrayList<Tag> Tag1 = tags.get("CUSTOMER.WEALTH");
        	for(Tag t: Tag1) {
        		RangeCriterion temp = new RangeCriterion();
        		temp.addCriterion(t);
        		custmerWealthCriterion.add(temp);
        	}
        }
        name = tags.get("NAME").get(0).getValue();
        premium = Integer.parseInt(tags.get("PREMIUM").get(0).getValue());
        maxCoveragePerClaim = Integer.parseInt(tags.get("MAX_COVERAGE_PER_CLAIM").get(0).getValue());
        deductible = Integer.parseInt(tags.get("DEDUCTIBLE").get(0).getValue());

        //These are steps checking whether "CUSTOMER.AGE" and "CUSTOMER.INCOME" is empty or not, for the not empty one
        if (tags.get("CUSTOMER.AGE") != null) {
        	ArrayList<Tag> T=tags.get("CUSTOMER.AGE");
        	for(Tag t: T) {
        		RangeCriterion temp = new RangeCriterion();
        		temp.addCriterion(t);
        		customerAgeCriterion.add(temp);
        	}
        	            
        }
        if (tags.get("CUSTOMER.INCOME") != null) {
        	ArrayList<Tag> T = tags.get("CUSTOMER.INCOME");
        	for(Tag t: T) {
        		RangeCriterion temp = new RangeCriterion();
        		temp.addCriterion(t);
        		customerIncomeCriterion.add(temp);
        	}
        }

    }

    abstract boolean isEligible(Insurable insurable, Date date);

    abstract ArrayList<? extends Insurable> getInsuredItems(Customer customer, Database database);

    abstract Insurable getInsuredItem(String insurableID, Database database);

    boolean isEligible(Customer customer, Date currentDate) {
        // Extracting the age of the customer
        LocalDate localCurrentDate = currentDate.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate localBirthDate = customer.getDateOfBirth().toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        long age = localCurrentDate.getYear() - localBirthDate.getYear();

        // As the same for last class, it check month and day
        // If the month or day has not been passed, then the age should be - 1 because not a whole year
        if (localCurrentDate.getMonthValue() < localBirthDate.getMonthValue()) {
            age--;
        } else if (localCurrentDate.getMonthValue() == localBirthDate.getMonthValue()) {
            if (localCurrentDate.getDayOfMonth() < localBirthDate.getDayOfMonth()) {
                age--;
            }
        }
        // Check if the age is in the range, if not then return false
        for (RangeCriterion tmp : customerAgeCriterion){
            if (!tmp.isInRange(age)){
                return false;
            }
        }
        // Check if the income is in the range, if not then return false
        for(RangeCriterion tmp: customerIncomeCriterion) {
            if (!tmp.isInRange(customer.getIncome())) {
                return false;
            }
        }
        // Check if the wealth is in the range, if not then return false
        long wealth=customer.getWealth();
        for(RangeCriterion tmp: custmerWealthCriterion) {
            if (!tmp.isInRange(wealth)){
                return false;
            }
        }
        return true;
    }

    String getName() {
        return name;
    }

    long getPremium() {
        return premium;
    }

    long getMaxCoveragePerClaim() {
        return maxCoveragePerClaim;
    }

    long getDeductible() {
        return deductible;
    }
}
