class str8{
public static void main(String args[]){
String str1="red is my favorite color";
String str2="orange is also my favorite color";
String startstr="red";
boolean starts1= str1.startsWith(startstr);
boolean starts2= str2.startsWith(startstr);
System.out.println(str1+"starts with"+ startstr+ starts1);
System.out.println(str2+"starts with"+ startstr+ starts2);

}
}
