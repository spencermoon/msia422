package homework5;

import java.text.*;
import java.util.*;

/**
 * This is the Appointment superclass. 
 * @author Spencer Moon
 */

public class Appointment 
{
    protected String description = "";
	protected Date date; 
 
	
	// Define appointment
    public Appointment(String description)
    { 
        this.description = description; 
    } 
    
    
    // Add occursOn method to check if an appointment occurs on a specified date
    public boolean occursOn(int year, int month, int day) throws ParseException 
    { 
        DateFormat dateFormatter = new SimpleDateFormat(String.format("yyyy-MM-dd")); 
        Date checkedDate = dateFormatter.parse(String.format("%d-%d-%d", year, month, day)); 
        return checkedDate.equals(this.date); 
    } 
}