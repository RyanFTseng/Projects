import java.util.Scanner;
class select{
public static void main(String[] args){
int m,i,j,b;
System.out.println("input array size");
Scanner in=new Scanner (System.in);
m=in.nextInt();
System.out.print("input array elements");
int a[]=new int[m];
for (i=0;i<m;i++)
        a[i]=in.nextInt();

for (i=0;i<m-1;i++)
	for (j=0;j<m-i-1;i++)
		if (a[


