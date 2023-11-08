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
    	boolean itemExists = false;
        for(int i = 0; i < pocketItems.size(); i++){
            if(pocketItems.get(i).itemName == itemName){
                itemExists = true;
                pocketItems.remove(i);
                break;
            }
        }

        if(!itemExists){
            throw new Exception(itemName + " is not in this Pocket", new Throwable("Remove"));
        }
    }
    
    public double getPocketTotalWeight(){
    	double totalWeight = 0;
    	for(BackpackItem i: pocketItems){
            totalWeight += i.itemWeight;
        }
    	
        return totalWeight;
    }
    
    public void listItemsInPocket(){
    	System.out.println("Listing " + pocketName + " Pocket Items..." );
    	for(BackpackItem i: pocketItems){
            System.out.println(i.itemName + " " + i.itemWeight);
        }
    }

	public Iterator<BackpackItem> iterator() {
		return pocketItems.iterator();
	}
}
