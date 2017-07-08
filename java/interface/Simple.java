import java.util.Calendar;
public class Simple{
public static void main (String[] args){
	Calendar now = Calendar.getInstance();
	System.out.println("current date: "
		+(now.get(Calendar.MONTH)+1)
		+"-"
		+now.get(Calendar.DATE)
		+"-"
		+now.get(Calendar.YEAR));

	now.add(Calendar.DATE,1);
	System.out.println("date after 1 day: "
		+(now.get(Calendar.MONTH)+1)
		+"-"
		+now.get(Calendar.DATE)
		+"-"
		+now.get(Calendar.YEAR));

	now = Calendar.getInstance();
	now.add(Calendar.DATE,+10);
	System.out.println("date after 10 days: "
                +(now.get(Calendar.MONTH)+1)
                +"-"
                +now.get(Calendar.DATE)
                +"-"
                +now.get(Calendar.YEAR));

}
}

