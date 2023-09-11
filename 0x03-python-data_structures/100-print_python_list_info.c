#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	long int size, i = 0;
	PyListObject *obj = (PyListObject *)p;

	size = PyList_Size(p);

	if (!PyList_Check(p))
	{
		PyErr_Print();
		return;
	}

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	while (i < size)
	{
		printf("Element %li: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
		i++;
	}
}
