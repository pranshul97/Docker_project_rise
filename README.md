## Docker_project_rise
This is a Web application deployed on Apache HTTP web server which is working on Centos:7 Docker container. This web app uses machine learning to perform face recognition which is a maens to perform authentication of the user. For performing the authentication a ML model is used which is trained on the faces of the user. the web app is being hosted on Apache Http webserver which works on Centos:7 Docker container.
# Pre-requisites:
1) Docker-CE
2) Python3 & Open-CV on base OS
3) Centos:7 docker image
# The entire working of project include:
1) Create docker container by following command docker run -it --name docker_project -p 91:80 centOS.
2) Configure HTTP web server on docker by using yum install httpd command.
3) Run httpd server using /usr/bin/httpd command.
4) Run the modelcreation.py file on host system which will create the model and ploce model in '/var/www/cgi-bin' repo. 
5) Place the other files also in the same repo '/var/www/cgi-bin'.
6) Install opencv and opencv-contrib-python libraries in docker using pip install openCV opencv-contrib-python.
7) As the 80 port of the docker has been exposed and linked to 91 port number of host system so while running the web app use the url as: 'http://ip_of_base_system:123'.
