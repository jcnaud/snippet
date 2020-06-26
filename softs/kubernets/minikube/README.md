# Kubernet

<!-- TOC -->

- [Kubernet](#kubernet)
  - [Links](#links)
  - [Overview](#overview)
    - [Install Kubectl](#install-kubectl)
    - [Install MiniKube](#install-minikube)
    - [Add On](#add-on)
  - [Run minikube](#run-minikube)
    - [Minikube command](#minikube-command)
    - [Kubectl command](#kubectl-command)
  - [Deploy exemple](#deploy-exemple)

<!-- /TOC -->

## Links

install minikube: https://minikube.sigs.k8s.io/docs/start/linux/
Installer Kubernetes avec Minikube : https://kubernetes.io/fr/docs/setup/learning-environment/minikube/
Tutorial interactif: www.katacoda.com


French tutorial : https://les-tilleuls.coop/fr/blog/article/l-orchestrateur-de-conteneurs-kubernetes-introduction

## Overview


- a node can contain multiple pod
- a pod can contain multiple container

```
+-Serveur Physique/VM---+
| +-Node--------------+ |
| | +-Pod-----------+ | |
| | | +-Container-+ | | |
| | | |           | | | |
| | | +-----------+ | | |
| | +---------------+ | |
| +-------------------+ |
+-----------------------+
```

Object list:
- Nodes : list of host (bare-metal or virtual)
- Pods: One instance of group of containers
- Volumes: Var data sharing with mone or multi contianers
  - See also : PersistentVolume
- Deployments: Scalability metrique, this will create pods
  - See also: ReplicaSet (apply sacalability)
- Services: Used to fixe/connect IP to pod or pods
- Namescape: Like virtual cluster

Manage by:
- kubectl cli options
- using configuration file


Kubernetes:
  - node type: master
    - kube-apiserver:     (API used by kubectl)
    - kube-controller-manager: run all contorlleur in ones
      - Node controller: check/action an node down
      - Replication Controller: use ReplicationContorler to run tyhe good number of pods
      - Endpoints Controller: Joint Service and Pods
      - Service Account & Token controler: Manage compte and token API
    - kube-scheduler: Monitoro deloyment and link pod to node
  - other:
    - cloud-controller-manager: run all controller of the cloud provider
      - Node Controller : Check if node  deleted
      - Route Controller : To add custom link/pah
      - Service Controller: To manage cloud provider load balancer
      - Volume Controller : Manage volume storage in accordant of cloud provider
    - kubelet: Run container execution in Pod.
    - kube-proxy: Proxy connexion with OS systeme or him self



- etcd : databaase key/value HA  used to save all cluster data


Objets Kubernetes:
Bases:
- Pod
- Service
- Volume
- Namespace
Avancé:
- ReplicaSet
- Deplayment
- StefulSet
- DaemnSet
- Job


Kubernetes control plane have a save of all Kubernetes object


Labels is used organise ressource and Annoatation os

Add ons:
- DNS Cluster: DNS serveur
- Dashboard: Web interface
- Tools for Monitoring Resources:
- Logging Architecture

### Install Kubectl

Kubectl est l'outl permetant la gestion d'un cluster K8s ou minikube via le K8s API Objetcs.


```bash
sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
```

Check if Kubectl is installed
```bash
kubectl version
```

### Install MiniKube

Minikude is a VM or docker running a cluster with one node

Check if your CPU suport kubernet
```bash
egrep -q 'vmx|svm' /proc/cpuinfo && echo yes || echo no
```

Install for debian
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_1.7.2-0_amd64.deb \
 && sudo dpkg -i minikube_1.7.2-0_amd64.deb
```

Check if MiniKube is installed
```bash
minikube version
```

### Add On

```
minikube addons list
minikube addons enable dashboard
minikube addons disable dashboard
```


## Run minikube

```bash
#minikube config set vm-driver virtualbox
#minikube delete
minikube start --vm-driver=virtualbox
kubectl cluster-info
kubectl get nodes
```

Create namespace :


```bash
kubectl create namespace example
kubectl get namespace
# Use run and not create to manage pods replication
#kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.10 -n example
#kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.10 -n example

kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.10 --port=9000 --replicas=1 --env="APP_ENV=dev" --labels=”app=api” -n example

kubectl get deployments -n example

kubectl get pods -n example
kubectl get events -n example
kubectl config view
```


Or
```bash
kubectl apply -f ./conf/example -n=example
```

Expose port (.i.e service)
```bash
kubectl expose deployment hello-minikube --type=NodePort --port=8080
kubectl get services
minikube service hello-minikube
```

http://localhost:8888

Tricks
```
export PORT=$(kubectl get svc hello-minikube -o go-template='{{range.spec.ports}}{{if .nodePort}}{{.nodePort}}{{"\n"}}{{end}}{{end}}')
echo "Accessing host01:$PORT"
curl host01:$PORT
```


```
minikube service hello-minikube --url
```


Delete all
```bash
kubectl delete services hello-minikube
kubectl delete deployment hello-minikube
minikube stop
minikube delete
```

### Minikube command

| Description | Command |
|- |- | 
| Display version | ```minikube version```|
| Start | ```minikube start```|
| Display logs | ```minikube logs```|
| Enasble dashboards | ```minikube dashboard```|
| List service | ```minikube service list```|


### Kubectl command

| Description | Command |
|- |- | 
| Display version | ```kubectl version```|
| Display info/logs | ```kubectl cluster-info```|
| Display nodes | ```kubectl get nodes```|
| List pod | ```kubectl get pod```|
| List pod | ```kubectl describe pods```|
| List all namespace | ```kubectl get svc --all-namespaces```|
| Get configuration | ```kubectl get pods --namespace=app --output=yaml``` |
| Make proxy from localhost to cluster | ```kubectl proxi```|

```
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
kubectl logs $POD_NAME
kubectl exec $POD_NAME env
kubectl exec -ti $POD_NAME bash
exit
```

Enable connection from maintenance
```bash
kubectl proxy
```
http://localhost:8001/







## Deploy exemple

```bash
kubectl run http --image=katacoda/docker-http-server:latest --replicas=1
kubectl get deployments
kubectl describe deployment http
```

```bash
kubectl expose deployment http --external-ip="127.0.0.1" --port=8888 --target-port=80
curl http://127.0.0.1:8888
```





Liste of commandes
```bash
# Scale
kubectl scale --replicas=3 deployment http
# Kubernetes Deployments, Services, Pods and PersistentVolumeClaims
kubectl get deployment,svc,pods,pvc
```


YAML
```bash
cat ./yaml/deployment.yaml
kubectl create -f deployment.yaml
kubectl get deployment
kubectl describe deployment webapp1
# Update deployment.yaml
kubectl apply -f deployment.yaml
```

```bash
cat ./yaml/service.yaml
kubectl create -f service.yaml
kubectl get svc
kubectl describe svc webapp1-svc
```


