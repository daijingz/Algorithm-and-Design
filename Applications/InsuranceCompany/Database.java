import java.util.ArrayList;

class Database {
    private ArrayList<Customer> customers = new ArrayList<>();
    private ArrayList<Home> homes = new ArrayList<>();
    private ArrayList<Car> cars = new ArrayList<>();
    private ArrayList<Plan> plans = new ArrayList<>();
    private ArrayList<Contract> contracts = new ArrayList<>();
    private ArrayList<Claim> claims = new ArrayList<>();
    //As we did before, build a new kind of array list for companies
    private ArrayList<Company> companies =new ArrayList<>();

    //Same method for adding a company to the array list
    void insertCompany(Company company){
    	companies.add(company);
    }
    
    void insertHome(Home home) {
        homes.add(home);
    }

    void insertCar(Car car) {
        cars.add(car);
    }

    void insertCustomer(Customer customer) {
        customers.add(customer);
    }

    void insertPlan(Plan plan) {
        plans.add(plan);
    }

    void insertClaim(Claim claim) {
        claims.add(claim);
    }

    void insertContract(Contract contract) {
        contracts.add(contract);
    }

    Plan getPlan(String name) {
        for (Plan plan : plans) {
            if (plan.name.equals(name))
                return plan;
        }
        return null;
    }

    Customer getCustomer(String name) {
        for (Customer customer : customers) {
            if (customer.getName().equals(name))
                return customer;
        }
        return null;
    }

    Contract getContract(String name) {
        for (Contract contract : contracts) {
            if (contract.getContractName().equals(name))
                return contract;
        }
        return null;
    }

    //Because a person may have many homes, so they need to use the program to get list of homes
    ArrayList<Home> getHomesByOwnerName(String ownerName) {
        ArrayList<Home> result = new ArrayList<>();
        for (Home home : homes) {
            if (home.getOwnerName().equals(ownerName))
                result.add(home);
        }
        return result;
    }

    //Because a person may have many cars, so they need to use the program to get list of cars
    ArrayList<Car> getCarsByOwnerName(String ownerName) {
        ArrayList<Car> result = new ArrayList<>();
        for (Car car : cars) {
            if (car.getOwnerName().equals(ownerName)) {
                result.add(car);
            }
        }
        return result;
    }

    long totalClaimAmountByCustomer(String customerName) {
        long totalClaimed = 0;
        for (Claim claim : claims) {
            if (getContract(claim.getContractName()).getCustomerName().equals(customerName))
                totalClaimed += claim.getAmount();
        }
        return totalClaimed;
    }

    long totalReceivedAmountByCustomer(String customerName) {
        long totalReceived = 0;
        for (Claim claim : claims) {
            Contract contract = getContract(claim.getContractName());
            if (contract.getCustomerName().equals(customerName)) {
                if (claim.wasSuccessful()) {
                    long deductible = getPlan(contract.getPlanName()).getDeductible();
                    totalReceived += Math.max(0, claim.getAmount() - deductible);
                }
            }
        }
        return totalReceived;
    }

    Insurable getCarByPlateNumber(String insurableID) {
        for (Car car : cars) {
            if (car.getPlateNumber().equals(insurableID))
                return car;
        }
        return null;
    }

    Insurable getHomeByPostalCode(String insurableID) {
        for (Home home : homes) {
            if (home.getPostalCode().equals(insurableID))
                return home;
        }
        return null;
    }
    
    //Here is a program for counting how much money does a person has
    long getCustomerWealth(String customerName) {
        //Initial value of wealth is 0
    	long Pos_Peo=0;
    	//Using a loop to find all homes' values and added to Pos_Peo
    	for(Home h: homes) {
    		if(h.getOwnerName().equals(customerName)) {
                Pos_Peo += h.getValue();
            }
    	}
        //Using a loop to find all cars' values and added to Pos_Peo
    	for(Car h: cars) {
    		if(h.getOwnerName().equals(customerName)) {
                Pos_Peo += h.getValue();
            }
    	}
        //Using a loop to find all companies' values and added to Pos_Peo
        for(Company h: companies) {
        	if(h.getOwnerName().equals(customerName)) {
        	    //Because calculating companies' values need more calculation so we use next program
        		Pos_Peo += getCompanyWealth(h);
    		}
        }
    	
    	return Pos_Peo;
    }
    
    //This is a program calculates how much money a company counts
    long getCompanyWealth(Company company) {
        //First we find input amount of money that a company has
    	long Pos_Com=company.getValue();
    	String Com_Name = company.getCompanyName();
    	//If a company is a son-company for another company, then we will add the value to the mother company
    	for(Company h: companies) {
    		if(h.getOwnerName().equals(Com_Name)) {
    			Pos_Com+=getCompanyWealth(h);
    		}
    	}
    	return Pos_Com;
    }
}
