https://lightly.teamcode.com/dashboard      

# Pytorch Quantization

PyTorch-Quantization is a toolkit for training and evaluating PyTorch models with simulated quantization. Quantization can be added to the model automatically, or manually, allowing the model to be tuned for accuracy and performance. Quantization is compatible with NVIDIAs high performance integer kernels which leverage integer Tensor Cores. The quantized model can be exported to ONNX and imported by TensorRT 8.0 and later.

PyTorch Quantization 是一个用于训练和评估具有模拟量化的PyTorch模型的工具包。量化可以自动或手动添加到模型中，允许对模型进行精度和性能调整。量化与NVIDIA高性能整型内核兼容，后者利用整型张量内核。量化模型可以导出到ONNX，并通过TensorRT 8.0及更高版本导入。

## Install From Source

```bash
git clone https://github.com/NVIDIA/TensorRT.git
cd tools/pytorch-quantization
```

Install PyTorch and prerequisites
```bash
pip install -r requirements.txt
# for CUDA 10.2 users
pip install torch>=1.9.1
# for CUDA 11.1 users
pip install torch>=1.9.1+cu111
```

Build and install pytorch-quantization
```bash
# Python version >= 3.7, GCC version >= 5.4 required
python setup.py install
```

## Resources

* Pytorch Quantization Toolkit [userguide](https://docs.nvidia.com/deeplearning/tensorrt/pytorch-quantization-toolkit/docs/userguide.html)
* Quantization Basics [whitepaper](https://arxiv.org/abs/2004.09602)

