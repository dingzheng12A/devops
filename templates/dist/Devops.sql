-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: Devops
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'test');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add hosts',7,'add_hosts'),(20,'Can change hosts',7,'change_hosts'),(21,'Can delete hosts',7,'delete_hosts'),(22,'Can add host group',8,'add_hostgroup'),(23,'Can change host group',8,'change_hostgroup'),(24,'Can delete host group',8,'delete_hostgroup'),(25,'Can add menu',9,'add_menu'),(26,'Can change menu',9,'change_menu'),(27,'Can delete menu',9,'delete_menu'),(28,'Can add host',10,'add_host'),(29,'Can change host',10,'change_host'),(30,'Can delete host',10,'delete_host'),(31,'Can add metric',11,'add_metric'),(32,'Can change metric',11,'change_metric'),(33,'Can delete metric',11,'delete_metric'),(34,'Can add host',12,'add_host'),(35,'Can change host',12,'change_host'),(36,'Can delete host',12,'delete_host'),(37,'Can add metric',13,'add_metric'),(38,'Can change metric',13,'change_metric'),(39,'Can delete metric',13,'delete_metric');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$qE34hESrgNE0$YvYTCv3MJyNQMpxrgSfhG6N04WI/fnEM9e/Qoxs5jHE=','2018-08-02 05:30:51',1,'admin','','','565165262@qq.com',1,1,'2018-07-25 01:10:30'),(19,'pbkdf2_sha256$100000$NUqAwK53Qigb$QObU3DK9hjPya0zdDubhSmgHeYXZ0td/EdQ9V1Y71PM=','2018-08-01 05:48:37',0,'zhangsan','张三','','zhangsan@qq.com',0,1,'2018-08-01 03:50:17'),(20,'pbkdf2_sha256$100000$iTiTqWZztAa0$p00G7nGgrdPUTkRBkXdw2Bt+1oCsZnvUIAV82vOuZjE=','2018-08-01 06:23:15',0,'lisi','李四','','aaa@bbb.com',0,1,'2018-08-01 06:08:18'),(21,'pbkdf2_sha256$100000$YzgNmWJUgqwG$lx2eVKM+uN8z8H0S3ZthECqgXI9fiXlcQbPAemwOkiE=','2018-08-01 14:00:46',0,'wangwu','王五','','aaa',0,1,'2018-08-01 06:55:41'),(22,'pbkdf2_sha256$100000$SHDKkKGUegq4$V3vA/LhIZRg4pCcmemUkAoky2eqS44YhwzGTw7rYfxQ=','2018-08-01 14:05:39',0,'zhaoliu','赵六','','aaa',0,1,'2018-08-01 06:56:03'),(23,'pbkdf2_sha256$100000$KamjrhyL9WhU$V1Yot4zoQyD/HGmMlgxLvzZbwdOGM+/bJBO9a046kys=',NULL,0,'chenqi','陈七','','123',0,1,'2018-08-01 08:30:19');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(10,'aliyun','host'),(11,'aliyun','metric'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'host','host'),(7,'Host','hosts'),(13,'host','metric'),(8,'hostgroup','hostgroup'),(9,'menu','menu'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-07-17 09:10:41'),(2,'auth','0001_initial','2018-07-17 09:10:42'),(3,'admin','0001_initial','2018-07-17 09:10:42'),(4,'admin','0002_logentry_remove_auto_add','2018-07-17 09:10:42'),(5,'contenttypes','0002_remove_content_type_name','2018-07-17 09:10:42'),(6,'auth','0002_alter_permission_name_max_length','2018-07-17 09:10:42'),(7,'auth','0003_alter_user_email_max_length','2018-07-17 09:10:43'),(8,'auth','0004_alter_user_username_opts','2018-07-17 09:10:43'),(9,'auth','0005_alter_user_last_login_null','2018-07-17 09:10:43'),(10,'auth','0006_require_contenttypes_0002','2018-07-17 09:10:43'),(11,'auth','0007_alter_validators_add_error_messages','2018-07-17 09:10:43'),(12,'auth','0008_alter_user_username_max_length','2018-07-17 09:10:43'),(13,'auth','0009_alter_user_last_name_max_length','2018-07-17 09:10:43'),(14,'sessions','0001_initial','2018-07-17 09:10:43'),(15,'Host','0001_initial','2018-07-17 09:30:55'),(16,'host','0001_initial','2018-07-17 09:32:53'),(17,'hostgroup','0001_initial','2018-07-17 09:43:24'),(18,'host','0002_auto_20180723_0650','2018-07-23 06:51:00'),(19,'host','0003_auto_20180723_0656','2018-07-23 06:56:05'),(20,'host','0004_auto_20180723_0702','2018-07-23 07:02:21'),(21,'host','0005_delete_hosts','2018-07-23 07:27:15'),(22,'menu','0001_initial','2018-07-23 07:27:16'),(23,'menu','0002_auto_20180725_0059','2018-07-25 01:00:44'),(24,'host','0006_host_metric','2018-07-25 02:37:30'),(25,'host','0007_auto_20180725_0623','2018-07-25 06:23:34');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2zei057med2p8pehxqd14pkkpz5nqo70','N2MxZDE3ZDE2MGMxY2RkMjZhODEyNTFiNTVjMDQ2OWRiZGYzMWZkYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiYjc3ZGU5Y2VkOGRlOGVlZDNkOGNmMzUxNjYwYmZhNzQxMjU0MmQwIn0=','2018-08-08 01:10:39'),('f0g5qn3pt0aulwxr6ry10rt4dtdncu3n','NzBlNTQ4MGEzODcwY2Q0OTYwNGUwMmM0ZjViNzhiMzBiOWZjNWNmNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NWNiNTA2MmYwZTMxNmZmYWJiNzVmYzI4OTMzZWNmY2QwOTg2NGYwIiwidXNlcm5hbWUiOiJhZG1pbiJ9','2018-08-16 05:30:51'),('gm0ktha6yr60ugc644bwffbh9p4o6p57','NzBlNTQ4MGEzODcwY2Q0OTYwNGUwMmM0ZjViNzhiMzBiOWZjNWNmNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NWNiNTA2MmYwZTMxNmZmYWJiNzVmYzI4OTMzZWNmY2QwOTg2NGYwIiwidXNlcm5hbWUiOiJhZG1pbiJ9','2018-08-10 06:08:22');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_host`
--

DROP TABLE IF EXISTS `host_host`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `host_host` (
  `id` varchar(100) NOT NULL,
  `region` varchar(20) NOT NULL,
  `az` varchar(20) NOT NULL,
  `mem` int(11) NOT NULL,
  `cpu` int(11) NOT NULL,
  `status` varchar(10) NOT NULL,
  `created` datetime NOT NULL,
  `expire` datetime NOT NULL,
  `instance_type` varchar(20) NOT NULL,
  `instance_name` varchar(50) NOT NULL,
  `hostname` varchar(50) NOT NULL,
  `internet_ip` char(39) NOT NULL,
  `internet_charge` varchar(100) NOT NULL,
  `internal_ip` char(39) NOT NULL,
  `elastic_ip` char(39) NOT NULL,
  `charge_type` varchar(20) NOT NULL,
  `desc` varchar(100) NOT NULL,
  `os_type` varchar(30) NOT NULL,
  `tags` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_host`
