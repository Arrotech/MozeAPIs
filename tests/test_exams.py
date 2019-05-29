import json

from utils.dummy import entry, new_entry, Invalid_exam_key, Invalid_exam_key_put
from .base_test import BaseTest


class TestExams(BaseTest):
    """Test exams."""
    def test_add_exams(self):
        """Test that the add exams endpoint works."""
        response = self.client.post(
            '/api/v1/portal/exams', data=json.dumps(new_entry), content_type='application/json',
            headers=self.get_admin_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Entry created successfully!')
        assert response.status_code == 201

    # def test_Invalid_exam_key(self):
    #     """Test the vote json keys."""
    #     response = self.client.post(
    #         '/api/v1/portal/exams', data=json.dumps(Invalid_exam_key), content_type='application/json',
    #         headers=self.get_admin_token())
    #     result = json.loads(response.data.decode('utf-8'))
    #     self.assertEqual(result['message'], 'Invalid admission_no key')
    #     assert response.status_code == 400

    def test_get_exams(self):
        """Test fetching all offices that have been created."""

        response = self.client.post(
            '/api/v1/portal/exams', data=json.dumps(new_entry), content_type='application/json',
            headers=self.get_admin_token())
        response1 = self.client.get(
            '/api/v1/portal/exams', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "successfully retrieved")
        assert response1.status_code == 200

    # def test_edit_exam_maths(self):
    #     """Test name json values."""
    #     response1 = self.client.post(
    #         '/api/v1/portal/exams', data=json.dumps(new_entry), content_type='application/json',
    #         headers=self.get_token())
    #     response = self.client.put(
    #         '/api/v1/portal/exams/1', data=json.dumps(entry), content_type='application/json',
    #         headers=self.get_admin_token())
    #     result = json.loads(response.data.decode())
    #     self.assertEqual(result['message'], 'Scores successfully updated')
    #     assert response.status_code == 200

    # def test_get_exam_by_admission(self):
    #     """Test getting a specific party by id."""
    #
    #     response = self.client.post(
    #         '/api/v1/portal/exams', data=json.dumps(new_entry), content_type='application/json',
    #         headers=self.get_token())
    #     response1 = self.client.get(
    #         '/api/v1/portal/exams/1', content_type='application/json', headers=self.get_token())
    #     result = json.loads(response1.data.decode())
    #     self.assertEqual(result['message'],
    #                      'successfully retrieved')
    #     assert response1.status_code == 200
