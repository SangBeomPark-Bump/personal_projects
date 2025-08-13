#include <stdio.h>


int main(void){
    int n;
    scanf("%d\n", &n);

    int temp;
    int pmax = -1000 * 100000;  
    int max = -1000 * 100000;


	for (int i = 0; i < n; i++){
        scanf("%d", &temp);
        pmax += temp;
        if (temp > pmax) pmax = temp;
        if (pmax > max) max = pmax;
    }
    printf("%d\n", max);
    return 0;
}