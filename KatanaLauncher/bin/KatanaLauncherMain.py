from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys, os, json

DEFAULT_PATHS = {'katana_path' : '/home/foundry/foundry',
         'arnold_path' : '/home/foundry/ktoa',
         'prman_path' : '/opt/pixar',
         'redshift_path' : '/usr/redshift/redshift4katana'
        }

SCRIPT_PATH = '../scripts'

#check if json file exists, create it if not
if os.path.exists('../config.json'):
    with open('../config.json', 'r') as infile:
        paths = json.load(infile)
    for path in paths:
        if os.path.isdir(paths[path]) == False:
            paths[path] = '/home'
            print('resetting %s not found, resetting to /home...' % path)
        
    with open('../config.json', "w") as outfile:
        json.dump(paths, outfile)
else:
    with open('../config.json', "w") as outfile:
        json.dump(DEFAULT_PATHS, outfile)
        paths = DEFAULT_PATHS

def getKatanaVersions():
    print(paths['katana_path'])
    katana_versions = []
    for f in os.listdir(paths['katana_path']):
        if os.path.isfile(paths['katana_path'] + "/" + f + "/katana"):
            katana_versions.append(f[6:])
    return katana_versions

def getArnoldVersions():
    
    arnold_versions = []
    for f in os.listdir(paths['arnold_path']):
        if 'ktoa' in f and os.path.isdir(paths['arnold_path'] + '/' + f):
            arnold_versions.append(f.split('-')[1])
    return arnold_versions

def getPrmanVersions():
    
    prman_versions = []
    for f in os.listdir(paths['prman_path']):
        if 'RenderManForKatana' in f and os.path.isdir(paths['prman_path'] + '/' + f):
            prman_versions.append(f.split('-')[1])
    return prman_versions

def getRedshiftVersions():
    
    redshift_versions = []
    try: 
        for f in os.listdir(paths['redshift_path']):
            if 'redshfit' in f:
                redshift_versions.append(f[6:])
    except: return []
    return redshift_versions

def getBatchScripts():
    
    scripts = []
    for f in os.listdir(SCRIPT_PATH):
        if f.endswith('.sh'):
            scripts.append(f)
    return scripts

def getRenderers():
    
    render_scripts = []
    for f in os.listdir(SCRIPT_PATH + '/Renderers'):
        if f.endswith('.sh'):
            render_scripts.append(f[0:-3])
    return render_scripts
