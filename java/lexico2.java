import java.util.Scanner;
class lexico2{
public static void main (String args[]){
System.out.println("input string 1");
Scanner in = new Scanner(System.in);
String x = in.nextLine();
System.out.println("input string 2");
String y = in.nextLine();
int z=x.compareToIgnoreCase(y);
System.out.println(z);

if (z<0){
	System.out.println("String 1>String 2");
	}
else if (z>0){
	System.out.println("String 1>String 2");
	}
else if (z==0){
	System.out.println("String 1=String 2");
	}


}
}
