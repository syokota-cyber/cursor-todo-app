class Todo:
    """ToDoリストを管理するクラス"""
    
    def __init__(self):
        """初期化：タスクリストを空で作成"""
        self.tasks = []
    
    def add_task(self, title, description="", priority="medium"):
        """新しいタスクを追加
        
        Args:
            title (str): タスクのタイトル
            description (str): タスクの説明（省略可）
            priority (str): 優先度（high/medium/low）
            
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
            'completed': False,
            'created_at': '2025-07-17'  # 簡易版（実際はdatetime.now()を使う）
        }
        self.tasks.append(task)
        return task['id']
    
    def get_all_tasks(self):
        """全てのタスクを取得
        
        Returns:
            list: タスクのリスト
        """
        return self.tasks
    
    def get_task_by_id(self, task_id):
        """IDでタスクを取得
        
        Args:
            task_id (int): タスクのID
            
        Returns:
            dict or None: タスク情報（見つからない場合はNone）
        """
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def complete_task(self, task_id):
        """タスクを完了にする
        
        Args:
            task_id (int): 完了にするタスクのID
            
        Returns:
            bool: 成功した場合はTrue、失敗した場合はFalse
        """
        task = self.get_task_by_id(task_id)
        if task:
            task['completed'] = True
            return True
        return False
    
    def delete_task(self, task_id):
        """タスクを削除
        
        Args:
            task_id (int): 削除するタスクのID
            
        Returns:
            bool: 成功した場合はTrue、失敗した場合はFalse
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
            list: 指定した優先度のタスクリスト
        """
        return [task for task in self.tasks if task['priority'] == priority]
    
    def get_completed_tasks(self):
        """完了済みのタスクを取得
        
        Returns:
            list: 完了済みタスクのリスト
        """
        return [task for task in self.tasks if task['completed']]
    
    def get_pending_tasks(self):
        """未完了のタスクを取得
        
        Returns:
            list: 未完了タスクのリスト
        """
        return [task for task in self.tasks if not task['completed']]