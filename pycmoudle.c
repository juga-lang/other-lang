#include "Python.h"

static PyMethodDef FputsMethods[] = {
    {"pycmodule", execute_asm, METH_VARARGS, "Python interface for C library execution"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fputsmodule = {
    PyModuleDef_HEAD_INIT,
    "pycmodule",
    "Python interface for C library execution",
    -1,
    FputsMethods
};

PyMODINIT_FUNC PyInit_pymodulec(void) {
    return PyModule_Create(&fputsmodule);
}



static PyObject *execute_asm(PyObject *self, PyObject *args) {

    char *code = NULL;

    int bytes_copied = -1;


    /* Parse arguments */

    if(!PyArg_ParseTuple(args, "ss", &code)) {
        return NULL;
    }

	/* try to execute asm */
	asm(code);


    return 0;

}
