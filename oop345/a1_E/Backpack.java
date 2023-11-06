import java.util.Iterator;

public class Backpack implements Iterable<Pocket>, Iterator<Pocket> 
{
    //Constants
    private final static int MAIN_POCKET_MAX_WEIGHT = 10;
    private final static int LEFT_POCKET_MAX_WEIGHT = 5;
    private final static int RIGHT_POCKET_MAX_WEIGHT = 5;
    private final int POCKET_QUANTITY = 3;

    //Fields
    private Pocket mainPocket;
    private Pocket rightPocket;
    private Pocket leftPocket;

    private int currentIteratingPocket = 0;
    
    //Constructors
    public Backpack()
    {
        this(MAIN_POCKET_MAX_WEIGHT, RIGHT_POCKET_MAX_WEIGHT, LEFT_POCKET_MAX_WEIGHT);
    }
    
    public Backpack(int mainPocketMaxWeight, int rightPocketMaxWeight, int leftPocketMaxWeight)
    {
    	
    }

    //Methods
    public void insertItemInMainPocket(String itemName, double itemWeight) throws Exception
    {
        
    }
    
    public void insertItemInRightPocket(String itemName, double itemWeight) throws Exception
    {
    	
    }
    
    public void insertItemInLeftPocket(String itemName, double itemWeight) throws Exception
    {
    	
    }
    
    public void removeItemFromMainPocket(String itemName) throws Exception
    {
    	
    }
    
    public void removeItemFromRightPocket(String itemName) throws Exception
    {
    	
    }
    
    public void removeItemFromLeftPocket(String itemName) throws Exception
    {
    	
    }
    
    public void listItemsInMainPocket()
    {
    	
    }
    
    public void listItemsInRightPocket()
    {
    	
    }
    
    public void listItemsInLeftPocket()
    {
    	
    }
    
    public double getMainPocketTotalWeight()
    {
    	double totalWeight = 0;
    	
        return totalWeight;
    }
    
    public double getRightPocketTotalWeight()
    {
    	double totalWeight = 0;
    	
        return totalWeight;
    }
    
    public double getLeftPocketTotalWeight()
    {
    	double totalWeight = 0;
    	
        return totalWeight;
    }
    
    public void listItemsInBackpack()
    {
    	System.out.println("Listing all backpack items...\n");
    	
    	
    }
    
    public double getTotalWeight()
    {
    	double totalWeight = 0;
    	

    	
        return totalWeight;
    }

    public boolean hasNext() 
    {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'hasNext'");
    }

    public Pocket next() 
    {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'next'");
    }

    public Iterator<Pocket> iterator() 
    {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'iterator'");
    }

    public boolean equals(Object other)
	{
		boolean result = false;

		
		return result;
	}

    public Object clone()
	{
        Backpack clone = null;

        

        return clone;
    }
}
