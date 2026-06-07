import torch

if torch.cuda.is_available():
    # 1. 텐서 생성 및 GPU 전송
    device = torch.device("cuda")
    x = torch.ones(1, 1, device=device) 
    
    # 2. 간단한 연산 테스트
    y = x + x
    
    print("성공: GPU에서 연산이 정상적으로 수행되었습니다.")
else:
    print("실패: GPU를 사용할 수 없는 상태입니다.")

# test_2