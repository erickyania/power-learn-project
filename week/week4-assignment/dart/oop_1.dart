import 'dart:io';

// Task 2: Define an interface
abstract class DataReader {
  List<String> readData(String filePath);
}

// Task 1: Create classes using inheritance
// Superclass
class Person {
  String name;

  Person(this.name);

  // Task 3: Override an inherited method
  void introduceYourself() {
    print("Hello, my name is $name.");
  }
}

// Subclass implementing interface
class FileDataReader implements DataReader {
  // Task 4: Initialize instance with data from a file
  @override
  List<String> readData(String filePath) {
    try {
      File file = File(filePath);
      List<String> lines = file.readAsLinesSync();
      return lines;
    } catch (e) {
      print("Error reading file: $e");
      return [];
    }
  }
}

// Task 5: Demonstrate the use of a loop
void printData(List<String> data) {
  for (String line in data) {
    print(line);
  }
}

void main() {
  // Create an instance of Person initialized with data from a file
  var dataReader = FileDataReader();
  List<String> fileData = dataReader.readData('data.txt');
  
  // Create an instance of Person with data from the file
  if (fileData.isNotEmpty) {
    String name = fileData.first;
    var person = Person(name);
    
    // Task 3: Call overridden method
    person.introduceYourself();
  } else {
    print("No data found in the file.");
  }
}
