import os
from flask import Flask, request, render_template, send_from_directory
import boto3
import io
import pandas as pd
import itertools

# Set below parameters
endpointName = 'document-classifier'

# Talk to SageMaker
client = boto3.client('sagemaker-runtime',region_name='us-west-2')




application = Flask(__name__)

@application.route("/")
def index():
    return render_template("index.html")


@application.route("/upload", methods=["POST","GET"])
def upload():
    print("Inside upload method")
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            #print(file.read())
            # Talk to SageMaker
            print("Calling boto3 sdk")
            client = boto3.client('sagemaker-runtime', region_name='us-west-2')
            response = client.invoke_endpoint(
                EndpointName=endpointName,
                Body=file.read(),
                ContentType='text/csv',
                Accept='Accept'
            )

            output = response['Body'].read().decode('ascii')
            output = output.split("\n")[:-1]
            print(output)
            return render_template("upload.html", result = output )
    else:
        return render_template("index.html")

if __name__ == "__main__":
    application.run(port=4555, debug=True)
