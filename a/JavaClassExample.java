public class JavaClassExample{
private String name;

public void setName(String n){
name = n;
}

public String getName(){
return name;
}

public static void main (String args[]){
JavaClassExample javaClassExample= new JavaClassExample();
javaClassExample.setName("visitor");
System.out.println("hello"+javaClassExample.getName());
}
}
