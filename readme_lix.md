from  TensorRT-release-8.6   

```
echo "# pytorch-quantization" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/lix19937/pytorch-quantization.git
git push -u origin main
```


分析 不同的calib 方法适应 何种网络  `稀疏`,  `稠密`,  `conv 1*1`       
+ 交叉熵  
+ 百分位数 
+ mse      


稠密网络 用百分位数 calib 一定有效吗？


除了 kl散度，还有其他衡量的指标吗？  
