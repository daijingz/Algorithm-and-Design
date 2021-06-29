import java.text.ParseException;

class PrintCommand extends Command {
    private String entityType;
    private String queryType;
    private String queryValue;

    PrintCommand(String[] tokens) {
        super();
        entityType = tokens[1];
        queryType = tokens[2];
        queryValue = tokens[3];
    }

    @Override
    void run(Database database) {
        if (entityType.equals("CUSTOMER"))
            runPrintCustomer(database);
        else if (entityType.equals("PLAN"))
            runPrintPlan(database);
        else {
            throw new BadCommandException("Bad print command.");
        }
    }

    private void runPrintCustomer(Database database) {
        if (queryType.equals("TOTAL_CLAIMED")) {
            System.out.println("Total amount claimed by " + database.getCustomer(queryValue).getName() +
                    " is " + database.totalClaimAmountByCustomer(queryValue));
        } else if (queryType.equals("TOTAL_RECEIVED")) {
            System.out.println("Total amount received by " + database.getCustomer(queryValue).getName() +
                            " is " + database.totalReceivedAmountByCustomer(queryValue));
        }
    }

    //TODO
    private void runPrintPlan(Database database) {
        System.out.println("PRINT PLAN feature is not yet implemented.");
    }
}
