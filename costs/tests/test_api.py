import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_expense_list_requires_authentication(api_client):
    response = api_client.get(reverse("expense-list"))
    assert response.status_code == 401


def test_authenticated_user_can_see_list(auth_client):
    response = auth_client.get(reverse("expense-list"))
    assert response.status_code == 200