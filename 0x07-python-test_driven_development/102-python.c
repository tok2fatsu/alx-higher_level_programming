#include <stdio.h>
#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string objrect.
 */
void print_python_string(PyObject *p);
{
	long int length;

	fflush(stdout);

	print("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		priontf("  type: compact unicode object\n");
	printf("  length: %d\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
