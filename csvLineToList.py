
# CSVのレコードをカラムごとに分割し、リストを返却するメソッド
# 値にカンマを含むカラムに対応
# 制約1 ダブルクォーテーションはダブルクォーテーション二つにエスケープしておくこと
# 制約2 カンマを含むカラムはダブルクォーテーションで囲むこと

def csvLineToList(record):
    # レコード分割後のカラムリスト
    columns = []
    # ダブルクォーテーションのカウンタ
    dqCount = 0
    # カラムの先頭文字のインデックス
    colFirst = 0
    for i, c in enumerate(record):
        if c == "\"":
            dqCount += 1
        if i == len(record)-1:
            columns.append(record[colFirst + 1 : i])
            break
        # ダブルクォートで囲まれていないカラムはカンマで区切る 囲まれているカラムはダブルクォートが2つであること、次の文字がカンマであること
        f = 0 if (dqCount == 0 and record[i] == ",") else 1 if (dqCount != 0 and dqCount % 2 == 0 and record[i] == ",") else 2
        if f != 2:
            if f == 0:
                columns.append(record[colFirst : i])
            elif f == 1:
                columns.append(record[colFirst + 1 : i - 1])
            # 次のカラムの先頭文字位置を保持
            colFirst = i + 1
            # カウントを初期化
            dqCount = 0
    return columns