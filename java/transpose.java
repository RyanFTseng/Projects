import java.util.Scanner;
class transpose{
public static void main (String args[]){
int x,y,i,j;
System.out.println("input matrix size");
Scanner in = new Scanner(System.in);
x=in.nextInt();
y=in.nextInt();
int matrix[][]=new int[x][y];

System.out.println("input matrix elements");
