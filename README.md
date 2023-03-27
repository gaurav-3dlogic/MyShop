﻿# MyShop


## How to install it?

- First Clone this repo

```cmd
    git clone https://github.com/gaurav-3dlogic/MyShop.git
```

- Change into the project directory

```cmd
    cd MyShop
```

- Create a Virtualenv and the project directory

```cmd
    virtualenv env
```

- Activate the virtualenv

```cmd
    env/Scripts/activate
```

- Install the project Dependencies

```cmd
    pip install -r requirements.txt
```

- Make The Migrations To the database

```cmd
    python manage.py migrate
```

- Create a superuser

```cmd
    python manage.py createsuperuser
```
- Spin Up The Django Developement Server

```cmd
    python manage.py runserver
```

Now You Are all set and the server Is Running on the url http://localhost:8000 and can create the products from django admin.
