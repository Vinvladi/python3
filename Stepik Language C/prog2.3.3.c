#include <stdio.h>

main()
{
      int i, k=0, m;

      printf("Wwedite 4islo: ");
      scanf("%d", &i);
      scanf("%*c");

      while (i<1 || i>20){
      printf("Wwedite 4islo ot 1 do 20: ");
      scanf("%d", &i);
      scanf("%*c");}


      while (k<i){
            m=1;
            while (m<=i){
                  printf("%s", "*");
                  ++m;
                  }
                  printf("\n");
                  ++k;
                  }

      scanf("%*c");

      return 0;
      }
//i-число,k-строчка,m-столбец(ну как бы столбец)