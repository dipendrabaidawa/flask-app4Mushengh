# Python modules

from flask import Flask
from flask.globals import request
import config
import os
import decimal
from urllib.request import urlopen 

# Flask modules
from flask import render_template, json

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# create a flask app
app = Flask(__name__)

app.config.update(
    DEBUG=config.DEBUG,
    SECRET_KEY=config.SECRET_KEY)

# Option config
option_names = ("Fn", "Cm", "Nd", "Srp", "IT", "DRS", "Pd", "SRQ")
option_values = (
    ("fn_1", "fn_2", "fn_3", "fn_4", "fn_5", "fn_6", "fn_7", "fn_8", "fn_9", "fn_10", "fn_11", "fn_12", "fn_13", "fn_14", "fn_15", "fn_16"),
    ("cm_1", "cm_2", "cm_3", "cm_4", "cm_5", "cm_6", "cm_7", "cm_8", "cm_9", "cm_10", "cm_11", "cm_12", "cm_13", "cm_14", "cm_15", "cm_16", "cm_17", "cm_18", "cm_19", "cm_20", "cm_21", "cm_22", "cm_23", "cm_24", "cm_25", "cm_26", "cm_27", "cm_28"),
    ("nd_1", "nd_2", "nd_3", "nd_4", "nd_5", "nd_6", "nd_7", "nd_8", "nd_9", "nd_10", "nd_11", "nd_12", "nd_13", "nd_14", "nd_15", "nd_16", "nd_17", "nd_18", "nd_19", "nd_20", "nd_21", "nd_22", "nd_23", "nd_24", "nd_25", "nd_26", "nd_27", "nd_28", "nd_29", "nd_30", "nd_31", "nd_32"),
    ("srp_1", "srp_2", "srp_3", "srp_4"),
    ("it_1", "it_2", "it_3"),
    ("drs_1", "drs_2", "drs_3", "drs_4", "drs_5"),
    ("pd_1", "pd_2", "pd_3", "pd_4", "pd_5", "pd_6", "pd_7", "pd_8", "pd_9", "pd_10", "pd_11", "pd_12", "pd_13", "pd_14", "pd_15", "pd_16", "pd_17", "pd_18", "pd_19", "pd_20", "pd_21", "pd_22", "pd_23", "pd_24", "pd_25", "pd_26", "pd_27", "pd_28"),
    ("srq_1", "srq_2", "srq_3", "srq_4", "srq_5", "srq_6", "srq_7", "srq_8", "srq_9", "srq_10", "srq_11", "srq_12")
)

# display index page
@app.route('/')
def index():
    return render_template("index.html", option_names=option_names, option_values=option_values)

# run the query engine
@app.route('/query', methods=['POST'])
def query():
    # get option values from request
    opts = request.form
    
    # run the query engine
    """
        print(opts) 
        # outputs: ImmutableMultiDict([('Cm', 'fn_1'), ('Nd', 'cm_1'), ('Srp', 'nd_1'), ('IT', 'srp_1'), ('DRS', 'it_1'), ('Pd', 'drs_1'), ('SRQ', 'pd_1')])
        
        Please make the filter_dict with opts variable.
        You can get each option value from there.
        ex: 'Fn' : opts['Fn'], 'Cm' : opts['Cm']
        
        filter_dict = {

        'Fn': str(input("Enter a value for Fn: ")),

        'std': str(input("Enter a value for std: ")),

        ......

        }

        filter_sr ={
        'Quarter': str(input("Enter a value for Quarter: "))
        }

        sr = filter_sr['Quarter'].replace(' to ', '<= Quarter <=')
        query = ' & '.join([f'{k} == "{v}"' for k,v in filter_dict.items() if v!=""])

        df.query(query)
    """
    df = (1, 2, 3, 4, 5, 6, 7, 8)
    
    return render_template("index.html", option_names=option_names, option_values=option_values, df=df)
