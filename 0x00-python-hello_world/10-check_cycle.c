#include "lists.h"

/**
 * check_cycle - A function that checks for cycle in a singly linked list
 * @list: head of the signly linked list
 *
 * Description - Checking for loops in a sigly linked list
 * Return: 1 if cycled is found and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *low, *high;

	if (!list)
		return (0);
	low = list;
	high = list->next;
	while (high && low && high->next)
	{
		if (low == high)
			return (1);
		low = low->next;
		high = high->next->next;
	}
	return (0);
}
