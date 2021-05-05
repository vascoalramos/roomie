from locust import HttpUser, task
from config import UserSimulationConfig

# 1 -> register
# 2 -> login
# 3 -> search for houses
# 4 -> apply to house(s)
# 5 -> remove one application


class TenantWorkload(HttpUser):
    wait_time = UserSimulationConfig.wait_time_between_tasks

    def on_start(self):
        self.client.get("https://github.com/")

    @task
    def simulate(self):
        pass

    @task
    def index(self):
        headers = {"content-type": "application/json"}
        payload = {"email": "test@test.com", "password": "test"}
        response = self.client.post("/api/auth/login", json=payload, headers=headers)