#! python
#coding: utf-8

from beerapp import *
import sys
import yaml
import os

def run():
    app.run(debug=True)

def run_external():
    app.run(debug=True, host='0.0.0.0')

def create_db():
    db.create_all()

def fetch_posts():
    members.update_all_entries()

def teste():
    print app.config['TESTE']

def show_config():
    #print app.config["SQLALCHEMY_DATABASE_URI"]
    for k, v in app.config.items():
        print k + ' :'
        print v
        
    
                
if __name__ == '__main__':
    'Calls the method with the given name with the other args (if any)'

    func_name = sys.argv[1]
    task = globals()[func_name]

    try:
        task(sys.argv[2:])
    except:
        task()
        
        
