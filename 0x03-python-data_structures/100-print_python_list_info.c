#include <stdio.h>
#include <stdlib.h>
#include <python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - A function that prints basic
 *	information about python list
 * @p: Python object
 *
 * Return: None
 */
void print_python_list_info(PyObject *p)
{
	int sz_l = 0;
	long int sz;
	PyListObject *objt = (PyListObject *)p;

	sz = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = %li\n", objt->allocated);
	while (sz_l < sz)
	{
		printf("Element %i: %s\n", sz_l, Py_TYPE(objt->ob_item[sz_l])->tp_name);
		sz_l++;
	}
}
