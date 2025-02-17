import unittest
from statsig import StatsigEvent, StatsigUser, StatsigOptions, StatsigServer

class TestBadInput(unittest.TestCase):
    
    def test_bad_key(self):
        with self.assertRaises(ValueError) as context:
            statsig = StatsigServer()
            statsig.initialize(None)
   
        self.assertTrue('Server Secret Key' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            statsig = StatsigServer()
            statsig.initialize("client-blah")
   
        self.assertTrue('Server Secret Key' in str(context.exception))
    
    def test_no_user_id(self):
        with self.assertRaises(ValueError) as context:
            StatsigUser("")
   
        self.assertTrue('user_id' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            StatsigUser(None)
   
        self.assertTrue('user_id' in str(context.exception))
    
    def test_invalid_tier(self):
        with self.assertRaises(ValueError) as context:
            StatsigOptions(tier=123)
   
        self.assertTrue('StatsigEnvironmentTier' in str(context.exception))
    
    def test_bad_events(self):
        with self.assertRaises(ValueError) as context:
            StatsigEvent(None, None)
   
        self.assertTrue('StatsigEvent.user must be set' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            StatsigEvent(StatsigUser("test"), None)

        self.assertTrue('StatsigEvent.event_name must be a valid str' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            StatsigEvent(StatsigUser("test"), "test_event", value=dict())
   
        self.assertTrue('StatsigEvent.value must be a str, float, or int' in str(context.exception))

if __name__ == '__main__':
    unittest.main()