import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
public class TestSort extends Sort{
    private int[] test1;

    @Before
    public void Set_up(){
        test1 = new int[]{ 1, 2, 5 };
    }

    @Test
    public void Test_Selection_Sort(){
        assertEquals(1.0, SelectionSort(test1)[0]);
    }
}