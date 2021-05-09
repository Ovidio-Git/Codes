#include <stdio.h>
#include <string.h>

char search(char chain[], char target[]){

    int n = 0;
    int m = 0;
    int len = strlen(target);
    char find[10];
    int j = 0;


    while (chain[n] != '\0'){
        printf("2");
        if (chain[n]==target[m]){
            printf("3");
            while(chain[n] == target[m]){
                n++;
                m++;
                printf("4");
                if (m==len){
                    printf("5");
                    while(chain[n] != '\0'){
                        printf("6");
                        find[j]=chain[n];
                        j++;
                        n++;
                    }
                }
            }
            m=0;
        }
        n++;
        m=0;
    }
    printf("7");
}


int main(){
    char b[]="Accept-Language: en-US,en;q=0.9  Username=er32 Password=89re ccep� ";
    char t[]="Usernamee";
    search(b, t);
}