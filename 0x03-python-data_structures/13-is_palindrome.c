#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome_recursive - Check if given linked list is palindrome
 * @left: keep track of the current position in the linked list
 * @right: current position in the linked list as the recursion progresses
 * Return: 1 if a palindrome, 0 if not a palindrome
 */

int is_palindrome_recursive(listint_t **left, listint_t *right) 
{
	int is_palindrome;

	if (right == NULL)
	{
		return 1;
	}

	is_palindrome = is_palindrome_recursive(left, right->next);

	if (is_palindrome && ((*left)->n == right->n))
	{
		*left = (*left)->next;
		return 1;
	}

	return 0;
}

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: This is the head of the list
 *
 * Return: 1 if a palindrome, 0 if not a palindrome
 */

int is_palindrome(listint_t **head)
{
	return is_palindrome_recursive(head, *head);
}
