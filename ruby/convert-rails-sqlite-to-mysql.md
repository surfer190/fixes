# Convert Rails SQLlite to use MySQL

1. In `Gemfile`: Replace `gem 'sqllite3'` to `gem 'mysql2'`

2. Change the database configuration `config/database.yml`:

```
default: &default
  adapter: mysql2
  encoding: utf8
  pool: 5
  timeout: 5000
  username: <yourusername>
  password: <yourpassword>
  socket: /var/run/mysqld/mysqld.sock

development:
  <<: *default
  database: apiflysaa_dev
```

#### Check Socket

```
mysqladmin -u root -p variables | grep socket
```

### Giving Permissions

```
GRANT ALL PRIVILEGES ON dbTest.* To
 'user'@'hostname' IDENTIFIED BY 'password';
```

Source:

* [Check Mysql Socket](http://stackoverflow.com/questions/25171327/mysql2error-cant-connect-to-local-mysql-server-through-socket-tmp-mysql-so)
* [MySQL Permissions](http://stackoverflow.com/questions/1720244/create-new-user-in-mysql-and-give-it-full-access-to-one-database)
* [Convert Rails to use SQLLite to MySQL](https://teamtreehouse.com/forum/how-to-let-ruby-app-know-to-use-mysql-instead-of-sqlite3)
