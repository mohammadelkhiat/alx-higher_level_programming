#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: PyObject representing a bytes object
 */
void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_GET_SIZE(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    size_t i;
    size_t size = PyBytes_GET_SIZE(p);
    unsigned char *string_data = (unsigned char *)PyBytes_AsString(p);

    for (i = 0; i < size && i < 10; ++i)
    {
        printf("%02x ", string_data[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Print information about Python list object
 * @p: PyObject representing a list object
 */
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("[ERROR] Not a Python List\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_GET_SIZE(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size_t i;
    for (i = 0; i < PyList_GET_SIZE(p); ++i)
    {
        printf("Element %ld: ", i);
        PyObject *element = PyList_GET_ITEM(p, i);

        if (PyBytes_Check(element))
        {
            print_python_bytes(element);
        }
        else if (PyList_Check(element) || PyTuple_Check(element))
        {
            print_python_list(element);
        }
        else
        {
            printf("[ERROR] Unsupported Type\n");
        }
    }
}
