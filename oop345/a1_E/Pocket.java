import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class Pocket implements Iterable<BackpackItem>
{
	//Fields
	private String pocketName;
	private int maxPocketWeight;
    private List<BackpackItem> pocketItems;
    
    //Constructors
    public Pocket(String pocketName, int maxPocketWeight)
    {
    	
    }
    
    //Methods
	public void insertItemInPocket(String itemName, double itemWeight) throws Exception
    {
		
    }
    
    public void removeItemFromPocket(String itemName) throws Exception
    {
    	
    }
    
    public double getPocketTotalWeight()
    {
    	double totalWeight = 0;
    	
    	
    	
        return totalWeight;
    }
    
    public void listItemsInPocket()
    {
    	System.out.println("Listing " + pocketName + " Pocket Items..." );
    	
    	
    }

	public Iterator<BackpackItem> iterator() 
	{
		return pocketItems.iterator();
	}

	public boolean equals(Object other)
	{
		boolean result = false;


		return result;
	}

	public Object clone()
	{
		Pocket clone = null;
	
		return clone;
	}
}
