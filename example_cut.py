# encoding=utf-8
import jieba
import jieba.posseg as pos
import jieba.analyse as ana
import sys


def start():
    sentence = raw_input('請輸入句子：')

    # jieba.enable_parallel(2) # 開啟多執行緒，参数為Thread數
    # jieba.disable_parallel() # 關閉多執行緒

    use_dict = True        # 是否使用繁體詞庫
    use_user_dict = False  # 是否使用使用者自定義詞庫

    if use_dict:
        jieba.set_dictionary('dict/dict.txt.big')

    if use_user_dict:
        jieba.load_userdict('dict/user_dict.txt')

    getFullMode(sentence)
    getFullModeHMM(sentence)
    getAccurate(sentence)
    getAccurateHMM(sentence)
    getNewWord(sentence)
    getSearch(sentence)
    getPostag(sentence)
    getTokenize(sentence)
    getKeyWord(sentence)
    getKeyWord(sentence, 'TextRank')


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


def getPostag(sentence):
    print "詞性標註："
    cut_list = pos.cut(sentence)
    for word, postag in cut_list:
        print word, postag
    print('='*50)


def getTokenize(sentence):
    print "字詞位置："
    result = jieba.tokenize(unicode(sentence))  # 參數只接受unicode
    for tk in result:
        print tk[0] + '  b:' + str(tk[1]) + '  e:' + str(tk[2])
    print('='*50)


def getKeyWord(sentence, algorithm=None):
    if algorithm is None:
        print "關鍵字："
        result = ana.extract_tags(sentence, 3, True)  # sentence 为待提取的文本
                                                      # topK 為返回幾個 TF/IDF 權重最大的關鍵詞，預設值為20
                                                      # withWeight 為是否一併返回關鍵詞的權重值，預設值為False
                                                      # allowPOS 僅包括指定詞性的詞，預設值為空，即不篩選 allowPOS=('ns', 'n', 'vn', 'v')
    elif algorithm == 'TextRank':
        print "關鍵字(With TextRank)："
        result = ana.textrank(sentence, 3, True)

    for keyWord, weight in result:
        print keyWord + '  w:' + str(weight)
    print('='*50)


def printResult(title, result):
    print(title + "/ ".join(result))
    print('='*50)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    start()