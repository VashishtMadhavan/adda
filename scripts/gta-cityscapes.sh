#!/bin/bash

# abort entire script on error
set -e

# train base model on GTA
python tools/train.py gta train vgg_dilation vgg_dilation_gta \
       --iterations 10000 \
       --batch_size 128 \
       --display 10 \
       --lr 0.001 \
       --snapshot 5000 \
       --solver adam

# run adda GTA->Cityscapes
python tools/train_adda.py gta:train cityscapes:train vgg_dilation adda_vgg_dilation_gta_city \
       --iterations 10000 \
       --batch_size 128 \
       --display 10 \
       --lr 0.0002 \
       --snapshot 5000 \
       --weights snapshot/lenet_svhn \
       --adversary_relu \
       --solver adam

# evaluate trained models
echo 'GTA only baseline:'
python tools/eval_segmentation.py gta train vgg_dilation snapshot/vgg_dilation_gta

echo 'ADDA':
python tools/eval_segmentation.py cityscapes train vgg_dilation snapshot/adda_vgg_dilation_gta_city
