#!/usr/bin/env python


class Manager:
    def __init__(self, worker_count):
        self.workers = [Worker(i) for i in range(worker_count)]

    def get_free_workers(self):
        free_workers = []
        for worker in self.workers:
            if worker.current_job is None:
                free_workers.append(worker)

        return free_workers

    def assign_work(self, workload, time):
        free_workers = self.get_free_workers()
        if len(free_workers) == 0:
            return False

        free_workers[0].assign_job(workload, time)

    def free_workers(self):
        free_workers = self.get_free_workers()

        return len(free_workers) > 0

    def tick(self):
        completed = []
        for worker in self.workers:
            r = worker.tick()
            if r is not None:
                completed.append(r)
        return completed


class Worker:
    def __init__(self, _id):
        self.current_job = None
        self.occupied_time = 0
        self.job_time = 0
        self.id = _id

    def tick(self):
        self.occupied_time += 1

        if self.occupied_time > self.job_time:
            self.occupied_time = 0
            self.job_time = 0
            e = self.current_job
            self.current_job = None

            return e

    def assign_job(self, workload, time):
        self.current_job = workload
        self.job_time = time
