import os
DATA_DIR = "./data/syrip/images/train_pre_infant/"
index=1

for a in os.listdir(DATA_DIR):
    os.rename(DATA_DIR+a, DATA_DIR+"train"+str(index).zfill(5)+".jpg")
    index=index+1