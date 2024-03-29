﻿/* 
#  Name: Charlie Havener
#  Date: 11/7/2023
#  Description: A backpack consisting of three Pockets which have a maximum weight capacity 	
*/ 
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
    	mainPocket = new Pocket("Main Pocket", mainPocketMaxWeight);
        rightPocket = new Pocket("Right Pocket", rightPocketMaxWeight);
        leftPocket = new Pocket("Left pocket", leftPocketMaxWeight);
    }

    //Methods
   
    /*       
	# Description: Adds a BackPack item to the main pocket if it is able to 
    # 
    # Parameters:
    #   itemName: the name of the item to be inserted
    #   itemWeight: the weight of the item to be inserted
    # 
    # Returns Value: None			
	*/
    public void insertItemInMainPocket(String itemName, double itemWeight) throws Exception{
        mainPocket.insertItemInPocket(itemName, itemWeight);
    }
    
    /*       
	# Description: Adds a BackPack item to the right pocket if it is able to
    # 
    # Parameters:
    #   itemName: the name of the item to be inserted
    #   itemWeight: the weight of the item to be inserted
    # 
    # Returns Value: None			
	*/
    public void insertItemInRightPocket(String itemName, double itemWeight) throws Exception
    {
    	rightPocket.insertItemInPocket(itemName, itemWeight);
    }
    
    /*       
	# Description: Adds a BackPack item to the left pocket if it is able to
    # 
    # Parameters:
    #   itemName: the name of the item to be inserted
    #   itemWeight: the weight of the item to be inserted
    # 
    # Returns Value: None			
	*/
    public void insertItemInLeftPocket(String itemName, double itemWeight) throws Exception
    {
    	leftPocket.insertItemInPocket(itemName, itemWeight);
    }
    
    /*       
	# Description: Removes a BackPack item to the main pocket if it exists
    # 
    # Parameters:
    #   itemName: the name of the item to remove
    #         // TODO Auto-generated method stub

    # Returns Value: None			
	*/
    public void removeItemFromMainPocket(String itemName) throws Exception
    {
    	mainPocket.removeItemFromPocket(itemName);
    }
    
    /*       
	# Description: Removes a BackPack item to the right pocket if it exists
    # 
    # Parameters:
    #   itemName: the name of the item to remove
    # 
    # Returns Value: None			
	*/
    public void removeItemFromRightPocket(String itemName) throws Exception
    {
    	rightPocket.removeItemFromPocket(itemName);
    }
    
    /*       
	# Description: Removes a BackPack item to the left pocket if it exists
    # 
    # Parameters: 
    #   itemName: the name of the item to remove
    # 
    # Returns Value: None			
	*/
    public void removeItemFromLeftPocket(String itemName) throws Exception
    {
        leftPocket.removeItemFromPocket(itemName);
    }
    
    /*       
	# Description: Lists the items in the main pocket and their weights
    # 
    # Parameters: none
    # 
    # Returns Value: None			
	*/
    public void listItemsInMainPocket() 
    {
    	mainPocket.listItemsInPocket();
    }
    
    /*       
	# Description: Lists the items in the right pocket and their weights
    # 
    # Parameters: none
    # 
    # Returns Value: None			
	*/
    public void listItemsInRightPocket()
    {
    	rightPocket.listItemsInPocket();
    }
    
    /*       
	# Description: Lists the items in the left pocket and their weights
    # 
    # Parameters: none
    # 
    # Returns Value: double			
	*/
    public void listItemsInLeftPocket()
    {
    	leftPocket.listItemsInPocket();
    }
    
    /*       
	# Description: Adds up the weight for all the items in the main pocket of the backpack
    # 
    # Parameters: none
    # 
    # Returns Value: double			
	*/
    public double getMainPocketTotalWeight()
    {
    	double totalWeight = 0;
    	totalWeight = mainPocket.getPocketTotalWeight();    	
        return totalWeight;
    }
    
    /*       
	# Description: Adds up the weight for all the items in the right pocket of the backpack
    # 
    # Parameters: none
    # 
    # Returns Value: double			
	*/
    public double getRightPocketTotalWeight()
    {
    	double totalWeight = 0;
    	totalWeight = rightPocket.getPocketTotalWeight();
        return totalWeight;
    }
    
    /*       
	# Description: Adds up the weight for all the items in the left pocket of the backpack  
    # 
    # Parameters: none
    # 
    # Returns Value: double			
	*/
    public double getLeftPocketTotalWeight()
    {
    	double totalWeight = 0;
    	totalWeight = leftPocket.getPocketTotalWeight();
        return totalWeight;
    }
    
    /*       
	# Description: Prints a list of all the itmes in each of the pockets in the backpack
    # 
    # Parameters: none
    # 
    # Returns Value: None			
	*/
    public void listItemsInBackpack()
    {
    	System.out.println("Listing all backpack items...\n");
    	listItemsInMainPocket();
        listItemsInRightPocket();
        listItemsInLeftPocket();
    }
    
    /*       
	# Description: Adds up the weight for all the items in the each of the pockets in the backpack
    # 
    # Parameters: none
    # 
    # Returns Value: double			
	*/
    public double getTotalWeight()
    {
    	double totalWeight = 0;
    	totalWeight += getMainPocketTotalWeight() + getRightPocketTotalWeight() + getLeftPocketTotalWeight();
        return totalWeight;
    }

    /*       
	# Description: Checks to see if the backpack has another pocket
    # 
    # Parameters: none
    # 
    # Returns Value: boolean			
	*/
    public boolean hasNext() 
    {
        return POCKET_QUANTITY > currentIteratingPocket;
    }

    /*       
	# Description: retuns the next pocket to be iterated 
    # 
    # Parameters: none
    # 
    # Returns Value: Pocket			
    */
    public Pocket next() 
    {
        switch(currentIteratingPocket){
            case 0:
                currentIteratingPocket++;
                return mainPocket;
            
            case 1:
                currentIteratingPocket++;
                return rightPocket;

            case 2:
                currentIteratingPocket++;
                return leftPocket;

            default:
                return null;    
        }

    }

    /*       
	# Description: creates an iterator over pockets
    # 
    # Parameters: none
    # 
    # Returns Value: Iterator<Pocket>			
	*/
    public Iterator<Pocket> iterator() 
    {
        currentIteratingPocket = 0;
        return this;
    }

    /*       
	# Description: checks to see if two backpacks contain the same items
    # 
    # Parameters: Backpack
    # 
    # Returns Value: boolean	
	*/
    public boolean equals(Object other)
	{
		boolean result = false;

		
		return result;
	}

    /*       
	# Description: creates a deep clone of a backpack object
    # 
    # Parameters: none
    # 
    # Returns Value: Backpack			
	*/
    public Object clone()
	{
        Backpack clone = null;

        

        return clone;
    }

    
}
