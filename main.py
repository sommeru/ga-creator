import yaml
import math

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(config)

mgAddr = 0
ugAddr = 0
for mg in config['GA_config']['MG']:
    print(str(mgAddr) + ' - ' + mg)
    for item in config['items']:
        if item.startswith(mg):
            for entity in config['block']['entities']:
                print(str(config['GA_config']['HG']) + '/' + str(mgAddr) + '/' + str(ugAddr) + ' - ' + item + ' ' + entity)
                ugAddr += 1
            # After one block is done continue with next block number    
            ugAddr = math.ceil(ugAddr / config['block']['blocksize']) * config['block']['blocksize']
    mgAddr += 1
    ugAddr = 0