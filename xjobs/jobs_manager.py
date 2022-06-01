import subprocess
import os
import psutil
import pickle

def read_pickle(filename):
    with open(filename,'rb') as fid:
        return pickle.load(fid)

class JobSet():

    def __init__(self, jobs, platform,
                    estimated_time = 4000, # only HTCondor
                    job_flavor = 'vanilla', # only HTCondor
                    queue_name = 'hpc_acc', # only LSF
                    num_max_cuncurrent_jobs = 100, # mostly for local 
                    # Optional low-level commands
                    add_to_bsub = '', # works only on LSF
                    add_to_condor_submit_file = ''):
        self.jobs = jobs
        self.platform = platform
        self.estimate_time = estimated_time                                    
        self.job_flavor = job_flavor
        self.queue_name = queue_name
        self.num_max_cuncurrent_jobs = num_max_cuncurrent_jobs
        self.add_to_bsub = add_to_bsub
        self.add_to_condor_submit_file = add_to_condor_submit_file

    def launch_jobs(self):
        if self.platform == 'local':
            for job in self.jobs:
                if len(self.get_running_jobs()) < self.num_max_cuncurrent_jobs:
                    if not job.is_started():
                        job.id = subprocess.Popen(job.command, 
                                                shell = True,
                                                preexec_fn=os.setsid).pid
                else:
                    break
            return

        if self.platform == 'LSF':
            print('Not implemented')

        if self.platform == 'HTCondor':
            print('Not implemented')
        else:
            print('Not implemented') 

    def __getitem__(self, name):
        return next((x for x in self.jobs if x.name == name), None)

    def get_running_jobs(self):
        jobs_list = []
        for job in self.jobs:
            if ((not job.id == None) and 
                (psutil.pid_exists(job.id)) and
                (not psutil.Process(job.id).status()=='zombie')):
                jobs_list.append(job)
        return jobs_list

    def get_ready_jobs(self):
        jobs_list = []
        for job in self.jobs:
            if (job.is_ready()):
                jobs_list.append(job)
        return jobs_list

    def get_completed_jobs(self):
        jobs_list = []
        for job in self.jobs:
            if (job.is_completed()):
                jobs_list.append(job)
        return jobs_list

    def get_successful_jobs(self):
        jobs_list = []
        for job in self.jobs:
            if (job.is_successful()):
                jobs_list.append(job)
        return jobs_list

    def get_started_jobs(self):
        jobs_list = []
        for job in self.jobs:
            if (job.is_started()):
                jobs_list.append(job)
        return jobs_list

    def to_pickle(self, filename):
        with open(filename, 'wb') as fid:
            pickle.dump(self, fid)

        



    