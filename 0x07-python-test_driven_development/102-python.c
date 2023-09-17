#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p)
{
    long int length;

    fflush(stdout);

    printf("[.] string object info\n");
    if (strcmp(Py_TYPE(p)->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = ((PyASCIIObject *)(p))->length;

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}