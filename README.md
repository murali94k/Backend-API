# Openshift_Devops
This is to learn deployment to openshift

## setting up docker mysql instance

1. Pull and run mysql image 
```
docker run -d -p 3306:3306 --name mysql_db
 -e MYSQL_ROOT_PASSWORD=root 
 -e MYSQL_DATABASE=nodejs_db 
 -e MYSQL_USER=root
 -e MYSQL_PASSWORD=root mysql/mysql-server:latest
```

2. Setting up schema and DB
```
docker cp ./sqldump.sql mysql_db:/tmp/
```
```
docker exec -it mysql_db /bin/bash
```
```
mysql -uroot -proot < /tmp/sqldump.sql
```

3. ecec into mysl shell
```commandline
mysql -u root -p 
```