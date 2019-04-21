## Docker Container Notes

1. Remove old docker images with `docker system prune` as root/sudo [^source]
2. Check which docker instances are running with `docker ps` [^docker-commands]
3. Building this docker image: https://github.com/idealo/image-quality-assessment : `docker build -t nima-cpu . -f Dockerfile.cpu` [^image-docker-project]


[^source]: [docker information from Linuxize](https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/)

[^docker-commands]: [docker commands](https://docs.docker.com/engine/reference/commandline/ps/)

[^image-docker-project]: [image machine learning project](https://github.com/idealo/image-quality-assessment/blob/master/README.md#getting-started)