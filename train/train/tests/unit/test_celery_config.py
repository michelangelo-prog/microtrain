import unittest

from train.domain.config import CeleryConfig, CeleryHeadquarterConfig


class TestCeleryConfig(unittest.TestCase):
    def test_beat_celery_config(self):
        self.assertEqual("redis://redis_train:6379/0", CeleryConfig.CELERY_BROKER_URL)
        self.assertEqual(
            "redis://redis_train:6379/0", CeleryConfig.CELERY_RESULT_BACKEND
        )


class TestCeleryHeadquarterConfig(unittest.TestCase):
    def test_celery_headquarter_config(self):
        self.assertEqual(
            "redis://redis_headquarter:6379/0",
            CeleryHeadquarterConfig.CELERY_BROKER_URL,
        )
        self.assertEqual(
            "redis://redis_headquarter:6379/0",
            CeleryHeadquarterConfig.CELERY_RESULT_BACKEND,
        )


if __name__ == "__main__":
    unittest.main()
