//to print the first n natural numbers:
#include <stdio.h>
#include <stdlib.h>

int main(){
	int n;
	printf("Enter a number:\n");
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++){
		int x = i + 1;
		printf("%d\n", x);
	}
}
