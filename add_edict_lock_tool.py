#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import settings
import os
import re
import pathlib
import filecmp

def main():
	if not os.path.exists(settings.OUTPUT_DIR):
		os.mkdir(settings.OUTPUT_DIR)

	# 全ての布告ファイルに対して実施
	files = pathlib.Path(settings.EDICT_BASE_DIR).glob('*.txt')
	for file in files:
		# ファイルパス設定
		input_file = os.path.join(settings.EDICT_BASE_DIR, file.name)
		output_file = os.path.join(settings.OUTPUT_DIR, file.name)
		write_edict(input_file, output_file)

		# 出力内容が読み込み元と全く変わらなかったファイルについては不要なので削除する
		if filecmp.cmp(input_file, output_file, shallow=True):
			os.remove(output_file)


def write_edict(input_file, output_file):
	# ファイル出力開始
	with open(output_file, 'w', encoding='utf-8') as wf:
		convert_edict(input_file, wf)


def convert_edict(input_file, wf):
	with open(input_file) as rf:
		# 読み込み中のデータ行が、個別の布告のパラメータを見ているかどうか
		is_parameter_line = False
		exist_perpetual_length_param = False
		exist_lock_param = False

		for line in rf:
			# 内部パラメータの行に入るまでは、そのまま読み込んだ行を出力する
			if not is_parameter_line:
				if re.fullmatch(settings.EDICT_START_PATTARN, line):
					is_parameter_line = True
				wf.writelines(line)
				continue

			# 内部パラメータの行から抜ける時に、特定のパラメータの有無を確認し
			# 条件に一致すれば「edict_lock_in_months = 12」を追加で付与する
			if re.fullmatch(settings.EDICT_END_PATTARN, line):
				if exist_perpetual_length_param and not exist_lock_param:
					wf.writelines(settings.ADD_PARAM)
				wf.writelines(line)

				# 変数は初期化しておく
				is_parameter_line = False
				exist_perpetual_length_param = False
				exist_lock_param = False
				continue

			# 内部パラメータの行に入ったら、特定のパラメータがあるかどうかを調査する
			if re.fullmatch(settings.EDICT_LENGTH_PATTARN, line):
				exist_perpetual_length_param = True
			elif re.fullmatch(settings.EDICT_LOCK_PATTARN, line):
				exist_lock_param = True
			wf.writelines(line)


if __name__ == "__main__":
	main()