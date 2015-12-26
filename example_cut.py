#encoding=utf-8
import jieba
import sys

class JiebaDemo:
	def start(self):
		self.sentence = raw_input('請輸入句子：')
		self.getFullMode()
		self.getFullModeHMM()
		self.getAccurate()
		self.getAccurateHMM()
		self.getNewWord()
		self.getSearch()

	def getFullMode(self):
		cut_list = jieba.cut(self.sentence, cut_all=True)
		self.printResult("全模式：", cut_list)

	def getFullModeHMM(self):
		cut_list = jieba.cut(self.sentence, cut_all=True, HMM=True)
		self.printResult("全模式(HMM)：", cut_list)

	def getAccurate(self):
		cut_list = jieba.cut(self.sentence, cut_all=False)
		self.printResult("精確模式：", cut_list)

	def getAccurateHMM(self):
		cut_list = jieba.cut(self.sentence, cut_all=False, HMM=True)
		self.printResult("精確模式(HMM)：", cut_list)

	def getNewWord(self):
		cut_list = jieba.cut(self.sentence)
		self.printResult("新詞識別：", cut_list)

	def getSearch(self):
		cut_list = jieba.cut_for_search(self.sentence)
		self.printResult("搜尋引擎模式：", cut_list)


	def printResult(self, title, result):
		print(title + "/ ".join(result))


if __name__ == '__main__':
	reload(sys)  
	sys.setdefaultencoding('utf8')
	JiebaDemo().start()
	
