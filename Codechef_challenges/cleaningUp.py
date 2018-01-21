for _ in range(int(input())):
    chef_jobs = []
    assitent_jobs = []
    n, m = map(int, input().split())
    completed_job = list(map(int, input().split()))
    total_job = list(range(1, n+1))
    for value in completed_job:
        total_job.remove(value)
    for itr in range(len(total_job)):
        if itr % 2 == 0:
            chef_jobs.append(total_job[itr])
        else:
            assitent_jobs.append(total_job[itr])

    for value in chef_jobs:
        print(value, end=' ')
    print()
    for value in assitent_jobs:
        print(value, end=' ')
    print()