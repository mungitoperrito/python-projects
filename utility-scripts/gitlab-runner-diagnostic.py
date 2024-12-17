import gitlab

# Connect to grammatech gitlab instance. Assumes there's a config file
#   as described https://python-gitlab.readthedocs.io/en/stable/cli.html
# 
# API is documented here:
#    https://python-gitlab.readthedocs.io/en/stable/api-objects.html
# 
# Connection with no context manager
#    gl = gitlab.Gitlab.from_config('grammatech')
with gitlab.Gitlab.from_config('grammatech') as gl:


# Note: parameter format for non-pythonic arguments
# gl.user_activities.list(query_parameters={'from': '2019-01-01'})  # Good
# gl.user_activities.list(from='2019-01-01')                        # Bad


# List all the runners
    # runners = gl.runners.list(all=True)      # Returns paginated list by default
    # runners = gl.runners.list(per_page=2)    # Returns paginated list by default
    runners = gl.runners.list(as_list=False)  # Returns a generator object

    #    active_jobs = gl.runners.list(status='running')
    for runner in runners:
        jobs = runner.jobs.list()
        if len(jobs) > 0:
            # print (jobs[-1].commit)
            curr_job = jobs.pop()
            print(curr_job.id)
            attrs = vars(curr_job)
            print('\n'.join("%s: %s" % item for item in attrs.items()))
            # exit()
            active_jobs = runner.jobs.list(status='running')
            print(active_jobs)
            print("")
