## 基类     
+ calibrator.py    

```py
class _Calibrator():
    """Abstract base class of calibrators
    Args:
        num_bits: An integer. Number of bits of quantization.
        axis    : A tuple. see QuantDescriptor.
        unsigned: A boolean. using unsigned quantization.
    Readonly Properties: axis:
    """
    def __init__(self, num_bits, axis, unsigned):
        self._num_bits = num_bits; self._axis = axis; self._unsigned = unsigned

    # 收集器   
    def collect(self, x):
        # Abstract method: collect tensor statistics used to compute amax
        raise NotImplementedError

    def reset(self):
        # Abstract method: reset calibrator to initial state  
        raise NotImplementedError

    # 计算
    def compute_amax(self, *args, **kwargs):
        # Abstract method: compute the amax from the collected data,  Returns: amax: a tensor
        raise NotImplementedError

    def __repr__(self):
        s = "num_bits={_num_bits}"; s += " axis={_axis}"; s += " unsigned={_unsigned}"
        return s.format(**self.__dict__)
```
------------------------------
## 派生类    
+ max.py   
    class MaxCalibrator(_Calibrator):

+ histogram.py    
  class HistogramCalibrator(_Calibrator):

------------------   
+ hist-mse   
![hist-mse](https://github.com/lix19937/pytorch-quantization/assets/38753233/60658195-3084-44b3-a08b-14473546e845)

我们找到使 mse 最小的amax 即 centers[i]     
