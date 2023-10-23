import yaml
import math
import sys

sep = '\t'

if len(sys.argv) != 2:
    print ('usage: ga-creator.py [file].yaml')
    print ('  ...trying config.yaml')
    filename = 'config'
else:
    filename=str(sys.argv[1])
    if '.' in filename:
        filename = filename.split('.')[0]

with open(filename + '.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(config)

def formatGA(mgAddr, ugAddr):
    ga = str(config['GA_config']['HG']) + '/' + str(mgAddr) + '/' + str(ugAddr)
    return(ga)

def formatCSV(ga, mg, ug):    
        if mg == '-' and ug == '-':
            print('Main', 'Middle', 'Sub', 'Address', 'Central', 'Unfiltered', 'Description', 'DatapointType', 'Security', sep=';')
            print(config['GA_config']['HG_Name'], '', '', ga, '', '', '', '', 'Auto', sep=';')
            with open(filename + '.csv', 'w', encoding='cp1252') as f:
                f.write('Main' + sep + 'Middle' + sep + 'Sub' + sep + 'Address' + sep + 'Central' + sep + 'Unfiltered' + sep + 'Description' + sep + 'DatapointType' + sep + 'Security\n')
                f.write(config['GA_config']['HG_Name'] + sep + sep + sep + ga + sep + sep + sep + sep + sep + 'Auto\n')
        if mg != '-' and ug == '-':            
            print('', mg, '', ga, '', '', '', '', 'Auto', sep=';')
            with open(filename + '.csv', 'a', encoding='cp1252') as f:
                f.write(sep + mg + sep + sep + ga + sep + sep + sep + sep + sep + 'Auto\n')
        if mg != '-' and ug != '-':
            print('', '', ug, ga, '', '', '', '', 'Auto', sep=';')
            with open(filename + '.csv', 'a', encoding='cp1252') as f:
                f.write(sep + sep + ug + sep + ga + sep + sep + sep + sep + sep + 'Auto\n')

mgAddr = 0
ugAddr = 0
ga = formatGA('-', '-')
formatCSV(ga, '-', '-')

for mg in config['GA_config']['MG_Name']:    
    ga = formatGA(mgAddr, '-')
    formatCSV(ga, mg, '-')

    for item in config['items']:
        if item.startswith(mg):
            for entity in config['block']['entities']:
                #print(str(config['GA_config']['HG']) + '/' + str(mgAddr) + '/' + str(ugAddr) + ' - ' + item + ' ' + entity)                
                #print(formatGA(mgAddr, ugAddr))
                ug =  item + ' ' + entity
                ga = formatGA(mgAddr, ugAddr)                
                formatCSV(ga, mg, ug)
                ugAddr += 1
            # After one block is done continue with next block number    
            ugAddr = math.ceil(ugAddr / config['block']['blocksize']) * config['block']['blocksize']
    mgAddr += 1
    ugAddr = 0