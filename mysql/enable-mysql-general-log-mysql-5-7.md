# How to Enable MySQL general Log in Mysql 5.6


        vim /etc/mysql/my.cnf

        [mysqld]
        general_log_file = /var/log/mysql/mysql.log
        general_log = 1

Connect through mysql (mysql -u <username> -p) and run :

        SET general_log = 1;

Restart MySql

        sudo service mysql restart 

Source:

* [AskUbuntu MySQL](https://askubuntu.com/questions/699964/how-to-activate-mysql-general-log-in-version-5-6)