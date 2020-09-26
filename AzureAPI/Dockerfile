FROM ubuntu:latest

#this runs continuously an prevents container from going to sleep
CMD tail -f /dev/null

#gets all updates for Ubuntu and installs Python Pip and Python Dev so you can run Python in this Ubuntu Image
RUN apt-get update -y && apt-get install -y python3-pip python-dev

#expose these ports
EXPOSE 80
EXPOSE 5000

#copy this file
COPY ./requirements.txt /AzureAPI/requirements.txt

WORKDIR /AzureAPI

#install these things in the Ubuntu image, requirements.txt: flask, azure-mgmt-compute, flake8
RUN pip3 install -r requirements.txt 

#copy entire application to this folder
COPY . /AzureAPI

#essentially execute: python3.exe app.py
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

