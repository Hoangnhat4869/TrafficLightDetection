import os
import shutil

# os.makedirs('./taolao', exist_ok=True)
# os.makedirs('./taolao/train', exist_ok=True)
# os.makedirs('./taolao/valid', exist_ok=True)
# os.makedirs('./taolao/train/images', exist_ok=True)
# os.makedirs('./taolao/train/labels', exist_ok=True)
# os.makedirs('./taolao/valid/images', exist_ok=True)
# os.makedirs('./taolao/valid/labels', exist_ok=True)

data1_imgtrainpath = './dataset/train/images'
data1_imgvalpath = './dataset/valid/images'
data1_lbltrainpath = './dataset/train/labels'
data1_lblvalpath = './dataset/valid/labels'

data2_imgtrainpath = './signdataset/images/train'
data2_imgvalpath = './signdataset/images/val'
data2_lbltrainpath = './signdataset/labels/train'
data2_lblvalpath = './signdataset/labels/val'

train_path = './data/train'
val_path = './data/valid'

# def copyfile(src, dest):
#     for file in os.listdir(src):
#         shutil.copy(src + '/' + file, dest)

# copyfile(data1_imgtrainpath, train_path + '/images')
# copyfile(data1_lbltrainpath, train_path + '/labels')
# copyfile(data1_imgvalpath, val_path + '/images')
# copyfile(data1_lblvalpath, val_path + '/labels')

# copyfile(data2_imgtrainpath, train_path + '/images')
# copyfile(data2_lbltrainpath, train_path + '/labels')
# copyfile(data2_imgvalpath, val_path + '/images')
# copyfile(data2_lblvalpath, val_path + '/labels')

# ## Because of the different datasets, we need to relabel the data.
# import os

# ## ['Green Light', 'Red Light', 'Speed Limit 10', 'Speed Limit 100', 'Speed Limit 110', 'Speed Limit 120',
# ## 'Speed Limit 20', 'Speed Limit 30', 'Speed Limit 40', 'Speed Limit 50', 'Speed Limit 60', 'Speed Limit 70',
# ## 'Speed Limit 80', 'Speed Limit 90', 'Stop', 'No pedestrian crossing', 'No parking', 'Parking',
# ## 'Give way', 'One way', 'No left turn', 'Speed limit', 'Bus lane', 'Pedestrian crossing']
# def newlabel(label):
#   labelchange = {'0': '0', '1': '1', '2': '2', '3': '2', '4': '2', '5': '2',
#                  '6': '2', '7': '2', '8': '2', '9': '2', '10': '2', '11': '2',
#                  '12': '2', '13': '2', '14': '3', '15': '4', '16': '5', '17': '6',
#                  '18': '7', '19': '8', '20': '9', '21': '2', '22': '10', '23': '11'}
#   return labelchange[label]

# def changelabel(labelpath, labelcount):
#   for f in os.listdir(labelpath):
#     path = labelpath + '/' + f
#     with open(path, 'r') as file:
#       content = file.readlines()
#       newcontent = []
#       for c in content:
#         labelarr = c.split(' ')
#         labelarr[0] = newlabel(labelarr[0])
#         labelcount[labelarr[0]] += 1
#         c = ' '.join(labelarr)
#         newcontent.append(c)
#       with open(path, 'w') as file:
#         file.writelines(newcontent)
#   print(labelcount)

# labelcount = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
#               '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0,
#               '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0,
#               '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
# print(len(os.listdir(train_path + '/labels')))
# label_train_path = train_path + '/labels'
# changelabel(label_train_path, labelcount)

# # count_label(label_train_path, labelcount)

# labelcount = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
#               '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0,
#               '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0,
#               '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
# print(len(os.listdir(val_path + '/labels')))
# label_val_path = val_path + '/labels'
# changelabel(label_val_path, labelcount)

# count_label(label_val_path, labelcount)

labelpath = train_path + '/labels'
labelcount = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
              '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0,
              '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0,
              '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
def count_label(labelpath, labelcount):
  for f in os.listdir(labelpath):
    path = labelpath + '/' + f
    with open(path, 'r') as file:
        lines = file.readlines()
        for label_line in lines:
          lbl = label_line.split(' ')[0]
          labelcount[lbl] += 1
  print(labelcount)
count_label(labelpath, labelcount)

print(len(os.listdir(train_path + '/images')))
print(len(os.listdir(train_path + '/labels')))
print(len(os.listdir(val_path + '/images')))
print(len(os.listdir(val_path + '/labels')))

for i in range(len(os.listdir(train_path + '/images'))):
    if os.listdir(train_path + '/images')[i][:-3] != os.listdir(train_path + '/labels')[i][:-3]:
      print('error')
      break
for i in range(len(os.listdir(val_path + '/images'))):
    if os.listdir(val_path + '/images')[i][:-3] != os.listdir(val_path + '/labels')[i][:-3]:
      print('========', os.listdir(val_path + '/images')[i][:-3], os.listdir(val_path + '/labels')[i][:-3])
      print('error')
      break
print('done')
