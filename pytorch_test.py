import torch



print(f"CUDA 가능 여부: {torch.cuda.is_available()}")

print(f"사용 가능 GPU 개수: {torch.cuda.device_count()}")

print(f"현재 GPU 이름: {torch.cuda.get_device_name(0)}")