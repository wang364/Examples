#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MAX_WORDS_NUM 1000

bool isAll9(char* str, int n)
{
    int i;
    for (i = 0; i < n; i ++)
    {
        if (str[i] != '9')
            return false;
    }
    
    return true;
} 

void printNumber(int wordsNum)
{
    char numStr[MAX_WORDS_NUM];
    const char zero = '0';
    int i,j,k;
    bool toDealWords = true;
    
    if(wordsNum > MAX_WORDS_NUM)
    {
        printf("The number of words is out of range!");
        return;
    }
    
    memset(numStr, 0, MAX_WORDS_NUM * sizeof(char));
    for (i = 0; i < wordsNum; i ++)
    {
        do
        {
            if (numStr[i] == '\0')
            {
                /* jinwei 1000... */
                if ( i > 0)
                {
                    numStr[0] = zero + 1;
                    for (j = i - 1; j > 0; j --)
                    {
                        numStr[j] = zero;
                    }
                }
            }
            else
            {
                for (j = i - 1; j >= 0; j --)
                {
                    if (numStr[j] == '9')
                        continue;
                    numStr[j] += 1;
                    for( k = j + 1; k <= i - 1; k ++)
                        numStr[k] = zero;
                    break;
                }
            }
            for(k = 0; k < 10; k ++)
            {
                numStr[i] = zero + k;
                printf("%s\n", numStr);
            }  
        } while (!isAll9(numStr, i));
        
    }
}

int main()
{
    int a;
    printf("Input the length of words:");
    scanf("%d", &a);
    printNumber(a);
    pause();
    return 0;
}