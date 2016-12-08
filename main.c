//读入文件content.txt并打印
#include<stdio.h>
int main(){
	FILE *ftp;
	char ch;
	ftp=fopen("content.txt","r");
	while(!feof(ftp)){
		ch=fgetc(ftp);
		putchar(ch);	
	} 
	fclose(ftp);
	return 0;
}
