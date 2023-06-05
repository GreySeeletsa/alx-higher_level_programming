#include "lists.h"
/**
 * check_cycle - function in C that checks if a
 * singly linked list has cycle in it
 * @list: parameter to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *not_fast = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (not_fast && fast && fast->next)
	{
		not_fast = not_fast->next;
		fast = fast->next->next;
		if (not_fast == fast)
			return (1);
	}
	return (0);
}
