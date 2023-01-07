#!/bin/bash

export PYTHONPATH=.: 

python train.py \
 --summary_comment=cleaned_words_all_def_min_upvotes_20_max_len_40_min_len_4_no_upper_randomized__urban_dictionary_cleaned_all_def_lr_0_00005_tw1 \
 --output_dir=models/urban_dictionary_cleaned_all_def_lr_0_00005_tw1 \
 --model_type=gpt2 \
 --model_name_or_path=gpt2 \
 --do_train \
 --train_data_file=data/cleaned_words_all_def_min_upvotes_20_max_len_40_min_len_4_no_upper_randomized.pickle \
 --do_eval \
 --eval_data_file=data/cleaned_words_all_def_min_upvotes_20_max_len_40_min_len_4_no_upper_randomized.pickle \
 --per_gpu_train_batch_size 2 \
 --per_gpu_eval_batch_size 2 \
 --gradient_accumulation_steps 2 \
 --urban_dictionary_dataset \
 --splits 0.95 --splits 0.05 \
 --train_split_idx 0 --eval_split_idx 1 \
 --title_scale 1.0 \
 --evaluate_during_training \
 --save_steps 10000 \
 --logging_steps 5000 \
 --eval_subsampling 0.2 \
 --learning_rate 0.00005 \
 --block_size 768 \
 --num_train_epochs 5 \
 --should_continue
