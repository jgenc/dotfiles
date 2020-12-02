#include <stdio.h>

int main() {
  

  FILE *input = fopen("input2", "r");
  int s = 0;

  int min, max;
  int cS;
  char letter;
  char c[50];
  int i;

  // fscanf(input,"%d %d %c  %s", &min, &max, &letter, &c);
  // printf("min %d, max %d, letter %c, string %s\n", min, max, letter, c);

  while(!(feof(input))) {
    fscanf(input,"%d %d %c  %s", &min, &max, &letter, &c);
    printf("min %d, max %d, letter %c, string %s\n", min, max, letter, c);
    cS = 0;
    i = 0;
    while (c[i] != '\0') {
      if (c[i] == letter) {
        cS++;
      }
      i++;
    }
    if (cS >= min && cS <= max) {
      s++;
    }
  }


  fclose(input);
  printf("%d valid passwords\n", s);
  return 0;
}
