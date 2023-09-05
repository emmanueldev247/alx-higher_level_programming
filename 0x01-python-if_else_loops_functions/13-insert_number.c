#include "lists.h"

/**
 * insert_node - that inserts a number into a sorted singly linked list
 * @head: head
 * @number: number to be inserted
 *
 * Return: returns the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *prev;

	if (*head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	current = *head;
	prev = *head;
	while (current)
	{
		if ((current->n) > number)
		{
			new->next = current;
			prev->next = new;
			return (new);
		}
		else
		{
			prev = current;
			current = current->next;
		}
	}
	prev->next = new;

	return (new);
}
