# Python metaArray

Wrapper for combining numpy ndarrays with meta information.

## Description

Wrapper for combining numpy ndarrays with meta information. Also has useful utilities; for example, reading in data files from PZFlex, binary data from oscilloscopes, talking to impedance analysers, etc.

## Get Started

### Dependencies

* Python >= 3.7.
* `h5py`, `matplotlib >= 3.5`, `numpy`, `pyserial`, `scipy`; all are installed automatically through `pip install` process, see below.

### Build

From the top level of the repository directory,

```bash
pip install --upgrade build
python -m build
```

these generated packages can be found in `dist` directory:

* `metaArray-1.1.7b1.tar.gz`
* `metaArray-1.1.7b1-py3-none-any.whl`

### Installing

Install `metaArray` from local wheel package,

```bash
pip install metaArray-1.1.7b1-py3-none-any.whl
```

**Optional**: in case `matplotlib` fails to draw the figure and presents this warning message "UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.", one can install extra dependency to fix it,

```bash
pip install 'metaArray[gui] @ file:///<full-path-to>/metaArray-1.1.7b1-py3-none-any.whl'
```

the `gui` extra installs Python package `PyQT5` that provides `matplotlib` with working graphic backend.

### Development

It's recommended to use `virtualenv` to setup the development context as below,

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

Currently only supports linear sampling. Ring buffer hehaviour (e.g. -ve index) is not supported, for it may cause confusion in xyz space.

Slice stepping is not supported, use `metaFunc.metaResample` instead.

```Python
object = metaArray(numpy.ndarray)

object.data  # the Numpy ndarray storage container
object.info  # the dict meta information container
```

If the requested index or slice object is `int`, no index translation is performed

```Python
object[int].data == object.data[int]
```

If the requested index or slice object is `float`, then it is assumed to be in x-y-z space, and will be rounded to the nearest i-j-k index before obtaining the data.

```Python
object[float] === object[x,y,z]
```

The x-y-z space is defined in such a way that, if `object.ndim == 3`:

```Python
object.info['range'] = {'begin':(x0,y0,z0), 'end':(x1,y1,z1)}
```

All mathmetical operations are x-y-z space aware, in a exclusion mode.

```Python
A = metaArray(dataA)
B = metaArray(dataB)
c = A + B  # === A[x,y,z] + B[x,y,z]
```

such that Cx,Cy,Cz will be the overlaping section between Ax,Ay,Az and Bx,By,Bz. If they do not overlap, then `c = None`.
    
Addition and subtraction requires both `metaArray` has the same unit description string, else an `UnitError` exception will be raised.

Unit definitions are default to `None`, i.e. `undefined/Arb`. Unitless quantities should be assigned empty string '' for unit description.

Module comes with demonstration function to illustrate `metaArray` usage. In Python shell:

```
>>> import metaArray
>>> metaArray.demo()
```

