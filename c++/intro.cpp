#include <iostream>

// this is a single line comment

/*
  This is a multi line
  comment

  to compile:
  g++ intro.cpp
  or
  g++ -o intor intro.cpp

  to run:
  ./a.out
  or
  ./intro.cpp
  
  
 */

int main()  // here to end of line is a comment 
{
  int x=21;
  double d = 21;
  char c; 
  bool tf = false;
  std::string s= "this is a string";
 
  std::cout << "Hello World!\n";
  std::cout << "the var x = " << x << "\n";
  
  std::cout << "Doubles: "<< d <<" "<< d/2 <<std::endl;
  std::cout << "Ints:"<< x << " "<< x/2 << std::endl;

  c = 'x'; //a SINGLE character
  std::cout<< c << "\n"

  std::cout<<  "A true value:" << tf <<"\n"; //returns 1 if bool is true and 0 if bool is false
  return 0;
}

// use -wall when running to show the errors in the program
