#include <stdio.h>
#include <string.h>
int main(void){
printf("Enter password: ");
char pass[40];
scanf("%s", pass);

char p2[] = "CSC2022";
int i = 0, sum = 0;
for(i = 0; pass[i] != '\0'; i++){
sum +=(int)pass[i];
}

if(sum == 415) printf("Access Granted!\n");
else printf("Access Denied!\n\n");

return 0;
}

