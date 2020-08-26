# Hands-on DB-05 : Installing Wordpress App on EC2 and RDS

Purpose of the this hands-on training is to create a LAMP (Linux, Apache, MariaDB, PHP) stack in EC2 Instance and run a Wordpress application with Database hosted in RDS.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- setup an environment and install LAMP stack.

- install and configure Wordpress.

- configure connection between EC2 instance and Database.

- set up the database for Wordpress App.

- back up tha database and migrate it to RDS DB Instance.

## Outline

- Part 1 - Preparing the Environment and Installing LAMP Stack without Database

- Part 2 - Installing and Configuring Database

- Part 3 - Setting Up the Connection between EC2 and Database

- Part 4 - Creating DB Tables and Populating with Data

- Part 5 - Migrating Database to the RDS DB Instance

## Part 1 - Preparing the Environment and Installing LAMP Stack without Database

### Step 1 - Creating Security Group

- Create 2 Security Groups:

```text
    1. Wordpress_Instance_Sec_Group: SSH 22, HTTP 80, Mysql/Aurora 3306  > anywhere(0:/00000)
    2. RDS_Database_Sec_Group: Mysql/Aurora 3306 > anywhere (0:/00000)
```

### Step 2 - Creating RDS Instance

- First, go to the Amazon RDS Service and select `Database` section from the left-hand menu, click databases and then click `Creating Database`.

- Choose a database creation method.

```text
Standard Create
```

- Select engine option.

```text
MySQL
```

- Select version.

```text
8.0.20 (latest)
```

- Select template.

```text
free tier
```

- Configure settings.

```text
DB instance identifier: RDS-mysql
Master password: admin
Master username: Pl123456789
```

- Select DB instance size.

```text
Burstable classes (includes t classes) : db.t2.micro
```

- Select storage.

```text
Storage type          : SSD
Storage size          : default 20GiB
Storage autoscaling   : unchecked
```

- Availability & durability.

```text
We can not select any option for free tier
```

- Configure connectivity.

```text
vpc                           : default

click Additional connectivity configuration;

Subnet group                  : default
Publicly accessible           : Yes
Existing VPC security groups  : Default, RDS_Database_Sec_Group
Availability Zone             : No preference
Database port                 : 3306
```

- Set database authentication.

```text
DB authentication: Password authentication
```

- Additional configuration.

```text
Initial DB name                   : clarusway
DB parameter group & option group : default
Automatic backups                 : enable
Backup retention period: 7 days (Explain how)

Select window for backup to show snapshots
Monitoring  : Unchecked
Log exports : Unchecked
Maintance
  - Enable auto minor version upgrade: Enabled (Explain what minor and major 
upgrade are)
  - Maintance window (be careful not to overlap maintance and backup windows)
deletion protection: enabled
```

- Click `Create Database` button.

### Step 3 - Creating EC2 Instance

- Create EC2 and install LAMP stack with user data using the following setup for Wordpress App.

- Configure instance.

- Set user data.

- Set Security Group as `Wordpress_Instance_Sec_Group`.

### Step 4 - Creating a Client Instance

- Create client EC2 instance with following setup and connect with SSH.

- Configure instance.

- Set user data.

- Set Security Group as `Wordpress_Instance_Sec_Group`.

## Part 2 - Installing and Configuring Database

- Go to the Wordpress EC2 Instance on console.

- Paste the DNS of Wordpress EC2 instance into the browser and show the `Error` of establishing a database connection

- Connect EC2 Instance named `Wordpress_Instance` with SSH.

- Check the Apache Server status.

- Check the PHP version.

- Check the MariaDB status and show that there is no MariaDB server running.

- Install MariaDB.

- Start MariaDB server.

- Enable MariaDB service, so that MariaDB service will be activated on restarts.

- Setup secure installation of MariaDB.

- Connect to MariaDB terminal.

- Create new database named `clarusway`.

- Show newly created database.

- Create a user named `admin`.

- Grant permissions to the user `admin` for database `clarusway`.

- Update privileges.

- Close the MariaDB terminal

## Part 3 - Setting Up the Connection between EC2 and Database

- Show the current path with `pwd`

- Go to the `/var/www/html/`" to back up the config file before changing.

- Change the config file as shown below to enable connection with database.

- Check the browser. You'll see the home page of Wordpress (enter password, user name etc.)

## Part 4 - Creating DB Tables and Populating with Data

- Log into the database again to populate tables with data.

- Show databases and select the database `clarusway` db.

- Create a table named `store`.

```sql
CREATE TABLE `store` (
  `store_id` int(11) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

- Insert sample data into the table `store`.

```sql
INSERT INTO `store` VALUES (1,'03 Reinke Trail','Cincinnati','OH');
INSERT INTO `store` VALUES (2,'5507 Becker Terrace','New York City','NY');
INSERT INTO `store` VALUES (3,'54 Northland Court','Richmond','VA');
INSERT INTO `store` VALUES (4,'08 South Crossing','Cincinnati','OH');
INSERT INTO `store` VALUES (5,'553 Maple Drive','Minneapolis','MN');
INSERT INTO `store` VALUES (6,'23 North Plaza','Aurora','CO');
INSERT INTO `store` VALUES (7,'9658 Wayridge Court','Boise','ID');
INSERT INTO `store` VALUES (8,'9 Grayhawk Trail','New York City','NY');
INSERT INTO `store` VALUES (9,'16862 Westend Hill','Knoxville','TN');
INSERT INTO `store` VALUES (10,'4 Bluestem Parkway','Savannah','GA');
```

- Create a table named `client`.

```sql
CREATE TABLE `client` (
  `client_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

- Insert sample data into the table `client`.

```sql
INSERT INTO `client` VALUES (37270,'Yovonnda','Magrannell');
INSERT INTO `client` VALUES (33391,'Darcy','Nortunen');
INSERT INTO `client` VALUES (37851,'Sayer','Matterson');
INSERT INTO `client` VALUES (40448,'Mindy','Crissil');
INSERT INTO `client` VALUES (56274,'Keriann','Alloisi');
INSERT INTO `client` VALUES (63196,'Alaster','Scutchin');
INSERT INTO `client` VALUES (67009,'North','de Clerc');
INSERT INTO `client` VALUES (67370,'Elladine','Rising');
INSERT INTO `client` VALUES (68249,'Nisse','Voysey');
INSERT INTO `client` VALUES (72540,'Guthrey','Iacopetti');
INSERT INTO `client` VALUES (72913,'Kass','Hefferan');
INSERT INTO `client` VALUES (75900,'Virge','Goodrum');
INSERT INTO `client` VALUES (76196,'Mirilla','Janowski');
INSERT INTO `client` VALUES (80529,'Lynde','Aronson');
```

- Show newly created tables.

- Check the tables if the data is there.

- Exit from database.

## Part 5 - Migrating Database to the RDS DB Instance

- Connect to the RDS DB instance to create `clarusway` database.

- Create new database named `clarusway`;

- Show newly created database and exit.

- Connect to the client instance.

- Create back-up of `clarusway` database from the `Wordpress Instance`, within `Client EC2`.

- Migrate `clarusway` database to the RDS instance using the back-up file within `Client EC2`.

- Log into database with RDS to check if `clarusway` migrated correctly.

- Select the `clarusway` db and show data within tables of `client` and `store`.
