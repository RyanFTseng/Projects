import java.util.Scanner;
class factorial{
public static void main(String args[]){
int x;
System.out.println("input");
Scanner in = new Scanner(System.in);
x = in.nextInt();
System.out.println(fact(x));
}

static int fact(int x){
if (x==1)
return 1;
else
return(x*fact(x-1));

}
}

