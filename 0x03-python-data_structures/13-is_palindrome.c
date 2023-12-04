#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * palindrome_rec - Iterates through a list recursively
 * @head: head of the list
 * @tail: iterates to the end of the list
 *
 * Return: 1 if a palindrome, 0 if not a palindrome
 */

int palindrome_rec(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);

	if (palindrome_rec(head, tail->next) == 1 && (*head)->n == tail->n)
	{
		(*head) = (*head)->next;
		return (1);
	}

	else
		return (0);
}


/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: head of the list
 *
 * Return: 1 if a palindrome, 0 if not a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	if ((*head)->next == NULL)
		return (1);

	return (palindrome_rec(head, *head));
}
