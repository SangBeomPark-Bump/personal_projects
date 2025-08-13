#include <stdio.h>
#include <string.h>


int main(void){

    char str[100];
    // char* p;

    scanf("%s", str);

    // printf( "%s \n", str );


    int start = 0;
    int end = strlen(str) - 1;

    // printf("%c", str[start]);
    // printf("%c", str[end]);

    int flag = 1;

    while (start< end){
        if (str[start] != str[end]){
            flag = 0;
            break;
        }

        start +=1;
        end -=1;
    }

    if (flag){
        printf("%d \n", 1);
    } else{
        printf("%d \n", 0);
    }


    return 0;
}