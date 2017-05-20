import java.util.Scanner;
class min{
public static void main(String[] args){
int m,i,j,minm,ind;
System.out.println("input array size");
Scanner in=new Scanner (System.in);
m=in.nextInt();
System.out.print("input array elements");
int a[]=new int[m];

for (i=0;i<m;i++)
        a[i]=in.nextInt();
minm=130;

for (i=0;i<m;i++)
	if (a[i]<minm)
		minm=a[i];

System.out.println(minm);
//System.out.println(ind);
}
}

