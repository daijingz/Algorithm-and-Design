import java.text.ParseException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Date;
import java.text.SimpleDateFormat;


public class Main {
    public static void main(String[] args) {
        try {
            InputReader inputReader = InputReader.getInstance();
            ArrayList<Command> commands = inputReader.getCommands();
            Iterator<Command> currentCommand = commands.iterator();

            CommandHandler commandHandler = new CommandHandler(new Database());

            while (currentCommand.hasNext()) {
                commandHandler.run(currentCommand.next());
            }
        } catch (ParseException e) {
            System.out.println(e.getMessage());
        } catch (BadCommandException e) {
            System.out.println(e.getMessage());
        }
    }
}

class Utils {

    private static SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");

    static Date convertDate(String input) throws ParseException {
        return formatter.parse(input);
    }
    static String formattedDate(Date date) {
        String pattern = "yyyy-MM-dd";
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat(pattern);
        return simpleDateFormat.format(date);
    }
}
