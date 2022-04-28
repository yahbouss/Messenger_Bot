# How to build

to setup, you need to install selenium using `pip`

`pip install selenium`

Install your prefered webdriver and update this line with the one you chose (if you're using chrome, leave it like this)

`self.driver = webdriver.Chrome()`

'if it doesn't work, add a path of your webdriver

Make a file in the same folder with the name `LoginInfo.py`
Write in it your login info
```
username = 'your login info'   
password = 'your password'
target = 'your target'
message = 'your message'
```