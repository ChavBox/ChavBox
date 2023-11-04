/* 
#  Name:       			 	
#  Date:        	  	
#  Description: 	
*/ 

import java.util.Iterator;
import java.util.Scanner;

public class Program
{
    public static void main(String[] args)
    {
        Scanner keyboard = new Scanner(System.in);
		
        System.out.println("Running the Backpack application...\n");

        try
        {
            Backpack backpack = new Backpack();

            String itemName = "Sleeping bag";
            backpack.insertItemInMainPocket(itemName, 2.0);
            //backpack.insertItemInMainPocket(itemName, -1.0);
            
            itemName = "Tent";
            backpack.insertItemInMainPocket(itemName, 5.0);

            //itemName = "Stove";
            //backpack.insertItemInMainPocket(itemName, 4.0);
        
            itemName = "Cup"; 
            backpack.insertItemInRightPocket(itemName, 0.25);
            
            itemName = "Plate";
            backpack.insertItemInRightPocket(itemName, 0.5);
           
            itemName = "Compass";
            backpack.insertItemInLeftPocket(itemName, 0.1);

            itemName = "Knife";
            backpack.insertItemInLeftPocket(itemName, 0.3);
          
            itemName = "Sleeping bag";
            backpack.removeItemFromMainPocket(itemName);
            
            itemName = "Plate";
            backpack.removeItemFromRightPocket(itemName);
           
            itemName = "Compass";
            backpack.removeItemFromLeftPocket(itemName);

            itemName = "Fork";
            backpack.removeItemFromLeftPocket(itemName);
            
            double backPackTotalWeight = backpack.getTotalWeight();
            System.out.println("Backpack total weight: " + backPackTotalWeight);
            System.out.println();

            System.out.println("Iterating through the backpack:\n");

            Iterator<Pocket> backpackIterator = backpack.iterator();
            while(backpackIterator.hasNext())
            {
                Pocket pocket = backpackIterator.next();
                Iterator<BackpackItem> pocketIterator = pocket.iterator();
                while (pocketIterator.hasNext())
                {
                    BackpackItem backpackItem = pocketIterator.next();

                    System.out.println("Item name: " + backpackItem.itemName 
                            + " Item weight: " + backpackItem.itemWeight);
                }
            }
            
            System.out.println("Iterating through the backpack:\n");

            for (Pocket pocket: backpack)
            {
                for (BackpackItem backpackItem : pocket) 
                {
                    System.out.println("Item name: " + backpackItem.itemName 
                            + " Item weight: " + backpackItem.itemWeight);
                }
            }

            System.out.println();
        }
        catch (Exception ex)
        {
            String exceptionMessage = ex.getMessage();
            String exceptionCauseMessage = ex.getCause().getMessage();

            if (exceptionCauseMessage == "Insert")
            {
                System.out.println(exceptionMessage);
            }
            else if (exceptionCauseMessage == "Remove")
            {
                System.out.println(exceptionMessage);
            }
        }

        keyboard.close();
    }
}

