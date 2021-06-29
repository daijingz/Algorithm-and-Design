import java.text.ParseException;

abstract class Command {
    abstract void run(Database database) throws ParseException;
}
