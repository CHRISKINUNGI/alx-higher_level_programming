#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head of the list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	tmp = *head;
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (tmp->n > number)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}

	while (tmp->next != NULL)
	{
		if (tmp->next->n > number)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}

	tmp->next = new;
	return (new);
}
