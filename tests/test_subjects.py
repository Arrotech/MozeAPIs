import json

from utils.dummy import new_subject
from .base_test import BaseTest


class TestSubjects(BaseTest):
    """Test exams."""
    def test_add_subjects(self):
        """Test that the add exams endpoint works."""
        response = self.client.post(
            '/api/v1/subjects', data=json.dumps(new_subject), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Subjects registered successfully!')
        assert response.status_code == 201

    def test_get_subjects(self):
        """Test fetching all offices that have been created."""

        response = self.client.post(
            '/api/v1/subjects', data=json.dumps(new_subject), content_type='application/json',
            headers=self.get_admin_token())
        response1 = self.client.get(
            '/api/v1/subjects', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "successfully retrieved")
        assert response1.status_code == 200

    # def test_get_subject(self):
    #     """Test getting a specific party by id."""
    #
    #     response = self.client.post(
    #         '/api/v1/subjects', data=json.dumps(new_subject), content_type='application/json',
    #         headers=self.get_token())
    #     response1 = self.client.get(
    #         '/api/v1/subjects/1', content_type='application/json', headers=self.get_token())
    #     result = json.loads(response1.data.decode())
    #     self.assertEqual(result['message'],
    #                      'success')
    #     assert response1.status_code == 200
