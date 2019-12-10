from dkube.sdk.dkube import *

env = Environment(scheme='https', host='192.168.200.23', user='ocdkube', token=sys.argv[1], port=32222)
simeple demo("test", autogenerate=True, environ=env.external, workspace='mn-ws', script='python model.py',datasets=['mn-data'])
