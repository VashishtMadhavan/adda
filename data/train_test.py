import os
import glob

cityscapes_path = "/home/vashisht/data/cityscapes/"
train_label_path = os.path.join( cityscapes_path , "gtFine"   , "train" , "*" , "*_gt*_labelTrainIds.png")
val_label_path =  os.path.join( cityscapes_path , "gtFine"   , "val" , "*" , "*_gt*_labelTrainIds.png")

train_label_files = glob.glob(train_label_path)
val_label_files = glob.glob(val_label_path)

train_image_files = []
for t in train_label_files:
	image_file = t.replace('gtFine', 'leftImg8bit').replace('_gtFine_labelTrainIds.png', '_leftImg8bit.png')
	train_image_files.append(image_file)

val_image_files = []
for v in val_label_files:
	image_file = t.replace('gtFine', 'leftImg8bit').replace('_gtFine_labelTrainIds.png', '_leftImg8bit.png')
	val_image_files.append(image_file)


with open('cityscapes/train_image_rel.txt','w') as f:
	for x in train_image_files:
		f.write('%s\n' % x)

with open('cityscapes/train_label_rel.txt','w') as f:
	for x in train_label_files:
		f.write('%s\n' % x)

with open('cityscapes/val_image_rel.txt','w') as f:
	for x in val_image_files:
		f.write('%s\n' % x)

with open('cityscapes/val_label_rel.txt','w') as f:
	for x in val_label_files:
		f.write('%s\n' % x)

