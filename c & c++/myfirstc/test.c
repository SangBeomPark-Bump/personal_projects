#include <stdio.h>

int main(void)

{
    int x[2] = {1, 10};
    int a[2][2] = { {1, 5}, {10, 50}};
    
    int b[2][3] = { {1, 5, 10}, {10, 50, 100}};

    int (*p)[2];

    int (*pp)[3];

    p = a;
    pp = b;

    printf("%d \n", pp);
    printf("%d \n", (pp+1));

    printf("%d \n", (*pp +1));
    printf("%d \n", (*(pp+1) +1));

    printf("%d \n", *(*pp +1));
    printf("%d \n", *(*(pp+1) +1));

    
    return 0;
}

// KVREA
// LOVA
// KVREALOVA