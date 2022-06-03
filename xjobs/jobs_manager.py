import subprocess
import os
import pandas as pd
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
        if isinstance(name,str):
            return next((x for x in self.jobs if x.name == name), None)
        elif isinstance(name,int):
            return self.jobs[name]
        elif isinstance(name,slice):
            return self.jobs[name]
        else:
            raise NotImplementedError

    def __len__(self):
        return len(self.jobs)

    def get_running(self):                
        return self.copy([job for job in self 
                          if job.is_running()])
        
    def get_ready(self):
        return self.copy([job for job in self 
                          if job.is_ready()])

    def get_done(self):
        return self.copy([job for job in self 
                          if job.is_done()])

    def get_successful(self):
        return self.copy([job for job in self 
                          if job.is_successful()])

    def get_started(self):
        return self.copy([job for job in self 
                          if job.is_started()])

    def to_pickle(self, filename):
        with open(filename, 'wb') as fid:
            pickle.dump(self, fid)

    def copy(self, jobs = None):
        if jobs == None:
            jobs == self.jobs

        return JobSet(jobs,
            self.platform,
            self.estimate_time,                             
            self.job_flavor,
            self.queue_name,
            self.num_max_cuncurrent_jobs,
            self.add_to_bsub,
            self.add_to_condor_submit_file)

    def to_DataFrame(self):
        my_list = []
        for job in self:
            my_dict ={}
            my_dict['job']=job
            aux = job.get_states()
            my_dict = {**my_dict,**aux}
            my_list.append(my_dict)
        return pd.DataFrame(my_list)

    def kill(self):
        for job in self:
            job.kill()

            

        



    