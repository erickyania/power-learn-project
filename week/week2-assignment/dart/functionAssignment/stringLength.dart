int stringLength(String letter) {
  return letter.length;
}

void main(){
  String myString = "Hello, world!";
  int length = stringLength(myString); 
  print("The length of the string is: $length");
}