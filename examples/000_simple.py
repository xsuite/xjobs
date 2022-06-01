# %%
import xjobs as xj
import os

my_jobs = xj.JobSet(
    jobs = [
        xj.Job(name='myjob1', command='./000_folder/run.sh Isaac Newton', 
               ready_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/run.sh'}],
               success_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/000.out'}],
               started_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/000.start'}],
               completed_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/000.end'}],
               ),
        xj.Job(name='myjob2', command='./000_folder/run.sh Albert Einstein 001', 
               ready_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/run.sh'}],
               success_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/001.out'}],
               started_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/001.start'}],
               completed_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/001.end'}],
               ),
        xj.Job(name='myjob3', command='./000_folder/run.sh Enrico Fermi 002',
               ready_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/run.sh'}],
               success_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/002.out'}],
               started_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/002.start'}],
               completed_condition=[os.path.isfile,
                                 {'path'  :'./000_folder/002.end'}],
               )
    ],
    platform = 'local',
    num_max_cuncurrent_jobs=1
)

my_jobs.to_pickle('jobs.pickle')

# %%
my_jobs = xj.read_pickle('jobs.pickle')

# %%
len(my_jobs.get_running_jobs())

# %%
my_jobs.launch_jobs()  
# %%
