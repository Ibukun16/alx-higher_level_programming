#include "lists.h"
/**
 * is_palindrome - A function that check for palindrome
 * @head: the pointer to the array containing the list
 *
 * Return: 0 if not palindrome and 1 for palindrome
 */
int is_palindrome(listint_t **head)
{
	const listint_t *head_cur;
	int len = 0, i = 0, j = 0;
	int array[10000];

	if (!*head)
		return (1);
	head_cur = *head;
	while (head_cur)
	{
		head_cur = head_cur->next;
		len++;
	}
	if (len == 1)
		return (1);

	head_cur = *head;
	while (head_cur)
	{
		array[i] = head_cur->next;
		i++;
		head_cur = head_cur->next;
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

