# How to run this package?
*hint:all words like ~~this~~,change it to your costomization.*

1. install docker on ubuntu <code>sudo apt install docker.io</code>
2. <code>sudo docker pull python:3.8.10 </code>     #base on 3.8.10
3. cd into "mnist_api"
4. <code>sudo docker build -t ~~image name:tag~~ .</code>     #build image via Dockerfile,which is under the local folder.
        # Don't miss the dot "." in the end of command,which means to use the Dockerfile in the local directory.


5. <code>sudo docker image ls</code>     #check the image you build
6. <code>sudo docker run -itd -p ~~port~~:3000 --name ~~container name~~ ~~image name:tag~~</code> #create a container to run the image,connect your port to container's 3000 port
7. <code>sudo docker ps </code> #check your container's process

## Check some docker's command:
https://ithelp.ithome.com.tw/articles/10262165?sc=rss.iron

