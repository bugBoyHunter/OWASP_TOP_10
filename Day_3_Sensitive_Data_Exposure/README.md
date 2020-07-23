## Sensitive data Exposure

#1 Have a look around the webapp. The developer has left themselves a note indicating that there is sensitive data in a specific directory. 

What is the name of the mentioned directory

```
/assets
```

#2 Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?
```
webapp.db
```

#3 Use the supporting material to access the sensitive data. What is the password hash of the admin user?
```
sqlite3 webapp.db

.tables // To list all tables

PRAGMA table_info(users); //To list fields of the tables

SELECT * FROM users; // To list all data
```

#4 Crack the hash.
What is the admin's plaintext password?

[Crackstation](https://crackstation.net/)

#5 Login as the admin. What is the flag?
```
use the password 
```
