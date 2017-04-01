class day{
enum Day{MONDAY,TUESDAY,WEDENESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY}
public static void main(String args[]){
//ONDAY,TUESDAY,WEDENESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY}
for (Day d:Day.values()){
	System.out.print(d);
	System.out.print(" is day number ");
	System.out.print(d.ordinal()+1 );
	System.out.println("");
	}
}
}

