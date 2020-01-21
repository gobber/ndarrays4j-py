import numpy as np
import ctypes
from jnius import autoclass

AbstractNdArray = autoclass('ndarrays4j.arrays.AbstractNdArray')

java_to_numpy_dtype = {
    AbstractNdArray.FLOAT: np.dtype('float32'),
    AbstractNdArray.DOUBLE: np.dtype('float64'),
    AbstractNdArray.BYTE: np.dtype('int8'),
    AbstractNdArray.U_BYTE: np.dtype('uint8'),
    AbstractNdArray.SHORT: np.dtype('int16'),
    AbstractNdArray.U_SHORT: np.dtype('uint16'),
    AbstractNdArray.INT: np.dtype('int32'),
    AbstractNdArray.U_INT: np.dtype('uint32'),
    AbstractNdArray.LONG: np.dtype('int64'),
    AbstractNdArray.U_LONG: np.dtype('uint64')
}

ctype_conversions_java = {
    AbstractNdArray.FLOAT: ctypes.c_float,
    AbstractNdArray.DOUBLE: ctypes.c_double,
    AbstractNdArray.BYTE: ctypes.c_int8,
    AbstractNdArray.U_BYTE: ctypes.c_uint8,
    AbstractNdArray.SHORT: ctypes.c_int16,
    AbstractNdArray.U_SHORT: ctypes.c_uint16,
    AbstractNdArray.INT: ctypes.c_int32,
    AbstractNdArray.U_INT: ctypes.c_uint32,
    AbstractNdArray.LONG: ctypes.c_int64,
    AbstractNdArray.U_LONG: ctypes.c_uint64
}


def to_numpy(java_arr):
    dtype = java_arr.dtype()
    if not dtype in java_to_numpy_dtype:
        raise NotImplementedError("Can not convert java to dtype yet: {}".format(dtype))
    else:
        address = java_arr.address()
        order = 'C' if java_arr.order() == AbstractNdArray.ORDER_C else 'F'
        pointer = ctypes.cast(address, ctypes.POINTER(ctype_conversions_java[dtype]))
        shape = tuple(java_arr.shape())
        return np.ndarray(shape=shape, dtype=java_to_numpy_dtype[dtype], buffer=np.ctypeslib.as_array(pointer, shape=shape), order=order)
