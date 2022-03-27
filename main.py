import cv2 as cv
import numpy as np

path = "assets/"
filename = "img"
ext = ".jpg"
suffix_to_save = "processed"

def main(path,filename,suffix_to_save,ext): 
    # Ler imagem inserindo o PATH do arquivo
    img = cv.imread(path+filename+ext,cv.IMREAD_COLOR)

    #Obtendo o tamanho do arquivo
    hei,wid = img.shape[:2]
    print("Height = {},  Width = {}".format(hei, wid))

    

    for index, vet in enumerate(img):

        print("{}% Concluido".format(int(index/np.size(img,0) * 100 )))

        for col in range(int(wid/2)):
            img[index][col] = [200,67,100]

    img_saved = cv.imwrite(path+filename+suffix_to_save+ext,img)

    if (img_saved!=True):
        print("FALHA ao salvar imagem!")
        exit()
    else:
        print("Imagem SALVA com SUCESSO!")
    
main(path,filename,suffix_to_save,ext)
