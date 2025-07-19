#!/usr/bin/env python3
"""
🎓 DSA Study Guide & Progress Tracker
====================================

An interactive tool to guide your Data Structures and Algorithms learning journey.
"""

import os
import json
from datetime import datetime, timedelta
from collections import defaultdict


class DSAStudyGuide:
    def __init__(self):
        self.progress_file = "progress.json"
        self.load_progress()
        
        # Define the complete curriculum
        self.curriculum = {
            "01_arrays_strings": {
                "name": "Arrays & Strings",
                "estimated_days": 14,
                "problems": [
                    {"name": "Two Sum", "difficulty": "Easy", "pattern": "Hash Map"},
                    {"name": "Valid Anagram", "difficulty": "Easy", "pattern": "Hash Map"},
                    {"name": "Contains Duplicate", "difficulty": "Easy", "pattern": "Hash Set"},
                    {"name": "Best Time to Buy Stock", "difficulty": "Easy", "pattern": "One Pass"},
                    {"name": "Valid Parentheses", "difficulty": "Easy", "pattern": "Stack"},
                    {"name": "Longest Substring", "difficulty": "Medium", "pattern": "Sliding Window"},
                    {"name": "3Sum", "difficulty": "Medium", "pattern": "Two Pointers"},
                    {"name": "Container With Water", "difficulty": "Medium", "pattern": "Two Pointers"},
                ]
            },
            "02_linked_lists": {
                "name": "Linked Lists",
                "estimated_days": 10,
                "problems": [
                    {"name": "Reverse Linked List", "difficulty": "Easy", "pattern": "Iterative"},
                    {"name": "Merge Two Lists", "difficulty": "Easy", "pattern": "Two Pointers"},
                    {"name": "Cycle Detection", "difficulty": "Easy", "pattern": "Floyd's Algorithm"},
                    {"name": "Remove Nth Node", "difficulty": "Medium", "pattern": "Two Pointers"},
                    {"name": "Add Two Numbers", "difficulty": "Medium", "pattern": "Math"},
                ]
            },
            "03_stacks_queues": {
                "name": "Stacks & Queues",
                "estimated_days": 8,
                "problems": [
                    {"name": "Valid Parentheses", "difficulty": "Easy", "pattern": "Stack"},
                    {"name": "Min Stack", "difficulty": "Easy", "pattern": "Design"},
                    {"name": "Daily Temperatures", "difficulty": "Medium", "pattern": "Monotonic Stack"},
                ]
            },
            "04_trees": {
                "name": "Trees",
                "estimated_days": 16,
                "problems": [
                    {"name": "Invert Binary Tree", "difficulty": "Easy", "pattern": "DFS"},
                    {"name": "Max Depth", "difficulty": "Easy", "pattern": "DFS/BFS"},
                    {"name": "Same Tree", "difficulty": "Easy", "pattern": "DFS"},
                    {"name": "Level Order", "difficulty": "Medium", "pattern": "BFS"},
                    {"name": "Validate BST", "difficulty": "Medium", "pattern": "DFS"},
                ]
            },
            "05_heaps": {
                "name": "Heaps",
                "estimated_days": 8,
                "problems": [
                    {"name": "Kth Largest", "difficulty": "Easy", "pattern": "Min Heap"},
                    {"name": "Top K Frequent", "difficulty": "Medium", "pattern": "Heap"},
                ]
            },
            "06_hash_tables": {
                "name": "Hash Tables",
                "estimated_days": 6,
                "problems": [
                    {"name": "Group Anagrams", "difficulty": "Medium", "pattern": "Hash Map"},
                    {"name": "Subarray Sum", "difficulty": "Medium", "pattern": "Prefix Sum"},
                ]
            },
            "07_graphs": {
                "name": "Graphs",
                "estimated_days": 14,
                "problems": [
                    {"name": "Number of Islands", "difficulty": "Medium", "pattern": "DFS/BFS"},
                    {"name": "Course Schedule", "difficulty": "Medium", "pattern": "Topological Sort"},
                ]
            },
        }
    
    def load_progress(self):
        """Load progress from JSON file."""
        try:
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        except FileNotFoundError:
            self.progress = {
                "problems_solved": {},
                "daily_goals": {},
                "start_date": datetime.now().isoformat(),
                "study_streak": 0,
                "total_problems": 0
            }
    
    def save_progress(self):
        """Save progress to JSON file."""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def mark_problem_solved(self, topic, problem_name, difficulty, notes=""):
        """Mark a problem as solved."""
        today = datetime.now().strftime("%Y-%m-%d")
        
        if topic not in self.progress["problems_solved"]:
            self.progress["problems_solved"][topic] = {}
        
        self.progress["problems_solved"][topic][problem_name] = {
            "solved_date": today,
            "difficulty": difficulty,
            "notes": notes
        }
        
        self.progress["total_problems"] += 1
        self.update_streak()
        self.save_progress()
        
        print(f"✅ Marked '{problem_name}' as solved!")
        print(f"🎯 Total problems solved: {self.progress['total_problems']}")
    
    def update_streak(self):
        """Update study streak."""
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        
        if today not in self.progress["daily_goals"]:
            if yesterday in self.progress["daily_goals"]:
                self.progress["study_streak"] += 1
            else:
                self.progress["study_streak"] = 1
            
            self.progress["daily_goals"][today] = True
    
    def show_dashboard(self):
        """Display progress dashboard."""
        print("\n" + "="*60)
        print("📊 DSA LEARNING DASHBOARD")
        print("="*60)
        
        # Overall progress
        total_available = sum(len(topic["problems"]) for topic in self.curriculum.values())
        solved = self.progress["total_problems"]
        progress_percent = (solved / total_available) * 100 if total_available > 0 else 0
        
        print(f"🎯 Overall Progress: {solved}/{total_available} problems ({progress_percent:.1f}%)")
        print(f"🔥 Study Streak: {self.progress['study_streak']} days")
        
        # Progress bar
        bar_length = 30
        filled = int(bar_length * progress_percent / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"📈 Progress: [{bar}] {progress_percent:.1f}%")
        
        # Topic breakdown
        print(f"\n📚 Topic Progress:")
        for topic_id, topic_data in self.curriculum.items():
            topic_solved = len(self.progress["problems_solved"].get(topic_id, {}))
            topic_total = len(topic_data["problems"])
            topic_percent = (topic_solved / topic_total) * 100 if topic_total > 0 else 0
            status = "✅" if topic_percent == 100 else "🔄" if topic_percent > 0 else "⏳"
            
            print(f"  {status} {topic_data['name']}: {topic_solved}/{topic_total} ({topic_percent:.0f}%)")
    
    def show_current_focus(self):
        """Show what to focus on today."""
        print("\n" + "="*60)
        print("🎯 TODAY'S FOCUS")
        print("="*60)
        
        # Find current topic (first incomplete)
        current_topic = None
        for topic_id, topic_data in self.curriculum.items():
            solved_in_topic = len(self.progress["problems_solved"].get(topic_id, {}))
            if solved_in_topic < len(topic_data["problems"]):
                current_topic = (topic_id, topic_data)
                break
        
        if not current_topic:
            print("🎉 Congratulations! You've completed all topics!")
            return
        
        topic_id, topic_data = current_topic
        solved_problems = set(self.progress["problems_solved"].get(topic_id, {}).keys())
        
        print(f"📖 Current Topic: {topic_data['name']}")
        print(f"⏱️ Estimated Time: {topic_data['estimated_days']} days")
        
        print(f"\n📝 Problems to solve:")
        for i, problem in enumerate(topic_data["problems"], 1):
            status = "✅" if problem["name"] in solved_problems else "⏳"
            print(f"  {i}. {status} {problem['name']} ({problem['difficulty']}) - {problem['pattern']}")
        
        # Next problem suggestion
        next_problem = None
        for problem in topic_data["problems"]:
            if problem["name"] not in solved_problems:
                next_problem = problem
                break
        
        if next_problem:
            print(f"\n🔥 Next Problem: {next_problem['name']}")
            print(f"   Difficulty: {next_problem['difficulty']}")
            print(f"   Pattern: {next_problem['pattern']}")
            print(f"   Tip: Look for this pattern in the solution!")
    
    def show_weekly_plan(self):
        """Show weekly study plan."""
        print("\n" + "="*60)
        print("📅 WEEKLY STUDY PLAN")
        print("="*60)
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        activities = [
            "Review theory + 1 easy problem",
            "Solve 2 problems (1 easy, 1 medium)",
            "Focus on current topic patterns",
            "Practice problems + review solutions",
            "Tackle 1 challenging problem",
            "Review week's progress + theory",
            "Free practice or rest day"
        ]
        
        for day, activity in zip(days, activities):
            print(f"  {day:10}: {activity}")
        
        print(f"\n💡 Pro Tips:")
        print(f"  • Spend 15 min on theory, 45 min on coding")
        print(f"  • Always analyze time/space complexity")
        print(f"  • Review your solution after solving")
        print(f"  • Don't worry if you can't solve it immediately!")
    
    def get_problem_recommendations(self):
        """Get personalized problem recommendations."""
        print("\n" + "="*60)
        print("💡 PROBLEM RECOMMENDATIONS")
        print("="*60)
        
        # Analyze solved problems for pattern preferences
        pattern_count = defaultdict(int)
        difficulty_count = defaultdict(int)
        
        for topic_problems in self.progress["problems_solved"].values():
            for problem_data in topic_problems.values():
                difficulty_count[problem_data["difficulty"]] += 1
        
        print("📈 Your solving pattern:")
        for diff, count in difficulty_count.items():
            print(f"  {diff}: {count} problems")
        
        # Recommend next difficulty level
        easy_solved = difficulty_count.get("Easy", 0)
        medium_solved = difficulty_count.get("Medium", 0)
        
        if easy_solved < 10:
            print(f"\n🎯 Recommendation: Focus on Easy problems (build foundation)")
        elif medium_solved < easy_solved // 2:
            print(f"\n🎯 Recommendation: Start tackling Medium problems")
        else:
            print(f"\n🎯 Recommendation: Great progress! Mix of Medium/Hard problems")
    
    def interactive_menu(self):
        """Main interactive menu."""
        while True:
            print("\n" + "="*60)
            print("🐍 DSA STUDY GUIDE - MAIN MENU")
            print("="*60)
            print("1. 📊 Show Dashboard")
            print("2. 🎯 Today's Focus")
            print("3. 📅 Weekly Plan")
            print("4. 💡 Problem Recommendations")
            print("5. ✅ Mark Problem Solved")
            print("6. 📖 Study Resources")
            print("7. 🚪 Exit")
            
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                self.show_dashboard()
            elif choice == "2":
                self.show_current_focus()
            elif choice == "3":
                self.show_weekly_plan()
            elif choice == "4":
                self.get_problem_recommendations()
            elif choice == "5":
                self.mark_problem_interactive()
            elif choice == "6":
                self.show_resources()
            elif choice == "7":
                print("👋 Happy coding! Remember: consistency beats intensity!")
                break
            else:
                print("❌ Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")
    
    def mark_problem_interactive(self):
        """Interactive problem marking."""
        print("\n📝 Mark Problem as Solved")
        print("-" * 30)
        
        # Show available topics
        print("Available topics:")
        topics = list(self.curriculum.keys())
        for i, (topic_id, topic_data) in enumerate(self.curriculum.items(), 1):
            print(f"  {i}. {topic_data['name']}")
        
        try:
            topic_choice = int(input("\nSelect topic (number): ")) - 1
            if 0 <= topic_choice < len(topics):
                topic_id = topics[topic_choice]
                topic_data = self.curriculum[topic_id]
                
                problem_name = input("Problem name: ").strip()
                difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
                notes = input("Notes (optional): ").strip()
                
                self.mark_problem_solved(topic_id, problem_name, difficulty, notes)
            else:
                print("❌ Invalid topic selection.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    def show_resources(self):
        """Show study resources."""
        print("\n" + "="*60)
        print("📖 STUDY RESOURCES")
        print("="*60)
        
        resources = {
            "📚 Theory & Concepts": [
                "• notes/01_complexity_analysis.md - Time/Space complexity",
                "• Visualize algorithms: visualgo.net",
                "• Interactive tutorials: leetcode.com/explore"
            ],
            "💻 Coding Practice": [
                "• LeetCode.com - Most popular platform",
                "• HackerRank.com - Good for beginners",
                "• GeeksforGeeks.org - Detailed explanations"
            ],
            "📹 Video Resources": [
                "• NeetCode - Excellent explanations",
                "• Abdul Bari - Algorithm theory",
                "• William Fiset - Data structures"
            ],
            "📖 Books": [
                "• Cracking the Coding Interview",
                "• Elements of Programming Interviews",
                "• Introduction to Algorithms (CLRS)"
            ]
        }
        
        for category, items in resources.items():
            print(f"\n{category}:")
            for item in items:
                print(f"  {item}")


def main():
    """Main function to run the study guide."""
    print("🐍 Welcome to your DSA Learning Journey!")
    print("This tool will help you track progress and stay motivated.")
    
    guide = DSAStudyGuide()
    guide.interactive_menu()


if __name__ == "__main__":
    main()


"""
🎯 HOW TO USE THIS STUDY GUIDE:

1. DAILY ROUTINE:
   - Run this script every day
   - Check "Today's Focus" for what to study
   - Mark problems as solved when you complete them
   - Review your progress regularly

2. TRACKING TIPS:
   - Be honest about what you've solved
   - Add notes about difficulties or insights
   - Celebrate small wins!

3. STAYING MOTIVATED:
   - Focus on your study streak
   - Don't compare with others
   - Consistency > intensity
   - It's okay to struggle - that's how you learn!

Remember: The goal is not to rush through problems, 
but to truly understand the patterns and techniques!
"""