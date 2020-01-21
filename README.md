# ndarrays4j-py

The `ndarrays4j-py` is a package to connect [ndarrays4j](https://github.com/gobber/ndarrays4j-unsafe) with python `numpy` arrays. 
As ndarrays4j allocates memory outside the JVM we can **share memory** from it to 
`numpy` arrays. This means that, we dont need to copy data! All this is inspired in
[imglyb](https://github.com/imglib/imglyb).

## Support

`ndarrays4j-py` connects the following representations:  

| Numpy dtype | Java ndarray4j |
| ------------ | ------------ |
| np.dtype('float32') | NdFloatArray|
| np.dtype('float64') | NdDoubleArray|
| np.dtype('int8') | NdByteArray |
| np.dtype('uint8') | NdUnsignedByteArray |
| np.dtype('int16') | NdShortArray |
| np.dtype('uint16') | NdUnsignedShortArray |
| np.dtype('int32') | NdIntArray |
| np.dtype('uint32') | NdUnsignedIntArray |
| np.dtype('int64') | NdLongArray |
| np.dtype('uint64') | NdUnsignedLongArray |

## Dependencies

`ndarrays4j-py` depends on the following python dependencies:

```
python >= 3
pyjnius
numpy
```

Of course, this package only makes sense if you are using [ndarrays4j](https://github.com/gobber/ndarrays4j-unsafe), then you must download
it and add to the java classpath before call any `ndarrays4j-py` method.

## Installation

We recommend to make an installation using pip:

```
$ pip install ndarrays4j
```

If you are using jupyter notebooks consider to install `ndarrays4j-py` through a notebook cell. Then, you can type and execute the following:

```
import sys
!{sys.executable} -m pip install ndarrays4j
```

## Usage

Currently this package only support non-complex numpy arrays (see Support section). 
First of all, your `JAVA_HOME` must be correct configured.    

### Minimal usage example

This is a simple example of usage. We will share a numpy array with a 
ndarrays4j. First, we need the following imports and configurations:

```python
# Configure java in pyjnius
import numpy as np
import jnius_config
ndarrays4j_path = '' # put here the path of ndarrays4j classes 
jnius_config.set_classpath('.', 
                           ndarrays4j_path)
```

Now import `ndarrays4j-py`:

```python
import ndarrays4j
```

Let create a numpy random array and get it address:

```python
# Create a numpy array
arr = np.random.rand(10, 3)

# Get address and print it
print(ndarrays4j.get_address(arr))
```

Now we will share this array with ndarrays4j:

```python
# Convert in java NdArray
arr_java = ndarrays4j.to_java(arr)

# Get adress (must be same as above)
print(arr_java.address())
```

Now we will back to another numpy array
```python
# Reference back to a numpy array
arr_back = ndarrays4j.to_numpy(arr_java)

# Get adress (must be same as above)
print(ndarrays4j.get_address(arr_back))
```

We will alter a position in numpy, it will be reflected in any other
reference:

```python
# Modify in arr_back and reflect in arr and arr_java since They are all the same 
# thanks to memory sharing :)
arr_back[0, 2] = 90

# Print to proof
print(arr[0, 2])
print(arr_java.get(0, 2))
```

## Questions

If you have any question please send me a mail <charles26f@gmail.com>.