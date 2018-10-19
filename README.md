## Guestbook Example

This example shows how to build a simple, multi-tier web application using Kubernetes and [Docker](https://www.docker.com/).

We will be using [Minikube](https://github.com/kubernetes/minikube) to install our application locally.


The example consists of:

- A web frontend
- A [redis](http://redis.io/) master (for storage), and a replicated set of redis 'slaves'.

The web frontend interacts with the redis master via javascript redis API calls.

**Note**:  If you are running this example on a [Google Container Engine](https://cloud.google.com/container-engine/) installation, see [this Google Container Engine guestbook walkthrough](https://cloud.google.com/container-engine/docs/tutorials/guestbook) instead. The basic concepts are the same, but the walkthrough is tailored to a Container Engine setup.

## Building Your Own Image
You can use the images already pre-defined in the kubernetes manifest files or you can use the below to create your own images and use them:

Replace the realbtotharye with your Dockerhub repository

```
docker build -t realbtotharye/flask-kubernetes-nginx nginx/
docker push realbtotharye/flask-kubernetes-nginx

docker build -t realbtotharye/flask-kubernetes-redis flask-redis/
docker push realbtotharye/flask-kubernetes-redis
```

### Prerequisites

Make sure to install [Minikube](https://github.com/kubernetes/minikube) and then proceed with ensuring kubectl works and your cluster is up.

This example requires a running Kubernetes cluster. First, check that kubectl is properly configured by getting the cluster state:

```console
$ kubectl cluster-info
```

If you see a url response, you are ready to go.

### Quick Start

This section shows the simplest way to get the example work. If you want to know the details, you should skip this and read [the rest of the example](#step-one-start-up-the-redis-master).

Start the guestbook with one command:

Ensure you are in the working dir

```
cd kubernetes-flask-example
```

```console
$ kubectl create -f .
service "redis-master" created
deployment "redis-master" created
service "redis-slave" created
deployment "redis-slave" created
service "frontend" created
deployment "frontend" created
```

Then, list all your Services:

```console
$ kubectl get services
NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
frontend       NodePort    10.99.150.67    <none>        80:32515/TCP   34s
kubernetes     ClusterIP   10.96.0.1       <none>        443/TCP        48m
redis-master   ClusterIP   10.104.124.32   <none>        6379/TCP       34s
redis-slave    ClusterIP   10.104.43.119   <none>        6379/TCP       34s
```

Now with using minikube we can run the following to get the url for the service and access our app:

```
minikube service frontend --url
```

Use the URL given to us here and we can access it.  If you are not using minikube then you can access this via the ClusterIP or setup a load balancer or proxy to access the application.

Clean up the guestbook:

```console
$ kubectl delete -f .
```