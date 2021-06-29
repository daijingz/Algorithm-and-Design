class RangeCriterion {
    private long maxValue = Long.MAX_VALUE;
    private long minValue = Long.MIN_VALUE;

    void addCriterion(Tag tag) {
        if (tag.getRelation() == Tag.Relation.LARGER) {
            minValue = Math.max(minValue, Long.parseLong(tag.getValue()));
        }
        if (tag.getRelation() == Tag.Relation.SMALLER) {
            maxValue = Math.min(maxValue, Long.parseLong(tag.getValue()));
        }
    }

    boolean isInRange(long value) {
        if (value < maxValue && value > minValue)
            return true;
        return false;
    }
}
