import numpy as np
from jnius import autoclass
from .utils import *

AbstractNdArray = autoclass('ndarrays4j.arrays.AbstractNdArray')
NdFloatArray = autoclass('ndarrays4j.arrays.real.NdFloatArray')
NdDoubleArray = autoclass('ndarrays4j.arrays.real.NdDoubleArray')
NdByteArray = autoclass('ndarrays4j.arrays.integer.NdByteArray')
NdUnsignedByteArray = autoclass('ndarrays4j.arrays.integer.NdUnsignedByteArray')
NdShortArray = autoclass('ndarrays4j.arrays.integer.NdShortArray')
NdUnsignedShortArray = autoclass('ndarrays4j.arrays.integer.NdUnsignedShortArray')
NdIntArray = autoclass('ndarrays4j.arrays.integer.NdIntArray')
NdUnsignedIntArray = autoclass('ndarrays4j.arrays.integer.NdUnsignedIntArray')
NdLongArray = autoclass('ndarrays4j.arrays.integer.NdLongArray')
NdUnsignedLongArray = autoclass('ndarrays4j.arrays.integer.NdUnsignedLongArray')

numpy_to_java_dtype = {
    np.dtype('float32'):NdFloatArray,
    np.dtype('float64'): NdDoubleArray,
    np.dtype('int8'): NdByteArray,
    np.dtype('uint8'): NdUnsignedByteArray,
    np.dtype('int16'): NdShortArray,
    np.dtype('uint16'): NdUnsignedShortArray,
    np.dtype('int32'): NdIntArray,
    np.dtype('uint32'): NdUnsignedIntArray,
    np.dtype('int64'): NdLongArray,
    np.dtype('uint64'): NdUnsignedLongArray
}


def to_java(np_arr):
    if not np_arr.dtype in numpy_to_java_dtype:
        raise NotImplementedError("Can not convert dtype to java type yet: {}".format(np_arr.dtype))
    else:
        address = get_address(np_arr)
        strides = [int(i) for i in np.array(np_arr.strides)/np_arr.itemsize]
        shape = np_arr.shape
        if np_arr.flags['CARRAY']:
            return numpy_to_java_dtype[np_arr.dtype](address, shape, strides, AbstractNdArray.ORDER_C)
        else:
            return numpy_to_java_dtype[np_arr.dtype](address, shape, strides, AbstractNdArray.ORDER_F)
