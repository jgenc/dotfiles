#include <stdio.h>

int main() {
    FILE *inputptr = fopen("input1", "r");
  
    int table[200];
    int i = 0;
    int f = 0;

    while (!(feof(inputptr))) {
      if (i == 200) { break; }
      fscanf(inputptr, "%d", &table[i]);
      printf("table[%d] = %d\n", i, table[i]);
      i++;
    }

    int x,y;
    for (x = 0; x <= 199; x++) {
      for (y = 0; y <= 199; y++) {
        printf("table[%d] + table[%d] = %d\n", x, y, table[x]+table[y]);
        if ((table[x] + table[y]) == 2020) {
          printf("\t\tDONE\n");
          f = 1;
          break;
        }
      }
      if (f == 1) { break; }
    }
    

    if (f == 1) {
        printf("%d + %d is %d\n", table[x], table[y], table[x]+table[y]);
        printf("%d * %d is %d\n", table[x], table[y], table[x]*table[y]);
    }

    fclose(inputptr);
    return 0;
}
