#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *array;
	int i, j, size;

	if (head == NULL || *head == NULL)
		return (1);

	current = *head;
	size = 0;
	while (current != NULL)
	{
		current = current->next;
		size++;
	}

	array = malloc(sizeof(int) * size);
	if (array == NULL)
		return (0);

	current = *head;
	i = 0;
	while (current != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}

	i = 0;
	j = size - 1;
	while (i < j)
	{
		if (array[i] != array[j])
		{
			free(array);
			return (0);
		}
		i++;
		j--;
	}

	free(array);
	return (1);
}
