#include<stdio.h>
int main(){
    int a;
    int b;
    int book = 15000;
    printf("책의 가격은 15000원 입니다.\n");
    printf("당신이 가지고 있는 돈은 얼마인가요?:");
    scanf("%d", &a);
    if (a >= book){
        b = a - book;
        printf("책을 성공적으로 구입했습니다. 이제 남은 돈은 %d입니다.\n", b);
    }

    return 0;
}