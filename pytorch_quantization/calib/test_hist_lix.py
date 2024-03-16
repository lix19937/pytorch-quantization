
# https://lightly.teamcode.com/python
# https://lightly.teamcode.com/dashboard  

import numpy as np
from loguru import logger

# 第一个输入  
x_np = np.array([1,2,4,6,8,9,12,34])
_calib_hist, _calib_bin_edges = np.histogram(x_np, bins=5)

logger.info("(34-1)/5={}".format(33/5))
logger.info("_calib_bin_edges:{}".format(_calib_bin_edges)) # [ 1.   7.6 14.2 20.8 27.4 34. ]
logger.info(_calib_hist) # [4 3 0 0 1]

x_np = np.array([2,12,6,4,9,8,34,1])
_calib_hist, _calib_bin_edges = np.histogram(x_np, bins=5)
logger.info("_calib_bin_edges:{}".format(_calib_bin_edges)) # [ 1.   7.6 14.2 20.8 27.4 34. ]
logger.info(_calib_hist) # [4 3 0 0 1]

mm=np.max(x_np) 
x_np = np.array([[1,6,4,2],[8,9,12,34]])
mm2=np.max(x_np) 
logger.info("{}  {}".format(mm, mm2))  # 34  34

# 第二个输入  
x_np = np.array([1,0,14,16,3,9,12,45])

temp_amax = np.max(x_np)  # x_np的最大值，是一个单独的浮点数字   
if temp_amax > _calib_bin_edges[-1]: # 
    width = _calib_bin_edges[1] - _calib_bin_edges[0]  # 计算范围     
    new_bin_edges = np.arange(_calib_bin_edges[-1] + width, temp_amax + width, width) # 拓展区域 
    logger.info("new_bin_edges:{}".format(new_bin_edges))
    _calib_bin_edges = np.hstack((_calib_bin_edges, new_bin_edges)) # 水平方向拼接  
    logger.info("_calib_bin_edges:{}".format(_calib_bin_edges))

hist, _calib_bin_edges = np.histogram(x_np, bins=_calib_bin_edges) # 再次进入 直方图统计  
logger.info("_calib_hist:{}".format(_calib_hist))
logger.info("hist:{}".format(hist))

hist[:len(_calib_hist)] += _calib_hist
_calib_hist = hist
logger.info("hist:{}".format(hist))

centers = (_calib_bin_edges[1:] + _calib_bin_edges[:-1]) / 2
logger.info("centerszz:{}".format(_calib_bin_edges[1:]))
logger.info("centersxx:{}".format(_calib_bin_edges[:-1]))

logger.info("centers:{}".format(centers))


nbins = 16; i = 4
space = np.linspace(0, i, num=nbins + 1)
logger.info("space:{}".format(space))

digitized_space = np.digitize(range(i), space) - 1
logger.info("digitized_space:{}".format(digitized_space))

