#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_nodeint - This adds a new node at the beginning of a listint_t list
 * @head: This is the head of listint_t
 * @n: The integer to add in listint_t list
 * Return: The address of the new element, or NULL if fail
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
	{
		return (NULL);
	}

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}

/**
 * is_palindrome - This identifies if a syngle linked list is palindrome
 * @head: This is the head of listint_t
 * Return: 1 if it is palindrome otherwise zero
 */

int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *temp1 = NULL, *temp2 = NULL;

	if (!*head || head2->next == NULL)
	{
		return (1);
	}
	while (head2 != NULL)
	{
		add_nodeint(&temp1, head2->n);
		head2 = head2->next;
	}
	temp2 = temp1;
	while (*head != NULL)
	{
		if ((*head)->n != temp2->n)
		{
			free_listint(temp1);
			return (0);
		}
		*head = (*head)->next;
		temp2 = temp2->next;
	}
	free_listint(temp1);
	return (1);
}
