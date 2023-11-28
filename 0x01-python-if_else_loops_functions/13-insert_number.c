#include "lists.h"

/**
 * insert_node - This function inserts number into a sorted singly-linked list
 * @head: This parameter is a pointer the head of the linked list.
 * @number: This parameter is the number to insert.
 * Return: NULL If the function fails, else a pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;

	if (!current_node || current_node->n >= number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}

	while (current_node && current_node->next
			&& current_node->next->n < number)
	{
		current_node = current_node->next;
	}

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
