import unittest

from headquarter.domain.config import CeleryConfig


class TestCeleryConfig(unittest.TestCase):
    def test_beat_celery_config(self):
        self.assertEqual(
            "redis://redis_headquarter:6379/0", CeleryConfig.CELERY_BROKER_URL
        )
        self.assertEqual(
            "redis://redis_headquarter:6379/0", CeleryConfig.CELERY_RESULT_BACKEND
        )


if __name__ == "__main__":
    unittest.main()
