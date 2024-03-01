T getFirstElement<T>(List<T> list) {
  if (list.isEmpty) {
    throw ArgumentError('The list cannot be empty.');
  }
  return list[0]; // Access the first element using index 0
}

// Example usage
void main() {
  List<int> numbers = [1, 2, 3];
  int firstNumber = getFirstElement<int>(numbers);
  print("The first element is: $firstNumber");  // Output: The first element is: 1

  List<String> names = ["Alice", "Bob", "Charlie"];
  String firstName = getFirstElement<String>(names);
  print("The first name is: $firstName");  // Output: The first name is: Alice
}
