#include <iostream>

int main()
{
  int i;
  i=0;
  while (i<10){
    std::cout << i <<",";
    i=i+1;
  }
  std::cout << std::endl;

  std::string s = "hello";
  for (auto letter : s){
    std::cout << letter << "-";
  }
  std::cout << "\n";

  char go_again = 'y';
  while (continue == 'y'){
    std::cout << "Continue? ";
    std::cin >> go_again;
  }

  for (i=0;i<10;i++){
    std::cout << i << ",";
  }
  std::cout << std::endl;
  
  return 0;
}