### Documentation

# Namespaces

* Project - group of environments
* Organization - group of projects

# Environment

* environment (collection of applications, databases and services needed to run a piece of software) is described in `bunnyshell.yaml` file
* environment specs [here](https://documentation.bunnyshell.com/docs/ref-yaml-definition)

# Components

* Represent the building blocks of an environment
* Types of components:
    * k8s compatible components: `KubernetesManifest` `Helm`
    * build components: `DockerImage`
    * docker compose components: `Application`, `Database`, `Service` (anything that is not app or db, e.g.caches, queues, etc.)
    * customizable components: `GenericComponent`

---

# Create environment via docker compose

* The conversion from `docker-compose.yaml` to `bunnyshell.yaml` is **one-time and one-way**.
* For each component in `docker-compose` bunyshell will create the needed k8s objects:
    * `dockerCompose.environment` will create a `ConfigMap`
    * `dockerCompose.ports` will create a `Service`
    * `hosts` will create a `Ingress`



