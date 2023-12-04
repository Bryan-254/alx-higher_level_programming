#include <Python.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: This parameter is the python list.
 */

void print_python_list_info(PyObject *p)
{
	int elmt;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elmt = 0; elmt < Py_SIZE(p); elmt++)
	{
		printf("Element %d: %s\n", elmt, Py_TYPE(PyList_GetItem(p, elmt))->tp_name);
	}
}
