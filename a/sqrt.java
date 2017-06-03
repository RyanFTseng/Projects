class sqrt{
public static void main (String args[]){
double c=Double.parseDouble(args[0]);
double eps=1e-15;
double t=c;
//for (int i=0;i<c+1;i++)
//	t=(c/t+t)/2;


while (Math.abs(t-c/t)>eps*t){
	t=(c/t+t)/2.0;
}

System.out.println(t);

}
}


