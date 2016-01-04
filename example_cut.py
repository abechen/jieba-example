#encoding=utf-8
import jieba
import sys


def start():
    sentence = raw_input('請輸入句子：')
    use_dict = True #是否使用繁體詞庫

    if use_dict:
        jieba.set_dictionary('dict/dict.txt.big')

    getFullMode(sentence)
    getFullModeHMM(sentence)
    getAccurate(sentence)
    getAccurateHMM(sentence)
    getNewWord(sentence)
    getSearch(sentence)


def getFullMode(sentence):
    cut_list = jieba.cut(sentence, cut_all=True)
    printResult("全模式：", cut_list)


def getFullModeHMM(sentence):
    cut_list = jieba.cut(sentence, cut_all=True, HMM=True)
    printResult("全模式(HMM)：", cut_list)


def getAccurate(sentence):
    cut_list = jieba.cut(sentence, cut_all=False)
    printResult("精確模式：", cut_list)


def getAccurateHMM(sentence):
    cut_list = jieba.cut(sentence, cut_all=False, HMM=True)
    printResult("精確模式(HMM)：", cut_list)


def getNewWord(sentence):
    cut_list = jieba.cut(sentence)
    printResult("新詞識別：", cut_list)


def getSearch(sentence):
    cut_list = jieba.cut_for_search(sentence)
    printResult("搜尋引擎模式：", cut_list)


def printResult(title, result):
    print(title + "/ ".join(result))

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    start()
