import java.time.LocalDate;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

class HomePlan extends Plan {
    static final String inputTag = "HOME_PLAN";
    private ArrayList<RangeCriterion> homeValueCriterion = new ArrayList<RangeCriterion>();
    private ArrayList<RangeCriterion> homeAgeCriterion = new ArrayList<RangeCriterion>();

    
    
    HomePlan(HashMap<String, ArrayList<Tag>> tags) {
        super(tags);       
        if (tags.get("HOME.VALUE") != null) {
        	ArrayList<Tag> T=tags.get("HOME.VALUE");
        	for(Tag t: T)
        	{
        		RangeCriterion temp=new RangeCriterion();
        		temp.addCriterion(t);
        		homeValueCriterion.add(temp);
        	}
            
        }
        if (tags.get("HOME.AGE") != null) {
           	ArrayList<Tag> T=tags.get("HOME.AGE");
        	for(Tag t: T)
        	{
        		RangeCriterion temp=new RangeCriterion();
        		temp.addCriterion(t);
        		homeAgeCriterion.add(temp);
        	}
            
        }
    }

    @Override
    boolean isEligible(Insurable insurable, Date date) {
        if (!(insurable instanceof Home))
            return false;
        Home home = (Home) insurable;
        for(RangeCriterion temp: homeValueCriterion)        	
        	if (!temp.isInRange(home.getValue()))
        		return false;

        // Extracting the age of the home
        LocalDate localCurrentDate = date.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate localBuiltDate = home.getBuildDate().toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        long age = localCurrentDate.getYear() - localBuiltDate.getYear();
        //If the build date in month has not been passed then we make it -1
        if(localCurrentDate.getMonthValue()<localBuiltDate.getMonthValue())
        	age--;
        else if(localCurrentDate.getMonthValue()==localBuiltDate.getMonthValue())
        {
            //If thr day is not passed then we make it -1
              if(localCurrentDate.getDayOfMonth()<localBuiltDate.getDayOfMonth())
            	  age--;
        }
        
        // Checking if the age is in the range.
        for(RangeCriterion temp: homeAgeCriterion)        
           if (!temp.isInRange(age))
           		return false;
        
        return true;
    }

    @Override
    ArrayList<? extends Insurable> getInsuredItems(Customer customer, Database database) {
        return database.getHomesByOwnerName(customer.getName());
    }

    @Override
    Insurable getInsuredItem(String insurableID, Database database) {
        return database.getHomeByPostalCode(insurableID);
    }
}
