"""
Tests for Resource class
Command line: python -m pytest tests/unit/test_resource.py
"""

import pytest

from app.models import inventory


@pytest.fixture
def resource_values():
    return {
        'name': 'Parrot',
        'manufacturer': 'Pirates A-Hoy',
        'total': 100,
        'allocated': 50
    }


@pytest.fixture
def resource(resource_values):
    return inventory.Resource(**resource_values)


def test_create_resource(resource_values, resource):
    for attr_name in resource_values:
        assert getattr(resource, attr_name) == resource_values.get(attr_name)


@pytest.mark.parametrize('total, allocated', [(10, -5), (10, 20)])
def test_create_invalid_allocated_value(total, allocated):
    with pytest.raises(ValueError):
        inventory.Resource('name', 'manu', total, allocated=allocated)
