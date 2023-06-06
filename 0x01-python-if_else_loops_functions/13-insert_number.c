#include "list.h"
/**
 * insert_node - function in C that inserts a number into
 * a sorted singly linked list
 * @head: pointer
 * @number: parameter
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *new_nd;

	new_nd = malloc(sizeof(listint_t));
	if (new_nd == NULL)
		return (NULL);
	new_nd->n = number;

	if (nd == NULL || nd->n >= number)
	{
		new_nd->next = nd;
		*head = new_nd;
		return (new_nd);
	}
	while (nd && nd->next && nd->next->n < number)
		nd = nd->next;
	new_nd->next = nd->next;
	nd->next = new_nd;
	return (new_nd);
}
