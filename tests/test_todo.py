import unittest
import sys
import os

# プロジェクトルートディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.todo import Todo
from datetime import datetime

class TestTodo(unittest.TestCase):
    def setUp(self):
        """各テストの前に実行される"""
        self.todo = Todo()
    
    def test_add_task(self):
        """タスク追加のテスト"""
        task_id = self.todo.add_task("テストタスク", "テスト用", "high", "2025-07-25")
        self.assertIsInstance(task_id, int)
        self.assertEqual(len(self.todo.get_tasks()), 1)
        
        task = self.todo.get_task_by_id(task_id)
        self.assertEqual(task['title'], "テストタスク")
        self.assertEqual(task['description'], "テスト用")
        self.assertEqual(task['priority'], "high")
        self.assertEqual(task['due_date'], "2025-07-25")
        self.assertFalse(task['completed'])
    
    def test_complete_task(self):
        """タスク完了のテスト"""
        task_id = self.todo.add_task("完了テスト", "", "medium")
        self.assertTrue(self.todo.complete_task(task_id))
        
        task = self.todo.get_task_by_id(task_id)
        self.assertTrue(task['completed'])
    
    def test_delete_task(self):
        """タスク削除のテスト"""
        task_id = self.todo.add_task("削除テスト", "", "low")
        self.assertTrue(self.todo.delete_task(task_id))
        self.assertEqual(len(self.todo.get_tasks()), 0)
        
        # 存在しないタスクの削除
        self.assertFalse(self.todo.delete_task(999))
    
    def test_get_tasks_by_priority(self):
        """優先度別フィルタリングのテスト"""
        self.todo.add_task("高優先度", "", "high")
        self.todo.add_task("中優先度", "", "medium")
        self.todo.add_task("低優先度", "", "low")
        
        high_tasks = self.todo.get_tasks_by_priority("high")
        self.assertEqual(len(high_tasks), 1)
        self.assertEqual(high_tasks[0]['title'], "高優先度")
    
    def test_get_overdue_tasks(self):
        """期限切れタスクのテスト"""
        # 過去の日付でタスクを作成
        past_date = "2025-01-01"
        self.todo.add_task("期限切れタスク", "", "high", past_date)
        
        overdue_tasks = self.todo.get_overdue_tasks()
        self.assertEqual(len(overdue_tasks), 1)
        self.assertEqual(overdue_tasks[0]['title'], "期限切れタスク")
    
    def test_task_id_increment(self):
        """タスクIDの自動増加テスト"""
        id1 = self.todo.add_task("タスク1", "", "medium")
        id2 = self.todo.add_task("タスク2", "", "medium")
        id3 = self.todo.add_task("タスク3", "", "medium")
        
        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)
        self.assertEqual(id3, 3)
    
    def test_get_task_by_id(self):
        """IDによるタスク取得のテスト"""
        task_id = self.todo.add_task("IDテスト", "説明", "low")
        task = self.todo.get_task_by_id(task_id)
        
        self.assertIsNotNone(task)
        self.assertEqual(task['title'], "IDテスト")
        self.assertEqual(task['description'], "説明")
        
        # 存在しないID
        self.assertIsNone(self.todo.get_task_by_id(999))

if __name__ == '__main__':
    unittest.main()