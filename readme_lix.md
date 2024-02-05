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
