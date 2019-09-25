# Django
from django.contrib.auth.hashers import check_password

# Utilities
import psycopg2

# Conections
from inventsoft.connections_pool import threaded_postgreSQL_pool

def authenticate(username=None, password=None):
    try:
        tcp = threaded_postgreSQL_pool
        connection = tcp.getconn()
        cursor = connection.cursor()
        query = f'SELECT * FROM employee WHERE email = \'{username}\''
        cursor.execute(query)
        resp = cursor.fetchone()
        column_names = [desc[0] for desc in cursor.description]
        user_val = [value for value in resp]
        user = {column:user_val[i] for i, column in enumerate(column_names)}
        if check_password(password, user['password']):
            if user['is_superuser'] == True and user['is_area_admin'] == False:
                user['type'] = 0
            elif user['is_superuser'] == False and user['is_area_admin'] == True:
                user['type'] = 1
            elif user['is_superuser'] == False and user['is_area_admin'] == False:
                user['type'] = 2
            else:
                user['type'] = 3
            
            return user      
        return None 
    except Exception as e:
        return None  
    finally:
        if (tcp):
            tcp.putconn(connection)
            print("Threaded PostgreSQL connection pool is closed")

def get_user(user_id):
    try:
        tcp = threaded_postgreSQL_pool
        connection = tcp.getconn()
        cursor = connection.cursor()
        query = f'SELECT * FROM employee WHERE emp_key = \'{user_id}\''
        cursor.execute(query)
        resp = cursor.fetchone()
        column_names = [desc[0] for desc in cursor.description]
        user_val = [value for value in resp]
        user_val = zip(column_names, user_val)
        user = {column:user_val[i] for i, column in enumerate(column_names)}
        user['backend'] = 'apps.usuarios.authentication.EmailAuthBackend'
        return user
    except Exception as e:
        return None
    finally:
        if (tcp):
            tcp.putconn(connection)
            print("Threaded PostgreSQL connection pool is closed")

"""

>>> from django.contrib.auth.hashers import make_password, check_password
>>> contra = 'edgar123' 
>>> ciph_contra = make_password(contra) 
>>> print(ciph_contra) 
pbkdf2_sha256$150000$wE9JmStZJWPh$TRMl/z4tXQYs2VqerMc3di0d0trHq2tPANELEoxmjm4=  
>>> contra_input = 'edgar123'
>>> did_match = check_password(contra_input, ciph_contra) 
>>> print(did_match) 
True

INSERT INTO Employee VALUES('A001','edgar@mail.com','pbkdf2_sha256$150000$wE9JmStZJWPh$TRMl/z4tXQYs2VqerMc3di0d0trHq2tPANELEoxmjm4=','Edgar', 'Gómez', '2019-09-23 09:46:31.22461-05', NULL, TRUE, FALSE);

"""