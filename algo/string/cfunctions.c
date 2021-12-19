#include <stdio.h>

char* strcpy(char *src, char *dest)
{
	if(NULL == src) return (dest);
	char *cp = dest;

	while(*cp++ = *src++)
		;

	return (dest);
}

char* strcat(char *src, char*dest)
{
	if(src == NULL ) return (dest);
	char * cp = dest;
	while(*cp != '\0')
		++cp;
	while(*cp++ = *src++);

	return (dest);
}
/*
   -1 src<dest
    0 src=dest
	1 src>dest
 */

int strcmp(const char*src,const char*dest)
{
	while(*dest && *src && (*dest == *src))
	{
		dest++;
		src ++;
	}

	return *dest - *src;
}
