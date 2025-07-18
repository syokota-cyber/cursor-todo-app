from todo import Todo
from datetime import datetime

def main():
    """メイン関数"""
    todo = Todo()
    
    print("=== ToDoリストアプリ ===")
    print("1. タスクを追加")
    print("2. タスク一覧を表示")
    print("3. 優先度別タスク表示")
    print("4. 期限別タスク表示")
    print("5. 期限切れタスク表示")
    print("6. タスクを完了にする")
    print("7. タスクを削除")
    print("8. 終了")
    
    while True:
        choice = input("\n選択してください (1-8): ")
        
        if choice == "1":
            title = input("タスクのタイトル: ")
            description = input("説明（省略可）: ")
            priority = input("優先度 (high/medium/low): ") or "medium"
            due_date = input("期限 (YYYY-MM-DD形式、省略可): ") or None
            
            task_id = todo.add_task(title, description, priority, due_date)
            print(f"タスクを追加しました。ID: {task_id}")
            
        elif choice == "2":
            tasks = todo.get_tasks()
            if not tasks:
                print("タスクがありません。")
            else:
                print("\n=== タスク一覧 ===")
                for task in tasks:
                    status = "✓" if task['completed'] else "□"
                    priority_icon = {"high": "🔴", "medium": "��", "low": "🟢"}.get(task['priority'], "⚪")
                    due_info = f" ��{task['due_date']}" if task.get('due_date') else ""
                    
                    # 期限切れチェック
                    if task.get('due_date') and not task['completed']:
                        today = datetime.now().strftime('%Y-%m-%d')
                        if task['due_date'] < today:
                            due_info += " ⚠️期限切れ"
                    
                    print(f"{task['id']}. [{status}] {priority_icon} {task['title']}{due_info}")
                    if task['description']:
                        print(f"   説明: {task['description']}")
                        
        elif choice == "3":
            priority = input("表示する優先度 (high/medium/low): ")
            tasks = todo.get_tasks_by_priority(priority)
            if not tasks:
                print(f"優先度 '{priority}' のタスクがありません。")
            else:
                print(f"\n=== 優先度 '{priority}' のタスク ===")
                for task in tasks:
                    status = "✓" if task['completed'] else "□"
                    priority_icon = {"high": "🔴", "medium": "��", "low": "🟢"}.get(task['priority'], "⚪")
                    due_info = f" ��{task['due_date']}" if task.get('due_date') else ""
                    print(f"{task['id']}. [{status}] {priority_icon} {task['title']}{due_info}")
                    if task['description']:
                        print(f"   説明: {task['description']}")
                        
        elif choice == "4":
            print("期限別表示オプション:")
            print("1. 期限ありのタスク")
            print("2. 期限なしのタスク")
            print("3. 今日が期限のタスク")
            
            sub_choice = input("選択してください (1-3): ")
            
            if sub_choice == "1":
                tasks = [task for task in todo.get_tasks() if task.get('due_date')]
                print("\n=== 期限ありのタスク ===")
            elif sub_choice == "2":
                tasks = [task for task in todo.get_tasks() if not task.get('due_date')]
                print("\n=== 期限なしのタスク ===")
            elif sub_choice == "3":
                today = datetime.now().strftime('%Y-%m-%d')
                tasks = [task for task in todo.get_tasks() if task.get('due_date') == today]
                print(f"\n=== 今日({today})が期限のタスク ===")
            else:
                print("無効な選択です。")
                continue
                
            if not tasks:
                print("該当するタスクがありません。")
            else:
                for task in tasks:
                    status = "✓" if task['completed'] else "□"
                    priority_icon = {"high": "🔴", "medium": "��", "low": "🟢"}.get(task['priority'], "⚪")
                    due_info = f" ��{task['due_date']}" if task.get('due_date') else ""
                    print(f"{task['id']}. [{status}] {priority_icon} {task['title']}{due_info}")
                    if task['description']:
                        print(f"   説明: {task['description']}")
                        
        elif choice == "5":
            overdue_tasks = todo.get_overdue_tasks()
            if not overdue_tasks:
                print("期限切れのタスクはありません。")
            else:
                print("\n=== 期限切れタスク ===")
                for task in overdue_tasks:
                    priority_icon = {"high": "🔴", "medium": "��", "low": "🟢"}.get(task['priority'], "⚪")
                    print(f"{task['id']}. {priority_icon} {task['title']} ⚠️期限: {task['due_date']}")
                    if task['description']:
                        print(f"   説明: {task['description']}")
                        
        elif choice == "6":
            task_id = int(input("完了にするタスクのID: "))
            if todo.complete_task(task_id):
                print("タスクを完了にしました。")
            else:
                print("タスクが見つかりません。")
                
        elif choice == "7":
            task_id = int(input("削除するタスクのID: "))
            if todo.delete_task(task_id):
                print("タスクを削除しました。")
            else:
                print("タスクが見つかりません。")
                
        elif choice == "8":
            print("アプリケーションを終了します。")
            break
            
        else:
            print("無効な選択です。")

if __name__ == "__main__":
    main()