/* 
#  Name: Charlie Havener
#  Date: 11/7/2023
#  Description: A pocket class that can hold BackpackItems
*/ 
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class Pocket implements Iterable<BackpackItem> {
	//Fields
	private String pocketName;
	private int maxPocketWeight;
  private List<BackpackItem> pocketItems;
    
  //Constructors
  public Pocket(String pocketName, int maxPocketWeight){
    	
  }
    
  //Methods

	/*       
	 # Description: creates and adds a BackpackItem to pocketItems if it is a valid item.
   # 
   # Parameters: 
	 #	 String itemName: the name of the item to be inserted
	 #	 double itemWeight: the weight of the item to be inserted
   # 
   # Returns Value: none
	*/
	public void insertItemInPocket(String itemName, double itemWeight) throws Exception {
		if(itemWeight < 0){
        throw new Exception("Item weight cannot be negative", new Throwable("Insert"));
    }else if(getPocketTotalWeight() + itemWeight > maxPocketWeight){
      throw new Exception("Item would exceed  " + pocketName + "'s maximum pocket weight", new Throwable("Insert"));
    }else{
      pocketItems.add(new BackpackItem(itemName, itemWeight));
    }
  }
    
	/*       
	 # Description: removes a BackpackItem from pocketItems if it is in the pocket.
   # 
   # Parameters: 
	 #	 String itemName: the name of the item to be removed
   # 
   # Returns Value: none
	*/
  public void removeItemFromPocket(String itemName) throws Exception{
  	boolean itemExists = false;
    for(int i = 0; i < pocketItems.size(); i++){
      if(pocketItems.get(i).itemName == itemName){
        itemExists = true;
        pocketItems.remove(i);
        break;
      }
    }

    if(!itemExists){throw new Exception(itemName + " is not in this Pocket", new Throwable("Remove"));}
  }
    
	/*       
	 # Description: sums the total weight of all BackpackItems in the pocket
   # 
   # Parameters: none
   # 
   # Returns Value: double
	*/
  public double getPocketTotalWeight() {
    double totalWeight = 0;
    for(BackpackItem i: pocketItems){
      totalWeight += i.itemWeight;
    }
    	
    return totalWeight;
  }
    
	/*       
	 # Description: Prints each items name along with it's weight contained in the pocket
   # 
   # Parameters: none
   # 
   # Returns Value: none
	*/
  public void listItemsInPocket(){
    System.out.println("Listing " + pocketName + " Pocket Items..." );
    for(BackpackItem i: pocketItems){
      System.out.println(i.itemName + " " + i.itemWeight);
		}	
  }

	/*       
	 # Description: creates an iterator for the pocket
   # 
   # Parameters: none
   # 
   # Returns Value: Iterator<BackpackItem>
	*/
	public Iterator<BackpackItem> iterator() {
		return pocketItems.iterator();
	}

	/*       
	# Description: checks to see if two pockets contain the same items
    # 
    # Parameters: Pocket
    # 
    # Returns Value: boolean
	*/
	public boolean equals(Object other) {
		boolean result = false;


		return result;
	}

	/*       
	# Description: creates a deep clone of a pocket object
    # 
    # Parameters: none
    # 
    # Returns Value: Pocket			
	*/
	public Object clone() {
		Pocket clone = null;	
		return clone;
	}
}
