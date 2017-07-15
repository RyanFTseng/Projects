public class car{
private String name;
private String color;
private String model;
private String year;

public void setName(String n){
name=n;
}
public String getName(){
return name;
}

public void setColor(String a){
color=a;
}
public String getColor(){
return color;
}

public void setModel(String m){
model=m;
}
public String getModel(){
return model;
}

public void setYear(String y){
year=y;
}
public String getYear(){
return year;
}


public static void main (String args[]){
car javaClassExample=new car();
javaClassExample.setName("Toyota");
javaClassExample.setColor("yellow");
javaClassExample.setModel("Camry");
javaClassExample.setYear("2010");
System.out.println(javaClassExample.getName());
System.out.println(javaClassExample.getColor());
System.out.println(javaClassExample.getModel());
System.out.println(javaClassExample.getYear());
}
}
