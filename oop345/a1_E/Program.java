/* 
#  Name:       			 	
#  Date:        	  	
#  Description: 	
*/ 

import java.util.Scanner; 

public class Program
{
    public static void main(String[] args)
    {
        Scanner keyboard = new Scanner(System.in);
		
        System.out.println("Running the Backpack application...\n");

        try
        {
            System.out.println("Creating backpack1 and backpack2 with the same items...");

            Backpack backpack1 = new Backpack();
            Backpack backpack2 = new Backpack();
            
            backpack1.insertItemInMainPocket("Sleeping bag", 2.0);
            backpack2.insertItemInMainPocket("Sleeping bag", 2.0);
            //backpack2.insertItemInMainPocket("Sleeping bag", 1.0);
            //backpack2.insertItemInMainPocket("Sleeping beauty", 2.0);
            
            backpack1.insertItemInMainPocket("Tent", 5.0);
            backpack2.insertItemInMainPocket("Tent", 5.0);

            backpack1.insertItemInRightPocket("Cup", 0.25);
            backpack2.insertItemInRightPocket("Cup", 0.25);
            
            backpack1.insertItemInRightPocket("Plate", 0.5);
            backpack2.insertItemInRightPocket("Plate", 0.5);
           
            backpack1.insertItemInLeftPocket("Spoon", 0.25);
            backpack2.insertItemInLeftPocket("Spoon", 0.25);
            
            backpack1.insertItemInLeftPocket("Fork", 0.5);
            backpack2.insertItemInLeftPocket("Fork", 0.5);

            boolean result = backpack1.equals(backpack2);
            System.out.println("Assertion: backpack1 is equal to backpack2: " + result);

            System.out.println();

            System.out.println("Creating backpack3 by cloning backpack1...");
            Backpack backpack3 = (Backpack)backpack1.clone();
            result = backpack3.equals(backpack1);
            System.out.println("Assertion: backpack3 is equal to backpack1: " + result);
            result = backpack3.equals(backpack2);
            System.out.println("Assertion: backpack3 is equal to backpack2: " + result);

            System.out.println();

            System.out.println("Creating backpack4 by passing backpack1 to copy constructor...");
            Backpack backpack4 = new Backpack(backpack2);
            result = backpack4.equals(backpack2);
            System.out.println("Assertion: backpack4 is equal to backpack2: " + result);
            
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

