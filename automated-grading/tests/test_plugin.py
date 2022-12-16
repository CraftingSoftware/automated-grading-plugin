import unittest


class TestCollectConfig(unittest.TestCase):
    def test_collect_config(self):
        # Set up test data
        expected_config = {...}

        # Call the collect_config function
        collect_config()

        # Check that the configuration was collected correctly
        self.assertEqual(manager.config, expected_config)


if __name__ == "__main__":
    unittest.main()
