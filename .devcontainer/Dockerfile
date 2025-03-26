# Start from Microsoft's Ubuntu-based devcontainer image
FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Define build arguments for customization
ARG ANO_CLAB_VERSION
ARG ANO_PRIV_KEY_NAME
ARG ANO_NETBOX_URL
ARG ANO_NETBOX_TOKEN

# Set environment variables from the build arguments
ENV ANO_CLAB_VERSION=${ANO_CLAB_VERSION}
ENV ANO_PRIV_KEY_NAME=${ANO_PRIV_KEY_NAME}
ENV ANO_NETBOX_URL=${ANO_NETBOX_URL}
ENV ANO_NETBOX_TOKEN=${ANO_NETBOX_TOKEN}

# Install basic tools as root
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        make \
        sshpass \
        iputils-ping \
        htop \
        python3 \
        python3-pip \
        sudo \
        telnet \
        openssh-client \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/doc /usr/share/man \
    && apt-get clean

# Install Python packages
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Copy the postCreate.py script
COPY ./postCreate.py /bin/postCreate.py
RUN chmod +x /bin/postCreate.py

# Allow the 'vscode' user to run sudo without a password
RUN echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode


# Install Containerlab and Python tools
RUN bash -c "$(curl -sL https://get.containerlab.dev)" -- -v "${ANO_CLAB_VERSION}" 

# Generate an SSH key pair for the 'vscode' user
RUN ssh-keygen -t rsa -b 2048 -f ~/.ssh/${ANO_PRIV_KEY_NAME} -N ""