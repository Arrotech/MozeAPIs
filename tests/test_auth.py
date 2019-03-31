import json

from utils.dummy import create_account, user_login, new_account, new_login, new_account1, wrong_firstname, \
    wrong_lastname, wrong_surname, wrong_form, wrong_email
from .base_test import BaseTest


class TestUsersAccount(BaseTest):
    """Testing the users account endpoint."""

    def get_token(self):
        self.client.post('/api/v1/portal/auth/register', data=json.dumps(create_account),
                         content_type='application/json')
        resp = self.client.post('/api/v1/portal/auth/login', data=json.dumps(user_login),
                                content_type='application/json')
        access_token = json.loads(resp.get_data(as_text=True))['token']
        auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
        return auth_header

    def test_create_account(self):
        """Test the vote json keys."""

        response = self.client.post(
            '/api/v1/portal/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Account created successfully!')
        assert response.status_code == 201

    def test_login(self):
        """Test the vote json keys."""

        response1 = self.client.post(
            '/api/v1/portal/auth/register', data=json.dumps(new_account1), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/portal/auth/login', data=json.dumps(new_login), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Successfully logged in!')
        assert response.status_code == 200

    def test_invalid_email_login(self):
        """Test the vote json keys."""

        response = self.client.post(
            '/api/v1/portal/auth/login', data=json.dumps(new_login), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Invalid Email or Password')
        assert response.status_code == 401

    def test_wrong_firstname(self):
        """Test the vote json keys."""

        response = self.client.post(
            '/api/v1/portal/auth/register', data=json.dumps(wrong_firstname), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'firstname is in wrong format')
        assert response.status_code == 400

    def test_wrong_lastname(self):
        """Test the vote json keys."""

        response = self.client.post(
            '/api/v1/portal/auth/register', data=json.dumps(wrong_lastname), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'lastname is in wrong format')
        assert response.status_code == 400

    def test_wrong_surname(self):
        """Test the vote json keys."""

        response = self.client.post(
            '/api/v1/portal/auth/register', data=json.dumps(wrong_surname), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'surname is in wrong format')
        assert response.status_code == 400

    def test_wrong_form(self):
        """Test the vote json keys."""

        response = self.client.post(
            '/api/v1/portal/auth/register', data=json.dumps(wrong_form), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'select from 1, 2, 3 or 4')
        assert response.status_code == 400

    def test_wrong_email(self):
        """Test the vote json keys."""

        response = self.client.post(
            '/api/v1/portal/auth/register', data=json.dumps(wrong_email), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Invalid Email Format!')
        assert response.status_code == 400
