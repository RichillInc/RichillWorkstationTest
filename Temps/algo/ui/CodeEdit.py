# -*- encoding: utf-8 -*-

'''
* @File    :   CodeEdit.py
* @Time    :   2021/02/06 22:38:15
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython



class CodeEdit(QsciScintilla):
    """ 代碼編輯 """

    DEFAULT_FONT_FAMLIY = "Consolas" # 預設的字型
    DEFAULT_FONT_SIZE = 10 # 預設的字體大小


    def __init__(self):
        super(CodeEdit, self).__init__()
    

        font = QFont()
        font.setFamily(CodeEdit.DEFAULT_FONT_FAMLIY)
        font.setPointSize(CodeEdit.DEFAULT_FONT_SIZE)        
        font.setFixedPitch(True)
        fontMetrics = QFontMetrics(font)

        self.resize(1000, 1000)
        self.setFont(font) # 設置字體
        self.setMarginsFont(font) # 設置邊距字體
        self.setMarginWidth(0, 30) # 設置邊距寬度
        self.setMarginsBackgroundColor(QColor("#ffffe9")) # 設置邊距顏色
        self.setMarginLineNumbers(0, True)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch) # Set brace matching
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0) # 隱藏水平滾動條
        self.setFolding(True) # 設置代碼可折疊
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#ffffe9")) # 設置當前列的背景顏色
        self.setAutoIndent(True) # 設置換行後自動縮進
        self.setUtf8(True) # 設置支持中文字串

        
        # 自動補全代碼
        self.setAutoCompletionSource(QsciScintilla.AcsAll) # 設定自動補全對於所有Ascii字符
        self.setAutoCompletionThreshold(1) # 輸入多少字才跳出補全提示
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionReplaceWord(False)

        # 使用縮排
        self.setIndentationsUseTabs(False)
        self.setTabWidth(4) # 設置Tab縮排數量
        self.setIndentationGuides(True)
        
        self.setLexer(self.__createPythonLexer(font)) # 設置語法分析器



    def __createPythonLexer(self, font):
        """ 創建Python語法分析器 """
        lexer = QsciLexerPython()
        lexer.setDefaultFont(font)
        return lexer





if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = CodeEdit()
    widget.show()
    app.exec_()

    
    