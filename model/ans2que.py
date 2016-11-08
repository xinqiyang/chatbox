#-*- coding:utf8 -*-

'问题-答案'

__author__='litterzhang'

import json

# 问题与答案之间的对应关系
# que_id : 问题id
# ans_ids : 答案ids
class Ans2Que(object):
	def __init__(self, _que_id, _ans_ids):
		self.que_id = _que_id
		self.ans_ids = _ans_ids

	def ansque2dict(ans2que):
		return {
			'que_id' : ans2que.que_id,
			'ans_ids' : ans2que.ans_ids
		}

	def dict2ansque(dic):
		return Ans2Que(dic['que_id'], dic['ans_ids'])

	def load(fp):
		ans2ques = list()
		with open(fp, 'r', encoding='utf-8') as fr:
			ans2ques = json.load(fr, object_hook=Ans2Que.dict2ansque)
		return ans2ques