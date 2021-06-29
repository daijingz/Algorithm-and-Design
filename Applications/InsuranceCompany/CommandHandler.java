import java.text.ParseException;

class CommandHandler {
    Database database;

    CommandHandler(Database database) {
        this.database = database;
    }

    void run(Command command) throws ParseException {
        command.run(database);
    }
}
