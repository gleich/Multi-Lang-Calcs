// Instructions:
// Just run the file and answer the questions!
//--------------------------------------------------------------------
package Calculators.Science.Physcial_Science;

import java.util.Scanner;

public class OHM_Calculator {
	
	private static Scanner sc;
    private static boolean isContinuing;
    
    private static double ampage;
    private static double voltage;
    private static double resistance;

	public static void main( String[] args )
    {
        sc = new Scanner( System.in );
        isContinuing = true;

        ampage = 0;
        voltage = 0;
        resistance = 0;
        
        while ( isContinuing )
        {
            System.out.println(
                "What are you trying to find: Voltage, Current, or Resistance?" );
            String input = sc.next();

            switch ( input )
            {
            case "Voltage":
            	System.out.println("What is the ampage?");
            	ampage =  sc.nextDouble();
            	System.out.println("What is the resistance?");
            	resistance = sc.nextDouble();
            	
            	voltage = ampage * resistance;
            	System.out.println("The voltage is: " + voltage + " volts.");

            	break;

            case "Current":
            	System.out.println("What is the voltage?");
            	voltage =  sc.nextDouble();
            	System.out.println("What is the resistance?");
            	resistance = sc.nextDouble();
            	
            	ampage = voltage / resistance;
            	System.out.println("The current is: " + voltage + " amps.");
            	
            	break;

            case "Resistance":
            	System.out.println("What is the ampage?");
            	ampage =  sc.nextDouble();
            	System.out.println("What is the voltage?");
            	voltage = sc.nextDouble();
            	
            	resistance = voltage / ampage;
            	System.out.println("The resistance is: " + resistance + ".");
            	
            	break;

            default:
                System.out.println( "Invalid input." );
                
                break;
            }
            
            System.out.println( "Would you like to continue? Y/N" );
            String userInputToContinue = sc.next();
            
            if( userInputToContinue == "Y")
            {
                isContinuing = true;
            }
            else
            {
            	if( !(userInputToContinue == "N") )
            	{
                    System.out.println(
                        "Invalid input, this program will now be terminated." );
            	}
            	
            	isContinuing = false;
            }
        }
    }
}