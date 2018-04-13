import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.misc
def load_csv(path = "../raw_data"):
    data = np.loadtxt(os.path.join(path, "labels.csv"), dtype=int, delimiter=",")
    return data.T.flatten()

def load_images(path = "../processed_data",height = 60,width = 60):
    folders = os.listdir(path)
    folders = [int(i) for i in folders]
    folders = sorted(folders)
    images = np.empty((len(folders)*64,height,width,1)) # 1 for grayscale
    for i in folders: #folders start at one, images start at zero
        cur_path = os.path.join(path,str(i),"squares")
        files = os.listdir(cur_path)
        files = [int(i.split(".")[0]) for i in files]
        files = sorted(files)
        for j in files:
            index = (i-1)*64+j
            image = scipy.misc.imread(os.path.join(cur_path,str(j)+".jpg"),mode="L")
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            images[index,:,:,:] = image.reshape((height,width,1))
    return images

def rotate(images,labels):
    r_images = np.empty([images.shape[0]*3]+list(images.shape[1:]))
    r_labels = np.empty((labels.shape[0]*3,))
    for i in range(images.shape[0]):
        r_images[i*3,:,:,:] = np.rot90(images[i,:,:,:],k=1,axes=(0,1))
        r_labels[i*3] = labels[i]
        r_images[i * 3+1, :, :, :] = np.rot90(images[i, :, :, :], k=2, axes=(0, 1))
        r_labels[i * 3+1] = labels[i]
        r_images[i * 3+2, :, :, :] = np.rot90(images[i, :, :, :], k=3, axes=(0, 1))
        r_labels[i * 3+2] = labels[i]
    return r_images,r_labels

def flip(images,labels):
    f_images = np.empty([images.shape[0]*2]+list(images.shape[1:]))
    f_labels = np.empty((labels.shape[0]*2,))
    for i in range(images.shape[0]):
        f_images[i*2,:,:,:] = np.flip(images[i,:,:,:],0)
        f_labels[i*2] = labels[i]
        f_images[i * 2+1, :, :, :] = np.flip(images[i, :, :, :],1)
        f_labels[i*2+1] = labels[i]
    return f_images,f_labels
def shift(images,labels,displacement=1):
    ...
def main():
    raw_path = os.path.join('../raw_data')
    processed_path = os.path.join('../processed_data')
    labels = load_csv(raw_path)
    images = load_images(processed_path)
    r_images, r_labels = rotate(images,labels)
    f_images, f_labels = flip(images,labels)
    image_data = np.concatenate((images,r_images,f_images))
    image_labels = np.concatenate((labels,r_labels,f_labels))
    np.save("images.npy",image_data)
    np.save("labels.npy",image_labels)
    # plt.imshow(images[0,:,:,:])
    # plt.show()
    # plt.imshow(f_images[0,:,:,:])
    # plt.show()
    # plt.imshow(f_images[1,:,:,:])
    # plt.show()
    #print(labels)
    #print(images)

if __name__ == "__main__":
    main()
