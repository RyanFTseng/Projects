import java.util.Scanner;
class transpose{
public static void main (String args[]){
int x,y,i,j;

System.out.println("input matrix size");
Scanner in = new Scanner(System.in);
x=in.nextInt();
y=in.nextInt();

int matrix[][]=new int[x][y];
int transpose[][]=new int[x][y];

System.out.println("input matrix elements");
for (i=0;i<x;i++)
	for (j=0;j<y;j++)
		matrix[i][j]=in.nextInt();


for (i=0;i<x;i++)
        for(j=0;j<y;j++)
		transpose[j][i]=matrix[i][j];

System.out.println("matrix");
for(i=0;i<x;i++){
        for(j=0;j<y;j++)
                System.out.print(matrix[i][j]+"\t");
        System.out.println();
        }


System.out.println("tranpose");
for(i=0;i<x;i++){
        for(j=0;j<y;j++)
                System.out.print(transpose[i][j]+"\t");
	System.out.println();
	}

int k=0;
for(i=0;i<x;i++)
        for(j=0;j<y;j++)
if (transpose[i][j]!=matrix[i][j]){
	k=1;
}

if (k==0){
	System.out.println("symmetric");
}
else{
	System.out.println("non symmetric");
}



}
}


