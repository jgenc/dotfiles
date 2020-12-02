#include <stdio.h>

int main() {
  
  FILE *input = fopen("input2", "r");
  int s = 0;

  int min, max;
  int cS;
  char letter;
  char c[50];
  int i;

  while(!(feof(input))) {
    fscanf(input,"%d %d %c  %s", &min, &max, &letter, &c);
    cS = 0;
    i = 0;
    if ((c[min-1] == letter && !(c[max-1] == letter)) || (!(c[min-1] == letter) && c[max-1] == letter)) {
      printf("min %d, max %d, letter %c, string %s\n", min, max, letter, c);
      s++;
    }
  }

  fclose(input);
  printf("%d valid passwords\n", s);
  return 0;
}
