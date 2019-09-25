import json

from utils.dummy import add_service, wrong_add_services_keys, wrong_phone

from .base_test import BaseTest


class TestAddServices(BaseTest):
    """Testing that a registered user can add a service."""

    def test_add_service(self):
        """A user can add a service."""
        response = self.client.post(
            '/api/v1/add_services', data=json.dumps(add_service), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'You have successfully added the service!')
        assert response.status_code == 201


    def test_add_services_keys(self):
        """Test add services json keys."""
        response = self.client.post(
            '/api/v1/add_services', data=json.dumps(wrong_add_services_keys), content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Invalid portfolio key')
        assert response.status_code == 400

    def test_get_services(self):
        """Test fetching all services that have been added."""
        response = self.client.post(
            '/api/v1/add_services', data=json.dumps(add_service), content_type='application/json')
        response1 = self.client.get(
            '/api/v1/add_services', content_type='application/json')
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "success")
        assert response1.status_code == 200

    def test_get_service(self):
        """Test getting a service by occupation."""
        response1 = self.client.post(
            '/api/v1/add_services', data=json.dumps(add_service), content_type='application/json')
        response = self.client.get(
            '/api/v1/add_services/carpenter', content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'success')
        assert response.status_code == 200

    def test_get_service_by_location(self):
        """Test getting a service by occupation and location."""
        response1 = self.client.post(
            '/api/v1/add_services', data=json.dumps(add_service), content_type='application/json')
        response = self.client.get(
            '/api/v1/add_services/carpenter/nakuru', content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'success')
        assert response.status_code == 200

    def test_get_unexisting_service(self):
        """Test getting an unexisting service."""
        response = self.client.get(
            '/api/v1/add_services/carpent', content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'service not found')
        assert response.status_code == 404

    def test_get_unexisting_service_by_location(self):
        """Test getting an unexisting service."""
        response = self.client.get(
            '/api/v1/add_services/carpenter/njoro', content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'service not found')
        assert response.status_code == 404
