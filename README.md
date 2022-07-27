
# REFIT-Kubernetes

Kubernetes is a tool to orchestrate the containers. In this project, I have created two applications: One is send requests and the other is receive requests. 
The code is written in Python language with Flask web server and rest end points are created in both sender and receiver applications to communicate.

In these applications, the configurations are read from the properties file which are created by configmaps of Kubernetes. 

I have created a service to setup the communication between the pods and all the API calls are done by the service hostname and application port. 

I have also write a code to create docker images(refer dockerfile), kubernetes deployments (refer deployments yaml file), services (refer service yaml files), and configmaps. 



## Pre-requisites
Install Minikube to run the application in your local

## Installation

1. Create a new directory
```bash  
  mkdir refit
  cd refit
```
2. Clone the repository into the above directory
```bash
git clone git@github.com:prakhar-iit/refit-kubernetes.git
```
3. Go inside refit-kubernetes project and refit-receiver directory
```bash
cd refit-kubernetes
```
4. Create a docker image for with a tag 
```bash
docker build -t <username>/refit-receiver:<build_number> .
```
<username> is your docker hub or private docker repository. 
For example: I am using the below docker command:
```bash
docker build -t 705922/refit-receiver:3 .
```
5. Push the docker image to the docker repository
```bash
docker push 705922/refit-receiver:3
```
6. Create Config Map in your machine
```bash 
kubectl create configmap refit-receiver-config --from-file=refit.properties
```
7. Create a Service
```bash
kubectl apply -f refit-receiver-svc.yaml
```
8. Create a deployment
```bash
kubectl apply -f refit-receiver-deployment.yaml
```
9. Repeat the above process for the sender. Go inside refit-sender directory
```bash
cd ../refit-sender
```
10. Create a docker image for with a tag 
```bash
docker build -t <username>/refit-sender:<build_number> .
```
<username> is your docker hub or private docker repository. 
For example: I am using the below docker command:
```bash
docker build -t 705922/refit-sender:3 .
```
11. Push the docker image to the docker repository
```bash
docker push 705922/refit-sender:3
```
12. Create Config Map in your machine
```bash 
kubectl create configmap refit-sender-config --from-file=refit.properties
```
13. Create a Service
```bash
kubectl apply -f refit-sender-svc.yaml
```
14. Create a deployment
```bash
kubectl apply -f refit-sender-deployment.yaml
```

## Command to Update the new image of application
```bash
kubectl set image deployments/refit-receiver-deployment refit-receiver=705922/refit-receiver:3
```

## Other Important Commands of kubernetes
```bash
kubectl apply -f cdl-refit-deployment.yaml
```
```bash
docker build -t cdl-refit-python .
docker push 705922/cdl-refit-python
docker run -p 8080:8080 cdl-refit-python
```
```bash
kubectl scale deployment/cdl-refit-deployment-python --replicas=2
kubectl get deployments
kubectl get pods
kubectl get services
kubectl logs cdl-refit-deployment-python-7fdf469758-wqcsp
kubectl exec -ti refit-sender-deployment-64bb555dd6-dvlk7 -- bash
kubectl get pods -o wide    
kubectl describe svc refit-nw-svc
kubectl get ep refit-nw-svc
kubectl exec cdl-refit-deployment-python-7fdf469758-d9z9v -- printenv | grep SERVICE
apt-get update
apt-get install curl
kubectl create configmap refit-config-map --from-file=refit.properties
kubectl describe configmaps refit-config-map
kubectl apply -k .

curl refit-nw-svc.default.svc.cluster.local:8080/chat
curl --header "Content-Type: application/json" -X POST --data '{"payload": "Hi"}' refit-receiver-svc.default.svc.cluster.local:8080/receiver
curl --header "Content-Type: application/json" refit-sender-svc.default.svc.cluster.local:8080/sender

kubectl create configmap refit-config --from-file=refit.properties
kubectl create configmap refit-config --from-env-file=refit.properties
kubectl delete configmap refit-config
kubectl apply -f cdl-refit-svc.yaml
kubectl get pods -l app=refit-receiver -o wide 
docker build -t cdl-refit-python .
```

## Process to make changes in Application File
1. Change config file path in sender file
2. Save changes in app.py file (sender and receiver files)
2. Make changes in Docker file
3. Create a docker image
4. docker push 705922/cdl-refit-python:1
5. Push docker image to docker hub
6. Create Config
7. Create Service
8. Create deployments