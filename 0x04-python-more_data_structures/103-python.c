#include <Python.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <listobject.h>

/**
 * print_python_list - Prints some basic info about Python list.
 * @p: Python list object
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid Python list object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints some basic info about Python bytes
 * @p: Python byte object
 */

void print_python_bytes(PyObject *p)
{
	unsigned char *bytes;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	bytes = (unsigned char *)PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		printf("%02hhx", bytes[i]);
		if (i < 9)
		{
			printf(" ");
		}
	}
	printf("\n");
}
