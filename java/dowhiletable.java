import java.util.Scanner;
class dowhiletable
{
public static void main(String args[])
{
Scanner in = new Scanner(System.in);
System.out.println("input number");
int n;
n=in.nextInt();
int i;
i=1;
do
        {
        System.out.println(n+"x"+i+"="+(n*i));
        i=i+1;
        }
while (i!=11);
}
}

