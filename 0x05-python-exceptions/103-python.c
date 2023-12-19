#include <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to a PyObject (Python list)
 */

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
	{
		printf("Element %zd: ", i);
		PyObject *element = PyList_GetItem(p, i);

		if (PyBytes_Check(element))
		{
			print_python_bytes(element);
		} else if (PyFloat_Check(element))
		{
			print_python_float(element);
		} else if (PyList_Check(element))
		{
			print_python_list(element);
		} else
		{
		}
	}
}


/**
 * print_python_bytes - Prints information about Python bytes
 * @p: Pointer to a PyObject (Python bytes)
 */

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", PyBytes_Size(p));

	printf("  trying string: ");
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t print_size = size > 10 ? 10 : size;

	for (Py_ssize_t i = 0; i < print_size; ++i)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}

	printf("\n");
}


/**
 * print_python_float - Prints information about Python floats
 * @p: Pointer to a PyObject (Python float)
 */

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}
