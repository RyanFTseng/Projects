class harmonicnum{
public static void main (String args[]){
int n=Integer.parseInt(args[0]);
double h=0.0;
for(int i=1;i<n+1;i++)
	h=h+1.0/i;

System.out.println(h);
}
}
