import java.util.ArrayList;
import java.util.HashMap;

class Insurable {
    protected String ownerName;
    protected long value;
    // .get(0) make this into one part of the program and it was put into new variables
    Insurable(HashMap<String, ArrayList<Tag>> tags) {
        ownerName = tags.get("OWNER_NAME").get(0).getValue();
        value = Long.parseLong(tags.get("VALUE").get(0).getValue());
    }

    public String getOwnerName() {
        return ownerName;
    }

    public long getValue() {
        return value;
    }
}
