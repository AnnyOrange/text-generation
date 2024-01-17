#!/bin/bash

MODEL_ID="timbrooks/instruct-pix2pix"
DATASET_ID="annyorange/Text-style-dataset"
OUTPUT_DIR="text-finetuned"

accelerate launch --mixed_precision="fp16" finetune_instruct_pix2pix.py \
  --pretrained_model_name_or_path="$MODEL_ID" \
  --dataset_name="$DATASET_ID" \
  --use_ema \
  --enable_xformers_memory_efficient_attention \
  --resolution=256 --random_flip \
  --train_batch_size=4 --gradient_accumulation_steps=4 --gradient_checkpointing \
  --max_train_steps=100 \
  --checkpointing_steps=50 --checkpoints_total_limit=2 \
  --learning_rate=5e-06 --lr_warmup_steps=0 \
  --mixed_precision=fp16 \
  --val_image_url="https://github.com/AnnyOrange/picture/blob/main/init.png?raw=true" \
  --val_gt_url="https://github.com/AnnyOrange/picture/blob/main/chgt.png?raw=true" \
  --validation_prompt="Convert the text in the picture to running script style." \
  --seed=42 \
  --output_dir="$OUTPUT_DIR" \
  --report_to=wandb \
  --push_to_hub
