#cifar100 e200 bs128  gs  2,4,8,16
import os,time


os.system("CUDA_VISIBLE_DEVICES=0,1,2,3 python -m torch.distributed.launch --nproc_per_node=4  --master_addr 127.0.0.2 --master_port 29502 main.py /home/yonghw/data/ImageNet/  --model r18  -b 256 --lr 0.1 --wd 0.0001 --alg wsgd ")


