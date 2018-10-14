#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AquaMagicのデータファイル(.bin)を読みこんで、画像(.png)と海底深度(.csv)を出力する
#
# 引数
#   第一引数:input_filename AquaMagicのデータファイル(.bin)のパス
#   第二引数:output_folder  画像と海底深度の出力ディレクトリ。省略時は、binと同じディレクトリに出力される。
# 
# 作成日：2018/10/08
# 作成者：大石卓司



# 引数処理 test
def get_args():
    parser = argparse.ArgumentParser(description='Convert from AquaMagic data to PNG file')

    parser.add_argument("input_filename", help="File path where AquaMagic data is located", nargs=None)
    parser.add_argument("output_folder", help="Derectory path where you want to save PNG & CSV files", nargs='?',default=False)

    args = parser.parse_args()
    return(args)

# メイン関数
def main():
    print('hello')
    print('bye')
    print('branch1')

if __name__ == '__main__':
    main()