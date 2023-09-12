#include "lists.h"
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: singly linked list to be checked
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *current, *prev, *next, *reversed;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;
	current = *head;
	prev = NULL;
	next = NULL;

	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	while (slow)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	reversed = prev;

	current = *head;

	while (reversed && current)
	{
		if (current->n != reversed->n)
			return (0);
		current = current->next;
		reversed = reversed->next;
	}

	return (1);
}
