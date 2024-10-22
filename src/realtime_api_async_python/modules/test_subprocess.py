import subprocess

browser_command = "start"  # This will open the default browser on Windows
response = type('Response', (object,), {'url': 'http://example.com'})  # Mock response object

subprocess.Popen(f"{browser_command} {response.url}", shell=True)