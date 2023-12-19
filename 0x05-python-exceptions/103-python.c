#include <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to a PyObject (Python list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *obj;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		else if (PyFloat_Check(obj))
			print_python_float(obj);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes
 * @p: Pointer to a PyObject (Python bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf("%02hhx%c", str[i], i + 1 == size + 1 || i + 1 == 10 ? '\n' : ' ');
}

/**
 * print_python_float - Prints information about Python floats
 * @p: Pointer to a PyObject (Python float)
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
