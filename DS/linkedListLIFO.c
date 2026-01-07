#include <stdlib.h>
#include <stdio.h>
struct tag
{
    int val;
    struct tag *next;
};
int main()
{
    struct tag *p, *q = NULL;
    int n, i;
    printf("How many nodes in linked list:");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        p = (struct tag *)malloc(sizeof(struct tag));
        printf("Enter Value:");
        scanf("%d", &p->val);
        p->next = q;
        q = p;
    }
    printf("The fetched elements of linked list (FIFO):-\n");
    while (p != NULL)
    {
        printf("%d\n", p->val);
        p = p->next;
    }
    return 0;
}