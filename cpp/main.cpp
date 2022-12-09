#include <iostream>
// HERE IS A FUNCTION WHERE I ADD THE SUM OF THE SQUARES FOR THE RANGE A TO B. 
//I used a for loop inside this function. 
int sum_of_squares(int a, int b){
  int c = 0;
  for (int i = a; i <= b; i++){
    c= c + i*i;
  }
  return c;
  }
// I used the main function to add the numbers I needed to test the function. 
int main(){
  int a,b,i;
  a = 3;
  b = 6;
  int c= sum_of_squares(a,b);
  std::cout<<c<<'\n';
  return 0;
}