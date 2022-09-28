import torch, cv2
import numpy as np

size=256
num_training=100
lr=100

random_tensor=torch.randn((size,size,3),dtype=torch.float)
#clip(x,min,max) : min보다 작은값은 min, max보다 큰값은 max로 변환
random_tensor=torch.clip(random_tensor,min=-1.0,max=1.0)


###random tensor visualization
#0~2의 범위로 변경하기 위해
#거기다 2를 나눠 0~1사이의 범위로 변경한 후에
#*255.0을 해 0~255사이의 범위로 최종변경한다.
vis_rt=(random_tensor+1)/2*255.0
vis_rt=vis_rt.numpy()
#cv2.imshow('rt',vis_rt.astype(np.uint8))
#cv2.waitKey(-1)

###training - 원래부터 255값이기때문에 변경 x
target=cv2.imread('./images/dog1.jpg')
target=cv2.resize(target,(size,size))
cv2.imshow('target',target)
#cv2.waitKey(-1)


#안정적이게 하기 위해 -1~1범위로 변경해주기
target=(target/255.0)*2-1
target=torch.from_numpy(target)

for it in range(num_training):
    random_tensor.requires_grad_(True)
    # mean을 하는 이유 : 각 픽셀마다의 값이 다 나오는거니까 그것들의 평균을 구함
    loss=torch.mean((target-random_tensor)**2)
    #loss=torch.mean(torch.abs(target-random_tensor)
    loss.backward()

    with torch.no_grad():
        #자동 미분
        random_tensor=random_tensor-lr*random_tensor.grad

    print('it : %d loss val : %.5f'%(it,loss))

    vis_rt=(random_tensor+1)/2*255.0
    vis_rt=vis_rt.numpy()
    cv2.imshow('rt' ,vis_rt.astype(np.uint8))
    cv2.waitKey(1)


