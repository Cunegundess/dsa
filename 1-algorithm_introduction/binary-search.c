#include <stdio.h>

/* 
   Binary Search 
   An algorithm that returns the position of the target element in a sorted array(list)
   if the element is not found, it returns None 
   It works by repeatedly dividing in half the portion of the list that could 
   contain the target value, until you've narrowed down the possible locations 
   to just one.
*/


int binarySearch(int array[], int array_length, int num) {
  
  int left = 0;
  int right = array_length - 1;

  while (left <= right) {
    int mid = (left + right) / 2;
    int target = array[mid];

    if (target == num) {
      return mid;
    }

    if (target > num) {
      right = mid - 1;
    }

    else {
      left = mid + 1;
    }
  }

  return -1; // Return -1 if the num is not found
}

int main() {

  int array[] = {1, 3, 5, 7, 9};
  int array_length = sizeof(array) / sizeof(array[0]);

  printf("Elemento esperado está na posição: %d\n", binarySearch(array, array_length, 5));
  printf("%d\n", binarySearch(array, array_length, -1));
  return 0;
}
