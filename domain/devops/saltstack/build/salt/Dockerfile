ARG ALPINE_VERSION

FROM python:3.6-alpine${ALPINE_VERSION}

ARG SALT_VERSION

RUN apk add --no-cache gcc g++ autoconf make libffi-dev openssl-dev dumb-init

RUN addgroup -g 450 -S salt && adduser -s /bin/sh -SD -G salt salt && \
    mkdir -p /etc/pki /etc/salt/pki /etc/salt/minion.d/ /etc/salt/master.d /etc/salt/proxy.d /var/cache/salt /var/log/salt /var/run/salt && \
    chmod -R 2775 /etc/pki /etc/salt /var/cache/salt /var/log/salt /var/run/salt && \
    chgrp -R salt /etc/pki /etc/salt /var/cache/salt /var/log/salt /var/run/salt

ENTRYPOINT ["/usr/bin/dumb-init"]
CMD ["/usr/local/bin/saltinit"]
ADD saltinit.py /usr/local/bin/saltinit
RUN chmod ugo+xr /usr/local/bin/saltinit
EXPOSE 4505 4506 8000
VOLUME /etc/salt/pki/

RUN USE_STATIC_REQUIREMENTS=1 pip3 install --no-cache-dir salt=="${SALT_VERSION}"
RUN su - salt -c 'salt-run salt.cmd tls.create_self_signed_cert'
