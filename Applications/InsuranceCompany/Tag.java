class Tag {
    public enum Relation {
        SMALLER, LARGER, EQUAL
    }
    private Relation relation;
    private String name;
    private String value;

    Tag(String[] tokens) {
        name = tokens[0];

        switch (tokens[1].charAt(0)) {
            case '<':
                relation = Relation.SMALLER;
                break;
            case '>':
                relation = Relation.LARGER;
                break;
            case '=':
                relation = Relation.EQUAL;
                break;
            default:
                throw new BadCommandException("Invalid tag: ill-defined bad relation.");
        }
        value = tokens[2];
    }

    public Relation getRelation() {
        return relation;
    }

    public String getName() {
        return name;
    }

    public String getValue() {
        return value;
    }
}
