#每次需要改的地方有
#path(存放的是bdd的json文件)
#"/home/zhongzhixing01/桌面/val/val_name_new.txt" 为存放pic路径的txt文件
#'/home/zhongzhixing01/下载/BDD100k/bdd100k_images/images/100k/val/' 存放图片的路径
#"/home/zhongzhixing01/桌面/val/val_label/" 生成每个图片的txt
#同理，train这里也需要改变三个
import pandas as pd
path = '/home/zhongzhixing01/PycharmProjects/my_project/get_label_from_kdd/bdd100k_labels/labels'
train_name = '/bdd100k_labels_images_train.json'
val_name = '/bdd100k_labels_images_val.json'
train_label = pd.read_json(path+train_name)
val_label = pd.read_json(path+val_name)

num_pictures = len(val_label['name'])
print('总的图片数为：'+str(num_pictures))

j=0
with open("/home/zhongzhixing01/桌面/val/val_name_new.txt","w") as f_name:
    for index,name_id in enumerate(val_label['name']):
        s = name_id
        xinxi = ''
        #对每行的数据进行遍历
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
            name_id_name = '/home/zhongzhixing01/下载/BDD100k/bdd100k_images/images/100k/val/'+name_id+'\n'
            f_name.write(name_id_name)
            with open("/home/zhongzhixing01/桌面/val/val_label/"+name_id[:-4]+'.txt',"w") as f:
                f.write(xinxi)
print('done')



num_pictures = len(train_label['name'])
print('总的图片数为：'+str(num_pictures))
j=0
r_num = 0
name_red = ''
with open("/home/zhongzhixing01/桌面/train/train_name_new.txt","w") as f_name:
    for index,name_id in enumerate(train_label['name']):
        flag = 0
        s = name_id
        xinxi = ''
        #对每行的数据进行遍历
        if index%100 == 0:
            print(index)
        xinxi = ''
        for i in range(len(train_label['labels'][index])): 
            #如果分类是交通灯的话  红0 绿1 黄2 无3
            if train_label['labels'][index][i]['category'] == 'traffic light':
                if train_label['labels'][index][i]['attributes']['trafficLightColor'] == 'red':
                    class_light = 0
                    flag = 1
                    
                
                elif train_label['labels'][index][i]['attributes']['trafficLightColor'] == 'green':
                    class_light = 1
                    
                    
                elif train_label['labels'][index][i]['attributes']['trafficLightColor'] == 'yellow':
                    
                    class_light = 2
                else:
                    
                    class_light =3
                num1 = train_label['labels'][index][i]['box2d']['x1']
                num2 = train_label['labels'][index][i]['box2d']['y1']
                num3 = train_label['labels'][index][i]['box2d']['x2']
                num4 = train_label['labels'][index][i]['box2d']['y2']
                #图片的信息，自己找的，如果其他数据这里需要修改
                h = 720
                w = 1280
                j =j+1
                xinxi = xinxi+str(class_light)+' ' +str(((num1+num3)/2.0)/w)+' '+str(((num2+num4)/2.0)/h)+' '+str((num3-num1)/w)+' '+str((num4-num2)/h)+'\n'
        if xinxi == '':
            continue
        else:
            if flag ==1:
                name_red = name_red+'/home/zhongzhixing01/下载/BDD100k/bdd100k_images/images/100k/train/'+name_id+'\n'
            name_id_name = '/home/zhongzhixing01/下载/BDD100k/bdd100k_images/images/100k/train/'+name_id+'\n'
            f_name.write(name_id_name)
            with open("/home/zhongzhixing01/桌面/train/train_label/"+name_id[:-4]+'.txt',"w") as f:
                f.write(xinxi)
        if flag ==1:
            r_num = r_num+1

with open("/home/zhongzhixing01/桌面/red_name.txt","w") as f:  
    f.write(name_red)
print(r_num)
print('done')
