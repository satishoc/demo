from dkube.sdk.dkube import *

env = Environment(scheme='https', host='18.236.126.102', user='ocdkube', token=sys.argv[1], port=32222)
launch_training_job("test", autogenerate=True, environ=env.external, workspace='mn-ws', script='python model.py',datasets=['mn-data'])
