import json
import subprocess
import urllib.error
import urllib.request

from flask import Flask, request, abort, render_template

import db

database = db.DB()
application = Flask(__name__)
try:
    token = subprocess.run(["curl", "--request", "PUT", "http://169.254.169.254/latest/api/token", "--header", "X-aws-ec2-metadata-token-ttl-seconds: 3600"], check=True,
                           stdout=subprocess.PIPE, universal_newlines=True).stdout.strip()
    instance_metadata = subprocess.run(["curl", "-s", "http://169.254.169.254/latest/dynamic/instance-identity/document", "--header", f"X-aws-ec2-metadata-token: {token}"],
                                       check=True, stdout=subprocess.PIPE, universal_newlines=True).stdout

    if instance_metadata:
        metadata = json.loads(instance_metadata)
        region = metadata["region"]
        availability_zone = metadata["availabilityZone"]
        application.config["REGION"] = availability_zone
    else:
        region = "us-east-1"
        application.config["REGION"] = "unknown region"

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    instance_id = None
    region = None
    instance_name = None


@application.route("/")
def home():
    #country = database.query("SELECT LocID, Location, Variant, Time, PopMale, PopFemale, PopTotal, PopDensity from population;")
    country_list = database.query("SELECT DISTINCT Location from population;")
    year_data = database.query("SELECT DISTINCT Time from population;")

    #print(country)
    return render_template('main.html', countries=country_list, years=year_data)

@application.route("/facts" , methods=['GET', 'POST'])
def facts():
    country_name = request.form.get('country')
    #print(country_name)
    year_select = request.form.get('year')
    #print(year_select)
    country = database.query(f"SELECT LocID, Location, Variant, Time, PopMale, PopFemale, PopTotal, PopDensity from population where Location = '{country_name}' and Time = {year_select};")
    #print(country)
    return render_template('fact.html', country=country)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0', port=8443)
