
# Diffusion API 


## Prerequisites

Before you begin, please ensure that you have Docker installed on your system. Docker allows you to package and distribute applications in containers, providing a consistent environment for running the Diffusion API.

If Docker is not installed on your system, follow the official Docker installation guide for your operating system:

- [Docker installation guide](https://docs.docker.com/get-docker/)

## Getting Started

To get started with the Diffusion API, follow the steps below:

### 1. Clone the Repository

Start by cloning the Diffusion API repository from GitHub. Open a terminal or command prompt and execute the following command:

```
git clone https://github.com/rohitkuk/diffusion_API.git
```

Change into the cloned repository directory:

```cd diffusion_API```

Build the Docker image by executing the following command:


```docker build -t bar_docker_api .```

This command builds the Docker image with the tag bar_docker_api

### 2. Running the Docker Image

Replace <host_port> with the port number on your host machine where you want to access the Diffusion API, and <container_port> with the port number specified in your application's configuration (default is usually 8080).

```docker run -p 8000:8080 bar_docker_api```

Once the Docker container is running, you can access the Diffusion API by opening a web browser and navigating to http://localhost:<host_port>.
