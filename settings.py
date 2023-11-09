#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# 共通設定
# EDICT_BASE_DIR: 読み込み元の布告ディレクトリパス
# OUTPUT_DIR: 出力先ディレクトリパス
###############################################################################
EDICT_BASE_DIR = 'C:\Program Files (x86)\Steam\steamapps\common\Stellaris\common\edicts'
OUTPUT_DIR = '.\output'

###############################################################################
# 布告解析用の正規表現のpattern
###############################################################################
EDICT_START_PATTARN = r'^[a-zA-Z0-9]+.*{.*\n'
EDICT_END_PATTARN = r'^}\n'
EDICT_LENGTH_PATTARN = r'^.*length[ ]*=[ ]*(-1|@EdictPerpetual|@EdictDuration|@campaignDuration|@ambitionDuration).*\n'
EDICT_LOCK_PATTARN = r'^.*edict_lock_in_months.*\n'

###############################################################################
# 出力文字列
###############################################################################
ADD_PARAM = '	edict_lock_in_months = 12\n'
