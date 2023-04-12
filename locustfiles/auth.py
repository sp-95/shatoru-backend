# from locust import HttpUser, task


# class AuthUser(HttpUser):
#     """
#     Locust user class for testing authentication endpoints.
#     """

#     @task
#     def login(self):
#         """
#         Task for testing user login.
#         """
#         self.client.post(
#             "/auth/login/",
#             json={
#                 "username": "testuser",
#                 "password": "testpass",
#             },
#         )

#     # @task
#     # def change_password(self):
#     #     """
#     #     Task for testing changing user password.
#     #     """
#     #     self.client.login(username='testuser', password='testpass')
#     #     self.client.patch("/password/change/1/", json={"password": "newpass"})

#     # @task
#     # def reset_password(self):
#     #     """
#     #     Task for testing resetting user password.
#     #     """
#     #     self.client.post("/password/reset/", json={"email": "testuser@example.com"})


import json

from locust import HttpUser, task


class AuthUser(HttpUser):
    # """
    # A Locust user that simulates password reset requests.
    # """

    # # Set the wait time between requests to be between 1 and 2 seconds
    # wait_time = between(1, 2)

    # @task
    # def password_reset(self):
    #     """
    #     Simulate a password reset request.
    #     """

    #     # Make a POST request to the password reset API endpoint
    #     response =
    # self.client.post("/password_reset/", json={"email": "test@example.com"})

    #     # Check that the response was successful
    #     assert response.status_code == 200

    #     # Check that an email was sent to the user
    #     assert "email" in response.json()
    #     assert response.json()["email"] == "test@example.com"

    @task
    def login(self):
        # Login endpoint
        response = self.client.post(
            "/auth/login/",
            data=json.dumps({"username": "admin", "password": "admin"}),
            headers={"content-type": "application/json"},
        )
        if response.status_code == 200:
            auth_token = response.json()["token"]
            self.client.headers["Authorization"] = f"Token {auth_token}"

    # @task
    # def change_password(self):
    #     # Change password endpoint
    #     response =
    # self.client.post('/auth/password/change/',
    #
    # data=json.dumps({'old_password': 'my_old_password',
    #
    # 'new_password': 'my_new_password'}),
    #
    # headers={'content-type': 'application/json'})
    #     if response.status_code == 200:
    #         # If password was changed successfully, update the auth token
    #         auth_token = response.json()['access_token']
    #         self.client.headers['Authorization'] =
    # f'Bearer {auth_token}'

    # @task
    # def reset_password(self):
    #     # Request password reset endpoint
    #     response = self.client.post('/auth/password/reset/',
    #     data=json.dumps({'email': 'my_email@example.com'}),
    #     headers={'content-type': 'application/json'})

    #     # Confirm email was sent
    #     assert response.status_code == 200

    #     # Retrieve password reset token from email (hypothetical)
    #     reset_token = 'my_password_reset_token'

    #     # Password reset endpoint
    #     response = self.client.post('/auth/password/reset/confirm/',
    #                                 data=json.dumps({'token': reset_token,
    #                                                  'password': 'my_new_password'}),
    #                                 headers={'content-type': 'application/json'})

    #     # Confirm password was reset successfully
    #     assert response.status_code == 200
