/*
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
*/
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    int n; 
    scanf("%i", &n);
    int *scores = malloc(sizeof(int) * n);
    int temp = 0;
    int scores_i = -1;
    for(int i=0; i < n; i++){
        scanf("%i",&temp);
        if(scores_i==-1 || temp != scores[scores_i])
        {
            scores[++scores_i] = temp;
        }
    }
    // printarr(scores, ++scores_i);
    int m;
    scanf("%i", &m);
    int scores_j = scores_i+1;
    for (int alice_i = 0; alice_i < m; alice_i++) {
        scanf("%i",&temp);
        while(scores_j > 0 && scores[scores_j-1]<=temp){
            scores_j--;
        }
        printf("%i\n", scores_j+1);
    }
    return 0;
}