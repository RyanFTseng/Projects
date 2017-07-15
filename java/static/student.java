class student{
int rollno;
String name;
static String college="ITS";

static void change(){
college="BBDIT";
}

student(int r,String n){
rollno=r;
name=n;
}

void display(){
System.out.println(rollno+" "+name+" "+college);
}

public static void main(String args[]){
student.change();

student s1=new student(111,"k");
student s2=new student(222,"a");
student s3=new student(333,"s");

s1.display();
s2.display();
s3.display();
}
}
