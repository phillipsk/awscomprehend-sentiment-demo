FROM python:3.6-alpine

ENV source_path /opt/program/awscomprehend-sentiment-demo
RUN mkdir -p ${source_path}



#Set up source
COPY ./  ${source_path}
RUN pip install -r ${source_path}/requirements.txt -t ${source_path}
RUN pip install  awscli --upgrade

#Set up working directory
WORKDIR ${source_path}
ENTRYPOINT  ["python", "${source_path}/demo.py"]

#Default arguments to run test
CMD ["single", "This is great! and amazing"]
