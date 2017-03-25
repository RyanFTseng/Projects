import java.util.Scanner;
class reversestring{
public static void main (String args[]){
System.out.println("input string");
Scanner a=new Scanner(System.in);
String x=a.nextLine();
String y="";
int z=x.length();
for (int i=z-1;i>=0;i--){
	y=y+x.charAt(i);
	}

	System.out.println(y);
	}
}
