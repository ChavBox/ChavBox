/* 
#  Name: Charlie Havener
#  Date: 11/1/2023
#  Description: A pocket class that can hold BackpackItems
*/ 
import java.util.ArrayList;
import java.util.Iterator;

public class Pocket implements Iterable<BackpackItem>{
	//Fields
	private String pocketName;
	private int maxPocketWeight;
    private ArrayList<BackpackItem> pocketItems;
    
    //Constructors
    public Pocket(String pocketName, int maxPocketWeight){
    	this.pocketName = pocketName;
        this.maxPocketWeight = maxPocketWeight;
        pocketItems = new ArrayList<BackpackItem>();
    }
    
    //Methods
	public void insertItemInPocket(String itemName, double itemWeight) throws Exception{
		if(itemWeight < 0){
            throw new Exception("Item weight cannot be negative", new Throwable("Insert"));
        }else if(getPocketTotalWeight() + itemWeight > maxPocketWeight){
            throw new Exception("Item would exceed  " + pocketName + "'s maximum pocket weight", new Throwable("Insert"));
        }else{
            pocketItems.add(new BackpackItem(itemName, itemWeight));
        }
    }
    
    public void removeItemFromPocket(String itemName) throws Exception{
    	
    }
    
    public double getPocketTotalWeight(){
    	double totalWeight = 0;
    	
    	
    	
        return totalWeight;
    }
    
    public void listItemsInPocket(){
    	System.out.println("Listing " + pocketName + " Pocket Items..." );
    	
    	
    }

	public Iterator<BackpackItem> iterator() {
		return pocketItems.iterator();
	}
}
