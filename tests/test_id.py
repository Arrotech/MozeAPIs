import json

from utils.dummy import add_student_info
from .base_test import BaseTest


class TestId(BaseTest):
    """Test Id."""
    def test_add_id(self):
        """Test that the add exams endpoint works."""
        response = self.client.post(
            '/api/v1/id', data=json.dumps(add_student_info), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Id assigned successfully')
        assert response.status_code == 201

    def test_get_ids(self):
        """Test fetching all offices that have been created."""
        response = self.client.post(
            '/api/v1/id', data=json.dumps(add_student_info), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.get(
            '/api/v1/id', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "Retrieved successfully")
        assert response1.status_code == 200
