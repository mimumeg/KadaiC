# 課題C: ワードフィルタ
class WordFilter:
    def __init__(self, ngWord):
        # インスタンス変数
        self.ngWord = ngWord

    def detect(self, text):
        print("アーセナル" in text)
        # if self.ngWord == text:
        #     return True
        # else:
        #     return False

    def censor(self, text):
        print(text.replace("アーセナル", "<censored>"))

if __name__ == "__main__":
    my_filter = WordFilter("アーセナル")  # インスタンス化
    # print(my_filter.detect()) #確認用

    # NGワードが含まれている場合
    my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す

    # NGワードが含まれていない場合
    my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す

    # NGワードが含まれている場合
    my_filter.censor("昨日のアーセナルの試合アツかった！")  # "昨日の<censored>の試合アツかった！" を返す

    # NGワードが含まれていない場合
    my_filter.censor("昨日のリバプールの試合アツかった！")  # "昨日のリバプールの試合アツかった！" を返す
