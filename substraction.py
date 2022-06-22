#!/usr/bin/env python
# coding: utf-8

# In[22]:


pip install nibabel


# In[2]:


import nibabel as nib
import matplotlib.pyplot as plt
import os, glob
import shutil


# In[3]:


# 這個程式用來執行相減
# 必須輸入資料夾名稱
# 給他資料夾的名稱，他幫我找到該資料夾內所有的nii
def my_subtraction(folder_name: str):
    path = os.path.join(folder_name, '*.nii')

    files = glob.glob(path)
#    
#
    
    return files


#for file in files:
#        print(file)


# In[5]:


folder_name1 = r'G:\test2\20151126HSIAO_FANG_CHUN_92035656'
folder_name2 = r'G:\test2\20151201CHUANG_CHIN_PING_8994499'
folder_name3 = r'G:\test2\20151203CHEN_HSIN_HSIN_92046658'
folder_name4 = r'G:\test2\20160104LI_PI_CHING_92036989'
folder_name5= r'G:\test2\20160308_CHANG_CHIUNG_HUI_92474778'
folder_list = [folder_name1, folder_name2, folder_name3, folder_name4, folder_name5]


#a = my_subtraction(folder_name1)
#print(len(a))

#分成奇數堆跟偶數堆

paths = []
path = []
img1_odd_list = []
img2_even_list = []

for i in folder_list:
    paths = my_subtraction(i)
    for j in range(0,len(paths)):
        path = paths[j]
        if int(path[-10:-7]) % 2 == 1:
            img1_odd_list.append(path)
            img1_odd_list.sort()
        elif int(path[-10:-7]) % 2 == 0:
            img2_even_list.append(path)
            img2_even_list.sort()

# 使用for迴圈等，可方便的建立多個資料夾
# str.replace(old, new[, max])

new_folder_name_list = []
target_img = []
track_header = 'G:\\test2\\'
track = []

for k in range (len(folder_list)):
    new_folder_name = folder_list[k].replace('E:\\test2\\', "")
    new_folder_name_list.append(new_folder_name)


for i in range(len(new_folder_name_list)):
    new_folder_name = new_folder_name_list[i] + str(i)
    os.mkdir(new_folder_name)
    track_name =  new_folder_name
    track.append(track_name)
    track.sort()
    


# In[8]:


folder_name1 = r'G:\test\normalization\20151126HSIAO_FANG_CHUN_92035656'
folder_name2 = r'G:\test\normalization\20151201CHUANG_CHIN_PING_8994499'
folder_name3 = r'G:\test\normalization\20151203CHEN_HSIN_HSIN_92046658'
folder_name4 = r'G:\test\normalization\20160104LI_PI_CHING_92036989'
folder_name5= r'G:\test\normalization\20160308_CHANG_CHIUNG_HUI_92474778'
folder_list = [folder_name1, folder_name2, folder_name3, folder_name4, folder_name5]

#a = my_subtraction(folder_name1)
#print(len(a))

#分成奇數堆跟偶數堆

paths = []
path = []
img1_odd_list = []
img2_even_list = []

for i in folder_list:
    paths = my_subtraction(i)
    for j in range(len(paths)):
        path = paths[j]
        if int(path[-11:-7]) % 2 == 1:
            img1_odd_list.append(path)
            img1_odd_list.sort()
        elif int(path[-11:-7]) % 2 == 0:
            img2_even_list.append(path)
            img2_even_list.sort()

for i in range(len(img1_odd_list)):
    print('==' * 20)
    print(img1_odd_list[i])
    print(img2_even_list[i])


    


# In[7]:


# 偶數張減奇數張 (2-3)
# 後續必須用nibabel依序讀取img1_list及img2_list, 並將兩影像相減
# for i in range(len(img1_list)):
#     img1 = nib.load(img1_list[i+1])
#     img2 = nib.load(img2_list[i+1])
#     img1 = img1.get_fdata()
#     img2 = img2.get_fdata()
# ........

for m in range(len(img1_odd_list)):
    img1 = nib.load(img1_odd_list[m])
    img2 = nib.load(img2_even_list[m])
    img1_header = img1.header.copy()
    img1_affine = img1.affine.copy()
    img2_header = img1.header.copy()
    img2_affine = img1.affine.copy()
    img1 = img1.get_fdata()
    img2 = img2.get_fdata()
    img3 = img2 - img1
    new_img = nib.nifti1.Nifti1Image(img3, affine=img1_affine, header=img1_header)
    nib.save(new_img, f'ASL_{m}')

    

    


# In[9]:


# 奇數張減偶數張 (3-2)

for m in range(len(img1_odd_list)):
    img1 = nib.load(img1_odd_list[m])
    img2 = nib.load(img2_even_list[m])
    img1_header = img1.header.copy()
    img1_affine = img1.affine.copy()
    img2_header = img1.header.copy()
    img2_affine = img1.affine.copy()
    img1 = img1.get_fdata()
    img2 = img2.get_fdata()
    img3 = img1 - img2
    new_img = nib.nifti1.Nifti1Image(img3, affine=img1_affine, header=img1_header)
    nib.save(new_img, f'{m}')
    


# In[32]:


#target_folder = 'C:\\Users\\user\\Desktop\\test'
#C:\Users\user\Desktop\test\20150602_M057Y_TSAI_SANYI
# 使用glob.glob抓取該資料夾內的所有".nii"檔案

#paths = []
#for i in range(241):
#path = f'CHIU_HSUAN_TAO.MR.BRAIN_STUDY_NEURO_DR_CHEN.0006\user\\Desktop.{i+1:04}.xxx.IMA'
    #path = f'C:\\Users\\\test\\20150602_M057Y_TSAI_SANYI\\20150602_094000wep2dtrapaslASLs007a001_{i+1:03}.nii'
    #paths.append(path)
#for i in paths:
    #print(i)

# 使用for迴圈等，可方便的建立多個資料夾
# str.replace(old, new[, max])


    

    


# In[33]:


#img1_odd_list = []
#img2_even_list = []

#for path in paths[1:241]:
#if int(path[99:101]) % 2 == 1:
    #if int(path[93:95]) % 2 == 1:
        #img1_odd_list.append(path)
    #else:
        #img2_even_list.append(path)

#for i in range(len(img1_odd_list)):
    #print('==' * 20)
    #print(img1_odd_list[i])
    #print(img2_even_list[i])



# In[37]:





# In[38]:





# In[ ]:





# In[ ]:





# In[ ]:




