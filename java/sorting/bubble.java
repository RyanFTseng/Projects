import java.util.Scanner;
class bubble{

public static void main(String args[]){
int m,i;
Scanner in = new Scanner(System.in);
System.out.println("input array size");
m=in.nextInt();
int a[]=new int[m];
System.out.println("input array elements");
for(i=0;i<m;i++)
	a[i]=in.nextInt();
for (i=0;i<m;i++)
sort(a,m);
for (i=0;i<m;i++)
System.out.println(a[i]);
}

static void sort(int a[],int m){
int i,j,x;

for (i=0;i<m;i++)
//	System.out.print("  "+a[i]);
	for (j=0;j<m-i-1;j++)
		if (a[j]>a[j+1]){
			x=a[j];
			a[j]=a[j+1];
			a[j+1]=x;
			}
}
}
