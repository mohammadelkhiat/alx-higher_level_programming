#include <Python.h>
#include <stdio.h>
#include <unistd.h>

/**
 * print_python_bytes - Printing Bytes
 * Return: Void
*/

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", Py_SIZE(bytes));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    size_t i;
    for (i = 0; i < Py_SIZE(bytes) && i < 10; ++i) {
        printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Printing List
 * Return: Void
*/
void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));
    printf("[*] Allocated = %ld\n", list->allocated);

    size_t i;
    for (i = 0; i < Py_SIZE(list); ++i) {
        printf("Element %ld: ", i);
        PyObject *element = PyList_GET_ITEM(p, i);
        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        } else if (PyList_Check(element)) {
            print_python_list(element);
        } else if (PyTuple_Check(element)) {
            print_python_list(element);
        } else if (PyFloat_Check(element)) {
            printf("float\n");
        } else if (PyLong_Check(element)) {
            printf("int\n");
        } else if (PyUnicode_Check(element)) {
            printf("str\n");
        } else {
            printf("[ERROR] Unsupported Type\n");
        }
    }
}
