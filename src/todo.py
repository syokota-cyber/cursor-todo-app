class Todo:
    def __init__(self):
        """ToDoリストを初期化"""
        self.tasks = []
    
    def add_task(self, title, description="", priority="medium", due_date=None):
        """新しいタスクを追加
        
        Args:
            title (str): タスクのタイトル
            description (str): タスクの説明（省略可）
            priority (str): 優先度（high/medium/low）
            due_date (str): 期限（YYYY-MM-DD形式）
            
        Returns:
            int: 追加されたタスクのID
        """
        # 既存のタスクから最大IDを取得
        max_id = 0
        for task in self.tasks:
            if task['id'] > max_id:
                max_id = task['id']
        
        # 新しいIDは最大ID + 1
        new_id = max_id + 1
        
        task = {
            'id': new_id,
            'title': title,
            'description': description,
            'priority': priority,
            'due_date': due_date,
            'completed': False,
            'created_at': '2025-07-17'  # 簡易版（実際はdatetime.now()を使う）
        }
        self.tasks.append(task)
        return task['id']
    
    def get_tasks(self):
        """全てのタスクを取得
        
        Returns:
            list: タスクリスト
        """
        return self.tasks
    
    def get_task_by_id(self, task_id):
        """IDでタスクを取得
        
        Args:
            task_id (int): タスクID
            
        Returns:
            dict: タスク情報（見つからない場合はNone）
        """
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def complete_task(self, task_id):
        """タスクを完了にする
        
        Args:
            task_id (int): タスクID
            
        Returns:
            bool: 成功した場合True、失敗した場合False
        """
        task = self.get_task_by_id(task_id)
        if task:
            task['completed'] = True
            return True
        return False
    
    def delete_task(self, task_id):
        """タスクを削除
        
        Args:
            task_id (int): タスクID
            
        Returns:
            bool: 成功した場合True、失敗した場合False
        """
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[i]
                return True
        return False
    
    def get_tasks_by_priority(self, priority):
        """優先度でタスクをフィルタリング
        
        Args:
            priority (str): 優先度（high/medium/low）
            
        Returns:
            list: 指定された優先度のタスクリスト
        """
        return [task for task in self.tasks if task['priority'] == priority]
    
    def get_overdue_tasks(self):
        """期限切れのタスクを取得
        
        Returns:
            list: 期限切れのタスクリスト
        """
        from datetime import datetime
        today = datetime.now().strftime('%Y-%m-%d')
        overdue_tasks = []
        
        for task in self.tasks:
            if task.get('due_date') and task['due_date'] < today and not task['completed']:
                overdue_tasks.append(task)
        
        return overdue_tasks
    
    def display_tasks(self):
        """タスク一覧を表示"""
        if not self.tasks:
            print("タスクがありません")
            return
        
        print("\n=== ToDoリスト ===")
        for task in self.tasks:
            status = "✓" if task['completed'] else "□"
            priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(task['priority'], "⚪")
            due_info = f" (期限: {task['due_date']})" if task.get('due_date') else ""
            
            print(f"{status} {priority_icon} ID:{task['id']} - {task['title']}{due_info}")
            if task['description']:
                print(f"   説明: {task['description']}")
        print()


# 使用例
if __name__ == "__main__":
    todo = Todo()
    
    # タスクを追加
    todo.add_task("買い物", "牛乳とパンを買う", "high", "2025-07-20")
    todo.add_task("掃除", "部屋の掃除", "medium", "2025-07-25")
    todo.add_task("読書", "技術書を読む", "low")
    
    # タスク一覧を表示
    todo.display_tasks()
    
    # 期限切れタスクを確認
    overdue = todo.get_overdue_tasks()
    if overdue:
        print("期限切れタスク:")
        for task in overdue:
            print(f"- {task['title']} (期限: {task['due_date']})")
    else:
        print("期限切れタスクはありません")# バグのある変更 - revert練習用
