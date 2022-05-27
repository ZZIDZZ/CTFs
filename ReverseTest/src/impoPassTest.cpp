#include <iostream>
void printFlag(short *param);
int main(){
    int iVar1;
    char *__s2;
    short local_48;
    char local_47;
    char local_46;
    char local_45;
    char local_44;
    char local_43;
    char local_42;
    char local_41;
    char local_40;
    char local_3f;
    char local_3e;
    char local_3d;
    char local_3c;
    char local_3b;
    char local_3a;
    char local_39;
    char local_38;
    char local_37;
    char local_36;
    char local_35;
    char input [20];
    int local_14;
    char *local_10;
    
    local_10 = "SuperSeKretKey";
    local_48 = 65;
    local_47 = ']'; //]Kr=9k0=0o0;k1?k91t
    local_46 = 'K';
    local_45 = 'r';
    local_44 = '=';
    local_43 = '9';
    local_42 = 'k';
    local_41 = '0';
    local_40 = '=';
    local_3f = '0';
    local_3e = 'o';
    local_3d = '0';
    local_3c = ';';
    local_3b = 'k';
    local_3a = '1';
    local_39 = '?';
    local_38 = 'k';
    local_37 = '8';
    local_36 = '1';
    local_35 = 't';
    printFlag(&local_48);

}
void printFlag(short *param){
    int i;
    short *j;
    
    i = 0;
    j = param;
    while ((*j != 9 && (i < 20))) {
        putchar((int)(char)(*j ^ 9));
        j = j + 1;
        i = i + 1;
    }
    putchar(10);
    return;
}