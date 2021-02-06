1. [] Install docker
2. [] Pull an image from dockerhub
>>>docker pull centos
Another linux distribution is by exemple alpine
>>>docker pull alpine

3. [] run downloaded image
>>>docker run -d -t --name firsttry centos
4. [] To check our running docker containers
>>>docker ps
5. [] To conect to our container
>>>docker exec -it firsttry bash
or to connect to the shell
>>>docker exec -it second sh
6. [] To pull image from hub.docker.com
>>>docker pull thenetworkchuck/nccoffee:frenchpress
7. [] To stop a docker conatainer 
>>>docker stop second
8. [] To see how much cpm, memory, network container are useing
>>>docker stats
