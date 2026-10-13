import pytest
from lab.moduleOne import LabModuleOne


@pytest.fixture
def lab_module():
    """Створює об'єкт і скидає його після завершення тесту."""
    module = LabModuleOne()
    yield module
    module.reset_value()


@pytest.fixture
def lab_module_after_one_increment(lab_module):
    lab_module.increment()
    yield lab_module
    lab_module.decrement()  # Повертаємо значення до попереднього стану


@pytest.fixture
def lab_module_after_two_increments(lab_module_after_one_increment):
    module = lab_module_after_one_increment
    module.increment()
    yield module
    module.decrement()  # Повертаємо значення до попереднього стану


@pytest.mark.unit
@pytest.mark.lab_module_one
@pytest.mark.fixtures
def test_lab_module_one_initial_value(lab_module):
    assert lab_module.value == 0


@pytest.mark.unit
@pytest.mark.lab_module_one
@pytest.mark.fixtures
def test_lab_module_one_incremented_value(lab_module_after_one_increment):
    assert lab_module_after_one_increment.value == 1


@pytest.mark.unit
@pytest.mark.lab_module_one
@pytest.mark.fixtures
def test_lab_module_one_incremented_twice(lab_module_after_two_increments):
    assert lab_module_after_two_increments.value == 2


@pytest.mark.unit
@pytest.mark.lab_module_one
@pytest.mark.fixtures
def test_lab_module_one_reset_value(lab_module_after_one_increment):
    lab_module_after_one_increment.increment()
    lab_module_after_one_increment.reset_value()
    assert lab_module_after_one_increment.value == -1
