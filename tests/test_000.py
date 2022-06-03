# %%
import xjobs as xj
import os

def test_JobSet():
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
    assert len(my_jobs.jobs)==3
    len(my_jobs.get_running())==0

    my_jobs.launch_jobs()
    assert my_jobs['myjob1'].is_running()