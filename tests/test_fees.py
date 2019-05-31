import json

from utils.dummy import add_fees
from .base_test import BaseTest


class TestFees(BaseTest):
    """Test exams."""
    def test_add_id(self):
        """Test that the add exams endpoint works."""
        response = self.client.post(
            '/api/v1/fees', data=json.dumps(add_fees), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Entry made successsfully')
        assert response.status_code == 201

    def test_get_ids(self):
        """Test fetching all offices that have been created."""
        response = self.client.post(
            '/api/v1/fees', data=json.dumps(add_fees), content_type='application/json',
            headers=self.get_admin_token())
        response1 = self.client.get(
            '/api/v1/fees', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "successfully retrieved")
        assert response1.status_code == 200
