<div align="center">
  <img src="https://user-images.githubusercontent.com/38591616/122379565-e3c2c500-cf5e-11eb-8200-321df6858a13.png">
  
  <h1><i>Roomie - Renting Platform</i></h1>
</div>

## 📖 Description

Roomie consists in a web platform where landlords can post their houses, and tenants can search for openings in houses. Each tenant has his evaluation scores that other users can access in order to decide if they want to live with them. Landlords can accept applications or reject them. This repository contains all stages of developoment, from modeling and low-fidelity prototypes, to a fully functional production version.

## 🚀 Deployment

### Full dpeloyment (Ansible + GCP + Docker + Docker Swarm)

#### Prerequisites

-   [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
-   [Python 3](https://www.python.org/downloads)
-   [pip3](https://pip.pypa.io/en/stable/installing/)
-   Google Cloud Service Account (in JSON format), with permissions to manage networking interfaces and Cloud Compute VMs (a disabled example is provided)

#### Installation

```bash
pip3 install requests google-auth
ansible-galaxy collection install google.cloud
ansible-galaxy collection install ansible.posix
ansible-galaxy collection install community.docker
```

#### Execution

-   To run a full provisioning (which creates all VMs, then installs all of the required components on them):

    ```bash
    ANSIBLE_CONFIG=ansible.cfg ansible-playbook playbook.yml --tags "create-vms,provision"
    ```

-   To delete the VMs (and, by extension, terminate the deployment):

    ```bash
    ANSIBLE_CONFIG=ansible.cfg ansible-playbook playbook.yml --tags "delete-vms"
    ```

-   To scale up or down a service:

    -   Available services:

        -   frontend - default of 3 replicas
        -   backend - default of 3 replicas

    -   Examples:
        ```bash
        ANSIBLE_CONFIG=ansible.cfg ansible-playbook -i hosts.gcp.yml scale.yml -e "frontend=3"
        ANSIBLE_CONFIG=ansible.cfg ansible-playbook -i hosts.gcp.yml scale.yml -e "frontend=3 backend=1"
        ```

#### Orchestration

The orchestration tool used in this assignment is [Docker Swarm](https://docs.docker.com/get-started/swarm-deploy). This phase of deployment is the result of improving the work described in the [Intermediate Installation section](#intermediate-installation).

#### Provisiong

This deployment uses [Ansible](https://www.ansible.com) to automate provisioning and configuration of the application on [Google Cloud Platform](https://cloud.google.com).

### Basic Deployment (Docker + Docker Compose)
The Docker deployment contains four components in three containers:
    - Frontend Web Server
    - Backend App Server
    - Postgres Database

To run all of this, use ``docker-compose`` on the main directory:
```bash
docker-compose up --build -d
```

## 🤝 Authors

-   **Diogo Ribeiro:** [ribeiropdiogo](https://github.com/ribeiropdiogo)
-   **José Diogo Monteiro:** [dxmonteiro](https://github.com/DxMonteiro)
-   **João Nuno Abreu:** [JoaoNunoAbreu](https://github.com/JoaoNunoAbreu)
-   **Rui Mendes:** [ruimendes29](https://github.com/ruimendes29)
-   **Vasco Ramos:** [vascoalramos](https://vascoalramos.me)


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
