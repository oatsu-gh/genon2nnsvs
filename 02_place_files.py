#!/usr/bin/env python3
# Copyright (c) 2020 oatsu
"""
学習しやすいように、各音響モデルごとにファイルを配置する。
"""
from distutils.dir_util import copy_tree
from os import makedirs
from os.path import abspath, basename, dirname, isdir, join


def place_files_for_each_model(out_dir):
    """
    そのまま学習できるように、
    acoustic, duration, timelag フォルダ以下に各ファイルを複製する。
    """
    full_align_dir_in = join(out_dir, 'label_phone_align')
    full_score_dir_in = join(out_dir, 'label_phone_score')
    wav_dir_in = join(out_dir, 'wav')

    acoustic_dir = join(out_dir, 'acoustic')
    duration_dir = join(out_dir, 'duration')
    timelag_dir = join(out_dir, 'timelag')
    makedirs(acoustic_dir, exist_ok=True)
    makedirs(duration_dir, exist_ok=True)
    makedirs(timelag_dir, exist_ok=True)

    print(f'Copying files to {acoustic_dir}')
    copy_tree(full_align_dir_in, join(acoustic_dir, 'label_phone_align'))
    copy_tree(full_score_dir_in, join(acoustic_dir, 'label_phone_score'))
    copy_tree(wav_dir_in, join(acoustic_dir, 'wav'))
    print(f'Copying files to {duration_dir}')
    copy_tree(full_align_dir_in, join(duration_dir, 'label_phone_align'))
    copy_tree(full_align_dir_in, join(duration_dir, 'label_phone_score'))
    print(f'Copying files to {timelag_dir}')
    copy_tree(full_align_dir_in, join(timelag_dir, 'label_phone_align'))
    copy_tree(full_align_dir_in, join(timelag_dir, 'label_phone_score'))

    print('All files were successfully copied.')


def main():
    """
    フォルダを指定して処理を実行
    """
    out_dir = 'data'
    place_files_for_each_model(out_dir)


if __name__ == '__main__':
    main()
