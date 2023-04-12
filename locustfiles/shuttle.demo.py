import json

from locust import HttpUser, between, task


class ShuttleDemo(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        # Authenticate with the API
        response = self.client.post(
            "/auth/login/",
            data={
                "username": "admin",
                "password": "admin",
            },
        )
        if response.status_code != 200:
            raise Exception("Failed to authenticate with the API")
        self.access_token = json.loads(response.content)["token"]

    @task
    def list_schedules(self):
        self.client.get(
            "/shuttles/schedules/",
            headers={"Authorization": f"Token {self.access_token}"},
        )

    @task(1)
    def list_shuttles(self):
        self.client.get(
            "/shuttles/",
            headers={"Authorization": f"Token {self.access_token}"},
        )
