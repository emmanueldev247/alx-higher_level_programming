#include "lists.h"

/**
 * check_cycle - function to check if a singly
 *				linked list has a cycle in it
 * @list: the list
 *
 * Return: 1 (a cycle is found); 0 (no cycle found)
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	hare = list;
	tortoise = list;

	if (list == NULL)
		return (0);

	while (hare && hare->next)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		if (hare == tortoise)
			return (1);
	}

	return (0);
}
