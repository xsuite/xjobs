import subprocess
import os
#import psutil
import pickle
import datetime

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
                if len(self.get_running()) < self.num_max_cuncurrent_jobs:
                    if not job.is_started():
                        job.id.process = subprocess.Popen(job.command, 
                                                shell = True,
                                                preexec_fn=os.setsid)
                        job.id.pid = job.id.process.pid
                        job.id.start_time = datetime.datetime.now()
                else:
                    break
            return

        if self.platform == 'LSF':
            raise NotImplementedError

        if self.platform == 'HTCondor':
            raise NotImplementedError
        else:
            raise NotImplementedError

    def __getitem__(self, name):
        return next((x for x in self.jobs if x.name == name), None)

    def get_running(self):
        jobs_list = []
        for job in self.jobs:
            if job.is_running():
                jobs_list.append(job)
        return jobs_list

    def get_ready(self):
        jobs_list = []
        for job in self.jobs:
            if (job.is_ready()):
                jobs_list.append(job)
        return jobs_list

    def get_done(self):
        jobs_list = []
        for job in self.jobs:
            if (job.is_done()):
                jobs_list.append(job)
        return jobs_list

    def get_successful(self):
        jobs_list = []
        for job in self.jobs:
            if (job.is_successful()):
                jobs_list.append(job)
        return jobs_list

    def get_started(self):
        jobs_list = []
        for job in self.jobs:
            if (job.is_started()):
                jobs_list.append(job)
        return jobs_list

    def to_pickle(self, filename):
        with open(filename, 'wb') as fid:
            pickle.dump(self, fid)

        



    