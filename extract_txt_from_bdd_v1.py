##path 为json文件的路径
##train_name为bdd100k_labels_images_train.json
##val_pic_dir = '/home/zhongzhixing01/下载/BDD100k/bdd100k_images/images/100k/val/' 为val图片路径
#val_txt_dir = "/home/zhongzhixing01/桌面/val/val_label/" 为用来保存txt的文件夹
#val_save_pic_path = "/home/zhongzhixing01/桌面/val/val_name_new.txt" 为用来保存图片路径的txt
import pandas as pd
path = '/home/zhongzhixing01/PycharmProjects/my_project/get_label_from_kdd/bdd100k_labels/labels'

val_name = '/bdd100k_labels_images_val.json'

val_label = pd.read_json(path+val_name)
val_pic_dir = '/home/zhongzhixing01/下载/BDD100k/bdd100k_images/images/100k/val/'
val_txt_dir = '/home/zhongzhixing01/桌面/val/val_label/'
val_save_pic_path = '/home/zhongzhixing01/桌面/val/val_name_new.txt'

#val
num_pictures = len(val_label['name'])
print('总的图片数为：'+str(num_pictures))
j=0
with open(val_save_pic_path,"w") as f_name:
    for index,name_id in enumerate(val_label['name'][:1000]):
        s = name_id
        xinxi = ''
        if index%100 == 0:
            print(index)
        xinxi = ''
        for i in range(len(val_label['labels'][index])):
            #如果分类是交通灯的话  红0 绿1 黄2 无3
            if val_label['labels'][index][i]['category'] == 'traffic light':
                if val_label['labels'][index][i]['attributes']['trafficLightColor'] == 'red':
                    class_light = 0
                elif val_label['labels'][index][i]['attributes']['trafficLightColor'] == 'green':
                    class_light = 1
                elif val_label['labels'][index][i]['attributes']['trafficLightColor'] == 'yellow':
                    class_light = 2
                else:
                    class_light =3
                num1 = val_label['labels'][index][i]['box2d']['x1']
                num2 = val_label['labels'][index][i]['box2d']['y1']
                num3 = val_label['labels'][index][i]['box2d']['x2']
                num4 = val_label['labels'][index][i]['box2d']['y2']
                #图片的信息，自己找的，如果其他数据#train_name = '/bdd100k_labels_images_train.json'
                h = 720
                w = 1280
                j =j+1
                xinxi = xinxi+str(class_light)+' ' +str(((num1+num3)/2.0)/w)+' '+str(((num2+num4)/2.0)/h)+' '+str((num3-num1)/w)+' '+str((num4-num2)/h)+'\n'
        if xinxi == '':
            continue
        else:
            name_id_name = val_pic_dir+name_id+'\n'
            f_name.write(name_id_name)
            with open(val_txt_dir+name_id[:-4]+'.txt',"w") as f:
                
                f.write(xinxi)
print('done')

