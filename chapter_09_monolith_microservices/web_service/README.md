To build the container

    docker build -f docker/Dockerfile --tag example .

To test the container

    docker run -p 8000:8000 example 
