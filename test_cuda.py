import torch
print(f"CUDA是否可用: {torch.cuda.is_available()}")
print(f"当前设备: {torch.cuda.current_device()}")
print(f"设备名称: {torch.cuda.get_device_name(0)}")
print(torch.tensor(1).to('cuda'))