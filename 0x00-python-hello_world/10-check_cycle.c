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
	listint_t *hare, *tortoise, *temp;

	hare = list;
	tortoise = list;
	temp = list;

	while (hare)
	{
		hare = temp->next->next;
		tortoise = list->next;

		if (hare == tortoise)
			return (1);
		list = tortoise;
		temp = hare;
	}

	return (0);
}
