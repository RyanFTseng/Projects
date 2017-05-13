import java.util.Scanner;
class matrix{
public static void main (String args[]){
int m,n,j,i;
System.out.println("input matrix size");
Scanner in = new Scanner(System.in);
m=in.nextInt();
n=in.nextInt();

int first[][]=new int[m][n];
int second[][]=new int[m][n];
int sum[][]=new int[m][n];

System.out.println("input 1st matrix elements");
for (i=0;i<m;i++)
	for(j=0;j<n;j++)
		first[i][j]=in.nextInt();

System.out.println("input 2nd matrix elements");

for (i=0;i<m;i++)
        for(j=0;j<n;j++)
                second[i][j]=in.nextInt();

for (i=0;i<m;i++)
	for(j=0;j<n;j++)
		sum[i][j]=first[i][j]+second[i][j];



System.out.printlrn("sum");
for(i=0;i<m;i++){
        for(j=0;j<n;j++)
		System.out.print(sum[i][j]+"\t");
		
	System.out.println();
	}
}
}

