import java.util.Calendar;
public class Addhours{
public static void main (String[] args){
	Calendar now = Calendar.getInstance();
        System.out.println("current date: "
                +(now.get(Calendar.MONTH)+1)
                +"-"
                +now.get(Calendar.DATE)
                +"-"
                +now.get(Calendar.YEAR));

        System.out.println("current time: "
                +now.get(Calendar.HOUR_OF_DAY)
                +":"
                +now.get(Calendar.MINUTE)
                +":"
                +now.get(Calendar.SECOND));

	now.add(Calendar.HOUR,10);
	System.out.println("New time after adding 10 hours:"
		+now.get(Calendar.HOUR_OF_DAY)
                +":"
                +now.get(Calendar.MINUTE)
                +":"
                +now.get(Calendar.SECOND));

        System.out.println("new date after 10 hours: "
                +(now.get(Calendar.MONTH)+1)
                +"-"
                +now.get(Calendar.DATE)
                +"-"
                +now.get(Calendar.YEAR));

	now=Calendar.getInstance();
	now.add(Calendar.HOUR,-3);
	        System.out.println("New time after subtracting 3 hours:"
        	+now.get(Calendar.HOUR_OF_DAY)
                +":"
                +now.get(Calendar.MINUTE)
                +":"
                +now.get(Calendar.SECOND));

}
}
