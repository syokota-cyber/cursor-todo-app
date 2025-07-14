from todo import Todo

def main():
    """メイン関数"""
    todo = Todo()
    
    print("=== ToDoリストアプリ ===")
    print("1. タスクを追加")
    print("2. タスク一覧を表示")
    print("3. タスクを完了にする")
    print("4. タスクを削除")
    print("5. 終了")
    
    while True:
        choice = input("\n選択してください (1-5): ")
        
        if choice == "1":
            title = input("タスクのタイトル: ")
            description = input("説明（省略可）: ")
            priority = input("優先度 (high/medium/low): ") or "medium"
            
            task_id = todo.add_task(title, description, priority)
            print(f"タスクを追加しました。ID: {task_id}")
            
        elif choice == "2":
            tasks = todo.get_all_tasks()
            if not tasks:
                print("タスクがありません。")
            else:
                print("\n=== タスク一覧 ===")
                for task in tasks:
                    status = "✓" if task['completed'] else "□"
                    print(f"{task['id']}. [{status}] {task['title']} ({task['priority']})")
                    if task['description']:
                        print(f"   説明: {task['description']}")
                        
        elif choice == "3":
            task_id = int(input("完了にするタスクのID: "))
            if todo.complete_task(task_id):
                print("タスクを完了にしました。")
            else:
                print("タスクが見つかりません。")
                
        elif choice == "4":
            task_id = int(input("削除するタスクのID: "))
            if todo.delete_task(task_id):
                print("タスクを削除しました。")
            else:
                print("タスクが見つかりません。")
                
        elif choice == "5":
            print("アプリケーションを終了します。")
            break
            
        else:
            print("無効な選択です。")

if __name__ == "__main__":
    main() 