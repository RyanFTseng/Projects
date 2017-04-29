class replace2{
public static void main (String args[]){
String str= "the quick brown fox jumps over the lazy dog";
System.out.println(str);
String new_str= str.replaceAll("fox", "cat");
System.out.println(new_str);
}
}

