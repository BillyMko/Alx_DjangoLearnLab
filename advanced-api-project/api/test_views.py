from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
       
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )
        self.book_list_url = reverse("book-list")
        self.book_detail_url = reverse("book-detail", args=[self.book.id])

    def test_get_all_books(self):

        response = self.client.get(self.book_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_get_single_book(self):

        response = self.client.get(self.book_detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_requires_authentication(self):
        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }

        response = self.client.post(self.book_list_url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):

        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }

        response = self.client.post(self.book_list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):

        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(self.book_detail_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.book_detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
