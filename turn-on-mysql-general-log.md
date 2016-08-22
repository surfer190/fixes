How to turn on Mysql General Log

1. Add the log settings in `/etc/mysql/my.cnf`

    ```
    [mysqld]
    general_log_file = /var/log/mysql/mysql.log
    general_log = 1
    ```

2. In Mysql:

    ```
    > SET GLOBAL general_log='OFF';
    ```

3. `service mysql restart`
