from nornir import init_nornir
from nornir.plugins.functions.text import print result
from nornir.plugins.tasks.networking import napalm_get

nr = InitNornir(
#   config_file ="01.config.yaml", dry_run=True
)

results = nr.run(  
    task=napalm_get, getattr=[ "facts", "interfaces", "environment", "interfaces_ip"]
)

print(results)
