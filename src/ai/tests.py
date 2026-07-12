from django.contrib.auth import get_user_model
from django.test import TestCase

from ai.tools import get_document_by_id, list_documents
from documents.models import Document


class ToolContextTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="tester", password="secret123")
        self.document = Document.objects.create(owner=self.user, title="Sample Doc")

    def test_list_documents_accepts_configuration_context(self):
        config = {"configuration": {"user_id": self.user.id}}

        result = list_documents.invoke(None, config)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], self.document.title)

    def test_get_document_by_id_accepts_configuration_context(self):
        config = {"configuration": {"user_id": self.user.id}}

        result = get_document_by_id.invoke({"document_id": self.document.id}, config)

        self.assertEqual(result["name"], self.document.title)
