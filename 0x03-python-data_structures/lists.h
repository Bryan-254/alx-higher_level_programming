#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

def print_list_integer(my_list=[]):;
def element_at(my_list, idx):;
def replace_in_list(my_list, idx, element):;
def print_reversed_list_integer(my_list=[]):;
def new_in_list(my_list, idx, element):;
def no_c(my_string):;
def print_matrix_integer(matrix=[[]]):;
def add_tuple(tuple_a=(), tuple_b=()):;
def multiple_returns(sentence):;
def max_integer(my_list=[]):;
def divisible_by_2(my_list=[]):;
def delete_at(my_list=[], idx=0):;
int is_palindrome(listint_t **head);
void print_python_list_info(PyObject *p);

#endif
