#include "lists.h"
/**
 * is_palindrome - A function that check for palindrome
 * @head: the pointer to the array containing the list
 *
 * Return: 0 if not palindrome and 1 for palindrome
 */
int is_palindrome(listint_t **head)
{
	const listint_t *cur_head;
	int len = 0, i = 0, j = 0;
	int array[10000];

	if (*head == NULL)
		return (1);
	cur_head = *head;
	while (cur_head)
	{
		cur_head = cur_head->next;
		len++;
	}
	if (len == 1)
		return (1);

	cur_head = *head;
	while (cur_head)
	{
		array[i] = cur_head->n;
		i++;
		cur_head = cur_head->next;
	}
	i--;
	len--;
	while (i >= (len / 2))
	{
		if (array[i] != array[j])
			return (0);
		i--;
		j++;
	}
	return (1);
}

