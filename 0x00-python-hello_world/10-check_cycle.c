#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	current = list;
	temp = list;
	while (current != NULL && temp != NULL && temp->next != NULL)
	{
		current = current->next;
		temp = temp->next->next;
		if (current == temp)
			return (1);
	}
	return (0);
}
