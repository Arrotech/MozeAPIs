import json

from utils.dummy import entry, new_entry, Invalid_exam_key, Invalid_exam_key_put, new_account, wrong_exam_keys, admin_account_test
from .base_test import BaseTest


class TestExams(BaseTest):
    """Test exams."""
    def test_add_exams(self):
        """Test that the add exams endpoint works."""
        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/exams', data=json.dumps(new_entry), content_type='application/json',
            headers=self.get_admin_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Entry created successfully!')
        assert response.status_code == 201

    def test_add_exams_with_unexisting_user(self):
        """Test that the add exams endpoint works."""
        response = self.client.post(
            '/api/v1/exams', data=json.dumps(new_entry), content_type='application/json',
            headers=self.get_admin_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Student with that Admission Number does not exitst.')
        assert response.status_code == 404

    def test_get_exams(self):
        """Test fetching all exams that have been created."""

        response = self.client.post(
            '/api/v1/exams', data=json.dumps(new_entry), content_type='application/json',
            headers=self.get_admin_token())
        response1 = self.client.get(
            '/api/v1/exams', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "successfully retrieved")
        assert response1.status_code == 200

    def test_get_unexisting_exam(self):
        """Test getting unexisting specific exam by admission_no."""
        response1 = self.client.get(
            '/api/v1/exams/NJCF4057', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         'Exam Not Found')
        assert response1.status_code == 404

    def test_unexisting_exams_url(self):
        """Test when unexisting url is provided."""
        response = self.client.get(
            '/api/v1/exam', headers=self.get_token())
        result = json.loads(response.data.decode())
        assert response.status_code == 404
        assert result['message'] == "resource not found"

    def test_method_not_allowed(self):
        """Test method not allowed."""
        response = self.client.put(
            '/api/v1/exams', data=json.dumps(new_entry), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'method not allowed')
        assert response.status_code == 405

    def test_delete_exams(self):
        """Test deleting a specific exam."""
        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_admin_token())
        response = self.client.post(
            '/api/v1/exams', data=json.dumps(new_entry), content_type='application/json',
            headers=self.get_admin_token())
        response1 = self.client.delete(
            '/api/v1/exams/NJCF4001', content_type='application/json', headers=self.get_admin_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         'Exam deleted successfully')
        assert response1.status_code == 200

    def test_delete_unexisting_exams(self):
        """Test deleting unexisting exam."""
        response1 = self.client.delete(
            '/api/v1/exams/NJCF4057', content_type='application/json', headers=self.get_admin_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         'Exam not found')
        assert response1.status_code == 404
