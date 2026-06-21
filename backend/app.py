""" 
app.py
Build a few jobs, registers them, run them, print a summary.
"""

from models import EmailJob, DataProcessingJob, PriorityJob
from task_manager import TaskManager
from executor import Executor

def build_jobs():
    return [
        EmailJob(1, "user@example.com"),
        DataProcessingJob(2, "dataset_A"),
        PriorityJob(5, "Send critical alert", "High"),
        EmailJob(3, "admin@example.com"),
        DataProcessingJob(4, "dataset_B"),
        PriorityJob(6, "Run nightly report", "Low"),
    ]

if __name__ == "__main__":
    jobs = build_jobs()

    manager = TaskManager()
    for job in jobs:
        manager.add_job(job) # all start as 'pending'

    Executor(jobs).run()

    print("\n=== SUMMARY ===")
    print(f"Pending:    {len(manager.get_jobs_by_status('pending'))}")
    print(f"Completed:  {len(manager.get_jobs_by_status('completed'))}")