# daz : Denormals are zeros
The tool to change the CPU flag about denormals number.

[![pypi](https://img.shields.io/pypi/v/daz.svg)](https://pypi.python.org/pypi/daz)
[![GitHub license](https://img.shields.io/github/license/chainer/daz.svg)](https://github.com/chainer/daz)
[![travis](https://img.shields.io/travis/chainer/daz/master.svg)](https://travis-ci.org/chainer/daz)

  * **DAZ** (Denormals-Are-Zero) treats denormal inputs as zero
  * **FTZ** (Flush-To-Zero) writes zero for denormal outputs


# Application

On x86-64 CPUs with 64-bit programs, the CPUs SSE unit performs the floating point operations.
When it comes to calculate with denormal (aka. subnormal) numbers, there are performance penalties.

If your specific use-case doesn't require highest precision with small numbers,
these can be treated as - or rounded to - zero.
This is achieved by setting the CPU-flags.
When doing so, the calculations won't be slowed down by factors!

In python, especially [NumPy](https://numpy.org/) functions show a measurable benefit.


# Usage

basic functional use:
```python
import daz
daz.set_ftz()
daz.set_daz()
daz.unset_ftz()
daz.unset_daz()
daz.get_ftz()
daz.get_daz()
```

alternative 1:
```python
from daz import DAZ
# prev_daz: bool = DAZ.set_daz(daz: bool | None = True)
# prev_ftz: bool = DAZ.set_ftz(ftz: bool | None = True)
prev_daz = DAZ.set_daz(True)
prev_ftz = DAZ.set_ftz()
```

alternative 2:
```python
from daz import DAZ

# DAZ(daz: bool = True, ftz: bool = True)
with DAZ():
    # daz and ftz set True
    pass

with DAZ(False, True):
    # daz unset, but ftz set True
    pass
```
