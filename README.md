
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

1. Start the Docker container by executing the command below:

```docker run -p <host_port>:<container_port> bar_docker_api```

Replace <host_port> with the port number on your host machine where you want to access the Diffusion API, and <container_port> with the port number specified in your application's configuration (default is usually 8080).

```docker run -p 8000:8080 bar_docker_api```

2. Once the Docker container is running, you can access the Diffusion API by opening a web browser and navigating to http://localhost:<host_port>.


## Testing 

```
import requests
import json
import numpy as np

url = "http://127.0.0.1:80"

text_prompt = """
    I have a silky smooth voice, and today I will tell you about 
    the exercise regimen of the common sloth.
"""
payload = {"text_prompt": text_prompt}

response = requests.post(url, json=payload)

decodedArrays = json.loads(response.json())

finalNumpyArray = np.asarray(decodedArrays["array"])
from IPython.display import Audio
Audio(finalNumpyArray, rate=SAMPLE_RATE)

```

[sloth.webm](https://user-images.githubusercontent.com/5068315/230684883-a344c619-a560-4ff5-8b99-b4463a34487b.webm)
