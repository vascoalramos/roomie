<div align="center">
  <img src="https://user-images.githubusercontent.com/38591616/122379565-e3c2c500-cf5e-11eb-8200-321df6858a13.png">
  
  <h1><i>Roomie - Renting Platform</i></h1>
</div>

## 📖 Description

Roomie consists in a web platform where landlords can post their houses, and tenants can search for openings in houses. Each tenant has his evaluation scores that other users can access in order to decide if they want to live with them. Landlords can accept applications or reject them. This repository contains all stages of developoment, from modeling and low-fidelity prototypes, to a fully functional production version.

## ✏️ Modeling and Prototype

### Modeling Diagrams
Modeling diagrams (such as Use Case Diagram or Class Diagram) are located in the [modeling folder](modeling).

### Low-Fidelity Prototype
Low-fidelity prototypes are located in the  [prototypes folder](prototypes). There is also the possibility to interact with a dynamic prototype that was built using figma, [here](https://www.figma.com/proto/QI3glrnfyr5FPTlQFCQNmb/Prototype?node-id=10%3A1356&scaling=min-zoom&page-id=2%3A1302).

## 💪 Getting Started (run locally)

### 🏢 Backend

#### 📥 Prerequisites
The following software is required to be installed on your system:
- JDK 11+
- PostgreSQL

#### 🧰 How to Run
1. Create Database and User
    ```bash
    sudo -u postgres psql
    postgres=# create database roomie;
    postgres=# create user roomie with encrypted password 'passw0rd';
    postgres=# grant all privileges on database roomie to roomie;
    ```

2. Run Project
Execute (in IntelliJ) by running `RestApiApplication.java` file.

3. Create DB Schema
Execute endpoint http://localhost:8083/api/admin/create-db.

### 💻 Frontend

#### :inbox_tray: Prerequisites

The following software is required to be installed on your system:

-   [nodejs](https://nodejs.org/en/download/)

#### :wrench: Installation

Use the package manager [npm](https://www.npmjs.com/) to install dependencies.

```bash
npm i
```

#### :hammer: Execution

```bash
npm run serve
```

## 🚀 Deployment
To deploy a production-grade instalation check out our [deployment branch](https://github.com/vascoalramos/roomie/tree/deployment).

## 🛠️ Extras

#### 👥 Population

We created a small program to populate ou system with users and houses. To do so, navigate to the `populate` folder and run:

```bash
python3 populate.py
```

#### 📖 Documentation 

In order to help the frontend development process and to document our REST API, we used swagger to generate some documentation. This can be accessed by running the backend and opening [this page](http://localhost:8083/api/docs).

#### 📈 Benchmarks

To test our applications capacity and performance we created some usefull tests with locust. These tests can be found in the [benchmarking folder](benchmarking).


## 🤝 Authors

-   **Diogo Ribeiro:** [ribeiropdiogo](https://github.com/ribeiropdiogo)
-   **José Diogo Monteiro:** [dxmonteiro](https://github.com/DxMonteiro)
-   **João Nuno Abreu:** [JoaoNunoAbreu](https://github.com/JoaoNunoAbreu)
-   **Rui Mendes:** [ruimendes29](https://github.com/ruimendes29)
-   **Vasco Ramos:** [vascoalramos](https://vascoalramos.me)


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
