#include <Python.h>

/**
 * print_python_float - Print information about Python float objects
 * @p: Pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
	}
	else
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
	}
}

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: Pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		char *str = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", str ? str : "(corrupted)");

		printf("  first 10 bytes: ");
		for (Py_ssize_t i = 0; i < size && i < 10; ++i)
		{
			printf("%02hhx", str[i]);
			if (i + 1 < size && i + 1 < 10)
				printf(" ");
		}
		printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Print information about Python list objects
 * @p: Pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (Py_ssize_t i = 0; i < size; ++i)
		{
			printf("Element %ld: ", i);

			PyObject *item = PyList_GetItem(p, i);

			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			else
				printf("[*] %s\n", Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
	}
}
