todo_list = []

while True:
    command = input("コマンドを入力してください(add/show/done/exit): ")

    if command == "add":
        task = input("追加するタスク: ")
        todo_list.append(task)
        print("追加しました:", task)

    elif command == "show":
        print("【現在のタスク】")
        for i,task in enumerate(todo_list):
            print(f"{i + 1}. {task}")

    elif command == "done":
        index = int(input("完了したタスクの番号: ")) - 1
        if 0 <= index <len(todo_list):
            completed = todo_list.pop(index)
            print("完了しました", completed)
        else:
            print("その番号は存在しません")

    elif command == "exit":
        print("アプリを終了します。お疲れ様でした！")
        break

    else:
        print("不明なコマンドです")