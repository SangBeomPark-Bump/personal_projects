#include <stdio.h>

int main(void){
    float sum = 0;
    float cresum = 0;
    float tempgrade;


    char name[51];
    float credit;
    char grade[3];

    for (int i = 0; i < 20; i++){
        scanf("%s %f %s", name, &credit, grade);

        if (grade[0] == 'P') continue;

        cresum += credit;

        if (grade[0] == 'F'){
            continue;
        }

        tempgrade = 'E' - grade[0];

        if( grade[1] == '+'){
            tempgrade += 0.5;
        }

        sum += tempgrade * credit;
    }
    
    printf( "%f\n", sum/cresum);

    return 0;
}