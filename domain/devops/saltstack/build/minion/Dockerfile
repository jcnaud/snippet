FROM centos:7

RUN yum update  && \
    yum install https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm  && \
    yum clean expire-cache  && \
    yum install salt-minion -y

# Additional tools
RUN yum install -y python-pip net-tools nmap git

CMD salt-minion
