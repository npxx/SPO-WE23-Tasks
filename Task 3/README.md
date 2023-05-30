# Task 3

- [x] Framework used : Django
- [x] Open source encryption package used : `bcrypt`
(this algorithm has a disadvantage that max length of password can only be upto 72 characters)

*Django automatically takes care of sanitation of input and prevention of SQL injections*

```python
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User(username=username)
        user.set_password(password)
        user.save()

        return redirect('index')

    return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)

        if user is not None:
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                print(f"User {username} successfully authenticated.")
                return render(request,'dashboard.html')
        else:
            print(f"Authentication failed for user {username}.")

        #Just for debugging purposes

        password_hash = user.password
        print(password_hash)
        print(f"Username entered : {username}, Password: {password}")
        print_bcrypt_hash(password)

    return render(request, 'login.html')
```
    
    
User model
```python
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

def set_password(self, raw_password):
    self.password = hashpw(raw_password.encode('utf-8'), gensalt()).decode('utf-8')
```

Database linkage (in `settings.py`)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


| welcome page | login page(also redirected when login fails) | signup page | dashboard |
| --- | --- | --- | --- |
|![image](https://github.com/npxx/SPO-WE23-Tasks/assets/96121824/8951023f-f29f-4568-b671-34855709db12)|![image](https://github.com/npxx/SPO-WE23-Tasks/assets/96121824/60a2804b-7a9e-49d7-a30a-ecd49e1bbb2c)|![image](https://github.com/npxx/SPO-WE23-Tasks/assets/96121824/199362b7-b67f-404c-bcc1-5699203d0a13)|![image](https://github.com/npxx/SPO-WE23-Tasks/assets/96121824/838b997a-0681-4193-b5d0-dbcda13e61f4)|


(In other implementations, Prevention of SQL injections into database can be taken care of by using parameterized queries and proper input sanitation; i.e. handling escape characters)
