#include <Python.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
	{
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
	}
}
