FROM fedora:26

RUN dnf install -y python-pip && \
    pip install --upgrade python-gitlab 

ADD ./script.py /bin/script.py

ENTRYPOINT ["python", "/bin/script.py"]
