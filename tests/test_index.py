import unittest

class TestWebpage(unittest.TestCase):
    def test_h1_exists(self):
        with open("index.html", "r") as f:
            content = f.read()
        self.assertIn("<h1>", content, "No <h1> tag found in index.html")

if __name__ == "__main__":
    unittest.main()
