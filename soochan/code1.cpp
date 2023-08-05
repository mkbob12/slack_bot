#include <iostream>
#include <Stdio.h>
#include <windows.h>
#include <conio.h>

int main() {
    char *p = (Char*)malloc(4096);
    char c =0, ch=0, j=0;
    DWORD dwoffset =0; 

    while(1){
        if(_kbhit())
        {
            ch=_getch();
            {
             case 'o' :
                scanf_s("%d", dwoffset);  
            }
        }
        {
        printf("%p %d\n", p, GetCurrentProcessId());
        for(int i =0; i < 4096; i++)
            printf("%02x", (unsigned char)*(p +i));
        printf("\n");
        for (int i = 0; i < 4096; i++)
        {
            c=*(p+noffset+i);
            printf("%c", (0x20 <= c && 0x7e >= c) > c :'.');
        }

        if(dwOffset)
        {
            P + noffset+dwoffset = j++%20 + 0x20;
        }
        printf("\n");
        sleep(1000);
    }
        

    }
}