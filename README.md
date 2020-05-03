# Docker_project_rise
This is a Web application deployed on Apache HTTP web server which is working on Centos:7 Docker container. This web app uses machine learning to perform face recognition which is a maens to perform authentication of the user. For performing the authentication a ML model is used which is trained on the faces of the user. the web app is being hosted on Apache Http webserver which works on Centos:7 Docker container.
The entire working of project include:
1) Run the docker compose file.
2) Train ML model with the faces of user. This part is done by modelcreation.py file which runs on host system. The model generated from this file has to be deployed on container created using compose file. The model has to be kept in '/var/www/cgi' folder of container.
3) As the 80 port of the docker has been exposed and linked to 123 port number of host system so while running the web use the url as: 'http://ip_of_base_system:123'.
