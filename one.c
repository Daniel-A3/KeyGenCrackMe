#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    if(argc==2) {
		printf("Checking License: %s\n", argv[1]);

		int sum = 0;
		for (int i = 0; i < strlen(argv[1]); i++) {
			sum += (int) argv[1][i];
		}
		printf("Value: %d\n", sum);
		if(sum == 1091) {
			printf("Access Granted!\n");
		} else {
			printf("WRONG!\n");
		}
	} else {
		fprintf(stderr, "Usage: <key>\n");
	}
	return 0;
}