--

LOCK TABLES `host_host` WRITE;
/*!40000 ALTER TABLE `host_host` DISABLE KEYS */;
/*!40000 ALTER TABLE `host_host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_metric`
--

DROP TABLE IF EXISTS `host_metric`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `host_metric` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `instanceid` varchar(50) DEFAULT NULL,
  `cpu_avg` int(11) NOT NULL,
  `cpu_max` int(11) NOT NULL,
  `mem_avg` int(11) NOT NULL,
  `mem_max` int(11) NOT NULL,
  `iops_avg` int(11) NOT NULL,
  `iops_max` int(11) NOT NULL,
  `network_avg` int(11) NOT NULL,
  `network_max` int(11) NOT NULL,
  `load_avg` int(11) NOT NULL,
  `load_max` int(11) NOT NULL,
  `created` datetime NOT NULL,
  `writeiops_avg` int(11) NOT NULL,
  `writeiops_max` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_metric`
--

LOCK TABLES `host_metric` WRITE;
/*!40000 ALTER TABLE `host_metric` DISABLE KEYS */;
INSERT INTO `host_metric` VALUES (1,'i-bp138a6dvhdxaua5jdef',2,100,18,19,0,7,10405,1067536,0,0,'2018-07-26 00:00:00',1,72),(2,'i-bp13o9dxrt4fy4texq1h',4,100,76,82,1,2099,67845,7273960,0,0,'2018-07-26 00:00:00',2,111),(3,'i-bp15ed6xe1yxrg7jt5di',4,65,67,76,0,2638,23074,873584,0,0,'2018-07-26 00:00:00',2,906),(4,'i-bp15ed6xe1yxrg7jt5dh',4,52,69,72,0,52,13138,573656,0,0,'2018-07-26 00:00:00',0,169),(5,'i-bp1d5kfq1dixlrc1uzf3',1,25,11,12,0,0,4938,91960,0,0,'2018-07-26 00:00:00',1,92),(6,'i-bp1d5kfq1dixlrc1uzf2',10,100,80,96,25,9000,8576,111128,0,2,'2018-07-26 00:00:00',0,50),(7,'i-bp1d5kfq1dixlrc1uzf4',4,44,74,78,0,254,8892,166400,0,0,'2018-07-26 00:00:00',0,67),(8,'i-bp1a9ki856ngchhvh0xp',1,57,5,6,0,1037,5465,1381736,0,0,'2018-07-26 00:00:00',0,150),(9,'i-bp1628ly4degukupslqi',5,100,32,36,0,16,13830,1875184,0,0,'2018-07-26 00:00:00',0,307),(10,'i-bp1628ly4degukupslqh',5,100,27,31,0,1342,11434,712896,0,0,'2018-07-26 00:00:00',0,325),(11,'i-bp12c0zpe8t4vl28egz0',4,94,35,35,0,14,106547,5659704,0,1,'2018-07-26 00:00:00',5,7000),(12,'i-bp1cynwitmm3x51zgxy4',0,0,0,0,0,0,0,0,0,0,'2018-07-26 00:00:00',0,0),(13,'i-bp1aseg189xcjqw47081',33,100,87,96,65,3540,4791358,90047768,1,33,'2018-07-26 00:00:00',0,333),(14,'i-bp13522n544kqx7tx215',44,100,23,30,0,44,8252390,231552728,2,3,'2018-07-26 00:00:00',1,800),(15,'i-bp17lqgecgbz4egn5d9d',0,0,0,0,0,0,0,0,0,0,'2018-07-26 00:00:00',0,0),(16,'i-bp14cod5rw6yjzqjljts',39,95,14,15,0,333,3160231,23198472,0,3,'2018-07-26 00:00:00',1,818),(17,'i-bp1gl7dlspf26qrr99fw',39,100,14,15,0,947,3160515,25520000,0,3,'2018-07-26 00:00:00',1,722),(18,'i-bp1gl7dlspf26qrr99fv',37,96,14,15,0,242,3159918,24066464,0,1,'2018-07-26 00:00:00',1,823),(19,'i-bp10ukittgtn9yog8ppc',42,96,15,16,0,292,3160064,35035808,1,4,'2018-07-26 00:00:00',1,1052),(20,'i-bp18wrstutw3pfk8imxe',7,72,9,9,1,3046,3596736,32372544,0,0,'2018-07-26 00:00:00',1,739),(21,'i-bp1562i6v4nw64lil3g4',7,73,9,9,1,3148,3596186,31029504,0,0,'2018-07-26 00:00:00',1,789),(22,'i-bp1gxchxpm4qiu1w5d2p',3,90,27,28,0,167,1645,145016,0,0,'2018-07-26 00:00:00',0,1896),(23,'i-bp1bzw4fy0esg0u1nuye',4,70,80,81,0,9,2037,146824,0,0,'2018-07-26 00:00:00',0,214),(24,'i-bp1b5rtmn917ees2bigz',28,100,96,99,9,5050,1278292,78737280,3,3,'2018-07-26 00:00:00',135,56315),(25,'i-bp17c1cena5epvd4wrhq',3,100,84,86,3,2666,62408,163745920,0,1,'2018-07-26 00:00:00',6,21240),(26,'i-bp1h90t5awxwpyf3c0v5',10,100,31,42,2,5833,1050188,58642192,1,1,'2018-07-26 00:00:00',23,118150),(27,'i-bp11vepnzhenwduu2da2',6,100,45,46,0,2603,411278,14462064,0,0,'2018-07-26 00:00:00',2,2470),(28,'i-bp1htw4t0ld5rm1t6dug',45,100,29,33,0,1,2263663,22635160,0,0,'2018-07-26 00:00:00',1,571),(29,'i-bp10c911n2z46d2d3vel',8,100,45,47,0,6,41679,1031896,0,0,'2018-07-26 00:00:00',1,1047),(30,'i-bp1gtcdnye17apg0h217',2,100,75,76,0,44,3839,168272,0,0,'2018-07-26 00:00:00',2,913),(31,'i-bp1a4d6crd1vft1siuw6',3,100,53,54,0,1552,54455,1792016,0,1,'2018-07-26 00:00:00',1,2157),(32,'i-bp1dgb871dbnnwv46gt5',15,100,23,30,0,341,684324,203146040,1,1,'2018-07-26 00:00:00',43,84782),(33,'i-bp12vc6gxsllet61tbdz',7,100,38,39,1,1444,250494,1300608,1,1,'2018-07-26 00:00:00',3,36184),(34,'i-bp1ie9r8wb0blmmunvfx',12,100,49,63,1,1556,230899,29730856,1,1,'2018-07-26 00:00:00',3,33790),(35,'i-bp1ie9r8wb0blmmunvfz',14,100,46,60,1,2419,229952,33332168,1,1,'2018-07-26 00:00:00',4,101487),(36,'i-bp1ie9r8wb0blmmunvfy',16,100,51,68,0,1684,1498774,58258064,0,1,'2018-07-26 00:00:00',2,40233),(37,'i-bp1ie9r8wb0blmmunvg0',14,100,79,82,0,1996,1460724,67066840,0,1,'2018-07-26 00:00:00',1,10234),(38,'i-bp147cvofreatuak9n5m',20,100,85,85,1,3369,1749278,9399872,1,1,'2018-07-26 00:00:00',3,31747),(39,'i-bp147cvofreatuak9n5o',20,100,85,86,1,1076,1751689,9821272,1,1,'2018-07-26 00:00:00',3,28671),(40,'i-bp147cvofreatuak9n5n',10,100,33,34,0,1074,476169,1941624,1,1,'2018-07-26 00:00:00',5,46713),(41,'i-bp1bjvditkxbln1o81q4',5,100,60,60,0,3084,118015,37959272,0,1,'2018-07-26 00:00:00',1,32782),(42,'i-bp10zkx5pckc33updsmt',4,100,81,85,1,1745,4786,28954344,1,1,'2018-07-26 00:00:00',0,631),(43,'i-bp1aehttqhrmymb4x14r',6,100,68,76,3,4148,161944,41499384,0,0,'2018-07-26 00:00:00',3,43779),(44,'i-bp1innyuqc4lo3elszen',5,100,49,49,0,1698,196091,1139608,1,1,'2018-07-26 00:00:00',3,37052),(45,'i-bp1aehttqhrmymb4x14p',8,100,82,86,1,1601,6056,142792,0,0,'2018-07-26 00:00:00',0,333),(46,'i-bp17ykmwwdhka7vc8t16',12,100,34,35,0,1318,542084,3388312,1,1,'2018-07-26 00:00:00',6,43664),(47,'i-23vspo7m8',8,100,29,29,2,1548,50195,3390712,0,1,'2018-07-26 00:00:00',91,12175),(48,'i-2361g17c5',13,100,67,68,0,1865,563334,14725792,1,1,'2018-07-26 00:00:00',3,9758),(49,'i-23bbi6smj',23,100,46,65,3,1680,2762479,21293048,0,1,'2018-07-26 00:00:00',3,1909),(50,'i-23qferbuv',3,50,40,42,0,1211,73117,32402256,0,0,'2018-07-26 00:00:00',2,3903),(51,'i-23iiu918t',6,100,50,50,0,0,2984,425792,0,0,'2018-07-26 00:00:00',1,600),(52,'i-23atfmnfx',6,100,56,56,1,1594,52636,12970032,1,1,'2018-07-26 00:00:00',0,384),(53,'i-23tq1lsrg',31,100,65,68,6,4093,104215,827178992,1,1,'2018-07-26 00:00:00',22,12065),(54,'i-23vfzfcsc',8,100,61,62,0,641,17342,94238808,1,1,'2018-07-26 00:00:00',5,13047),(55,'i-23sihaf8x',4,100,19,21,2,4812,3566,458576,0,0,'2018-07-26 00:00:00',1,533),(56,'i-23fqyvvdp',6,97,46,54,20,4130,665437,168995784,0,2,'2018-07-26 00:00:00',27,48625),(57,'i-23ajbmdjk',9,100,34,38,0,421,3195780,80398352,0,0,'2018-07-26 00:00:00',6,3151),(58,'i-6wef3f3em19p61s6gljg',0,0,0,0,0,0,0,0,0,0,'2018-07-26 00:00:00',0,0),(59,'i-6wef3f3em19p5zt5cjkb',0,0,0,0,0,0,0,0,0,0,'2018-07-26 00:00:00',0,0),(60,'i-6we68dcri8njyvle8vx9',0,0,0,0,0,0,0,0,0,0,'2018-07-26 00:00:00',0,0),(61,'i-6we68dcri8njyvle8vxa',0,0,0,0,0,0,0,0,0,0,'2018-07-26 00:00:00',0,0),(62,'i-p0w9y9fe38i09a22v6ip',2,63,22,29,0,2,19028,446776,0,0,'2018-07-26 00:00:00',1,627),(63,'i-p0wiifqxi5v7rfpgefst',8,100,49,51,0,657,2339584,1297389504,0,0,'2018-07-26 00:00:00',1,2000),(64,'i-p0wiifqxi5v7rfpgefss',16,100,23,28,0,16,1321658,119074920,0,0,'2018-07-26 00:00:00',1,925),(65,'i-p0wai5d3hbwn81strleq',4,100,51,55,0,72,35402,26693760,0,0,'2018-07-26 00:00:00',4,13208),(66,'i-rj9cpzov101xtn8ozrw1',2,100,17,19,0,81,8981,281248,0,0,'2018-07-26 00:00:00',1,1824),(67,'i-rj961qs3tbt48n5amcau',5,100,52,63,0,208,25341,423272,0,1,'2018-07-26 00:00:00',3,506),(68,'i-rj961qs3tbt48n5amcav',3,100,33,35,0,7,18458,536136,0,0,'2018-07-26 00:00:00',0,162),(69,'i-rj9d8hsewm5hvp5vxxiy',16,100,71,72,1,1473,1335431,6227728,0,0,'2018-07-26 00:00:00',2,1842),(70,'i-rj9jf31z3tdvassdb1s6',28,98,52,58,3,2762,1267519,70159112,0,0,'2018-07-26 00:00:00',1,935),(71,'i-rj9dlo96sxrc1fvfoobl',14,100,42,43,2,1607,1334833,54876760,0,0,'2018-07-26 00:00:00',1,827),(72,'i-rj99h0nuwcmb1bcxor3s',2,65,64,66,0,1910,21652,70292280,0,0,'2018-07-26 00:00:00',7,25760),(73,'i-rj95gsizckkm6t9l94qt',7,100,59,59,0,1,35304,380072,0,0,'2018-07-26 00:00:00',3,1684),(74,'i-rj9h2fyiaanmfa1upt2j',2,100,13,13,0,913,2733,1055144,0,1,'2018-07-26 00:00:00',0,454),(75,'i-rj9e1przeygcvrzlhxrr',11,100,20,24,0,1,189297,46805952,1,1,'2018-07-26 00:00:00',11,11080),(76,'i-rj9de8ndqh28cr1d71fb',49,100,43,46,0,405,6123179,114348952,3,4,'2018-07-26 00:00:00',4,10559),(77,'i-u1f5r73ug',12,100,54,63,5,1517,915208,52950600,1,2,'2018-07-26 00:00:00',59,60000),(78,'i-gw84ox1dtqribeadty2s',0,0,0,0,0,0,0,0,0,0,'2018-07-26 00:00:00',0,0),(79,'i-gw83hho0zov8xhkjnupp',9,92,55,58,1,1653,1906441,1176150232,0,0,'2018-07-26 00:00:00',1,1347),(80,'i-gw83hho0zov8xhkjnupo',21,97,54,58,2,1762,1811511,92552072,0,0,'2018-07-26 00:00:00',1,1391),(81,'i-gw8d5hecfeq3oy165mtu',4,100,48,52,0,1651,42036,53714056,0,0,'2018-07-26 00:00:00',6,15500);
/*!40000 ALTER TABLE `host_metric` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostgroup_hostgroup`
--

DROP TABLE IF EXISTS `hostgroup_hostgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hostgroup_hostgroup` (
  `id` int(11) NOT NULL,
  `group_name` varchar(256) NOT NULL,
  `group_desc` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostgroup_hostgroup`
--

LOCK TABLES `hostgroup_hostgroup` WRITE;
/*!40000 ALTER TABLE `hostgroup_hostgroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `hostgroup_hostgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_menu`
--

DROP TABLE IF EXISTS `menu_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_menu` (
  `id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `parent_id` int(11) NOT NULL,
  `url` varchar(128) NOT NULL,
  `sort` int(11) NOT NULL,
  `span_id` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_menu`
--

LOCK TABLES `menu_menu` WRITE;
/*!40000 ALTER TABLE `menu_menu` DISABLE KEYS */;
INSERT INTO `menu_menu` VALUES (0,'aaa',0,'',0,0,'0000-00-00 00:00:00');
/*!40000 ALTER TABLE `menu_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ttt`
--

DROP TABLE IF EXISTS `ttt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ttt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ttt`
--

LOCK TABLES `ttt` WRITE;
/*!40000 ALTER TABLE `ttt` DISABLE KEYS */;
INSERT INTO `ttt` VALUES (1,'张三',15),(2,'李四',20),(3,'王五',16),(4,'陈七',18),(5,'赵六',20),(6,'孙八',22);
/*!40000 ALTER TABLE `ttt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'Devops'
--

--
-- Dumping routines for database 'Devops'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-02 16:27:57
