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


if __name__ == "__main__":
    my_filter = WordFilter("アーセナル")  # インスタンス化
    # print(my_filter.detect()) #確認用

    # NGワードが含まれている場合
    my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す

    # NGワードが含まれていない場合
    my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す ※出力されるわけではありません！
