# %%
import xjobs as xj
import os

# %% an empty JobSet
my_jobs = xj.JobSet(
    jobs = [],
    platform = 'local',
    num_max_cuncurrent_jobs=1
)
my_jobs.launch_jobs()

# %% a simple JobSet
my_jobs = xj.JobSet(
    jobs = [
        xj.Job(name='myjob1', command='./000_folder/run.sh Isaac Newton', 
               ready_condition=xj.ConditionFileExists(
                      './000_folder/run.sh'),
               success_condition=xj.ConditionFileContains(
                      './000_folder/000.out',
                      'ton'),
                ),
        xj.Job(name='myjob2', command='./000_folder/run.sh Albert Einstein 001', 
               ready_condition=xj.ConditionFileExists(
                      './000_folder/run.sh'),
               success_condition=xj.ConditionFileContains(
                      './000_folder/001.out',
                      'Alb'),
                ),
        xj.Job(name='myjob3', command='./000_folder/run.sh Enrico Fermi 002',
               ready_condition=xj.ConditionFileExists(
                      './000_folder/run.sh'),
               success_condition=xj.ConditionFileContains(
                      './000_folder/002.out',
                      'ico'),
                )
    ],
    platform = 'local',
    num_max_cuncurrent_jobs=1
)

my_jobs.to_pickle('jobs.pickle')

# %%
my_jobs = xj.read_pickle('jobs.pickle')

# %%
my_jobs.launch_jobs()
len(my_jobs.get_running())

# %%
my_jobs.launch_jobs()
my_jobs.kill()
for job in my_jobs.jobs:
       print(job.is_running())


# %%
my_jobs[0].get_states()

# %%

my_jobs.to_DataFrame()
# %%
my_jobs[3::-1]
# %%
print(my_jobs['myjob2'])


# %%
