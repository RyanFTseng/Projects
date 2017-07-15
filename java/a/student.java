public class student{
private String name;
private String school;
private String id;


public void setName(String n){
name = n;
}
public String getName(){
return name;
}

public void setSchool(String s){
school=s;
}
public String getSchool(){
return school;
}

public void setID(String i){
id=i;
}
public String getID(){
return id;
}

public static void main(String args[]){
student javaClassExample=new student();
javaClassExample.setName("P");
javaClassExample.setSchool("School");
javaClassExample.setID("123");
System.out.println(javaClassExample.getName());
System.out.println(javaClassExample.getSchool());
System.out.println(javaClassExample.getID());
}
}






