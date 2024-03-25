# Stage 1: Build Python environment
FROM python:3.10 as python-builder

# Install dependencies
RUN pip install cryptography

# Stage 2: Use nginx image as base
FROM nginx:alpine

COPY --from=python-builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/

EXPOSE 80

# Copy the configuration file
COPY nginx.cfg /etc/nginx/

RUN apk update && \
    apk add bash git openssh rsync augeas shadow && \
    deluser $(getent passwd 33 | cut -d: -f1) && \
    delgroup $(getent group 33 | cut -d: -f1) 2>/dev/null || true && \
    mkdir -p ~root/.ssh /etc/authorized_keys && chmod 700 ~root/.ssh/ && \
    augtool 'set /files/etc/ssh/sshd_config/AuthorizedKeysFile ".ssh/authorized_keys /etc/authorized_keys/%u"' && \
    echo -e "Port 2225\n" >> /etc/ssh/sshd_config && \
    cp -a /etc/ssh /etc/ssh.cache && \
    rm -rf /var/cache/apk/*