#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;          /* Move one step */
		fast = fast->next->next;    /* Move two steps */

		if (slow == fast)
			return (1);  /* If slow and fast meet, there's a cycle */
	}

	return (0);  /* No cycle detected */
}
