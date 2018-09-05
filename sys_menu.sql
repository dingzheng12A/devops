-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: Devops
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `sys_menu`
--

LOCK TABLES `sys_menu` WRITE;
/*!40000 ALTER TABLE `sys_menu` DISABLE KEYS */;
INSERT INTO `sys_menu` VALUES (1,'用户管理',0,'用户管理','2018-08-30 07:02:24'),(2,'添加用户',1,'/addUser?page=1','2018-08-30 07:03:33'),(3,'删除用户',1,'/dropUser?page=1','2018-08-30 07:03:49'),(4,'角色管理',0,'角色管理','2018-08-30 07:04:22'),(5,'添加角色',4,'/addRole?page_role=1','2018-08-30 07:05:16'),(6,'删除角色',4,'/dropRole?page_role=1','2018-08-30 07:05:46'),(7,'菜单管理',0,'菜单管理','2018-08-30 07:06:12'),(8,'添加菜单',7,'/menumanager/addmenu','2018-08-30 07:07:23'),(9,'删除菜单',7,'/menumanager/dropmenu','2018-08-30 07:08:15'),(10,'测试菜单1',0,'测试菜单1','2018-08-30 08:14:56'),(11,'测试子菜单1',10,'/test?page=1','2018-08-30 08:15:21'),(12,'aaa1',0,'aaa1','2018-08-30 09:53:55'),(13,'aa',12,'aaa','2018-08-30 09:54:04'),(14,'xxxx',0,'xxxx','2018-08-31 06:38:28'),(15,'xxx1',14,'xx1','2018-08-31 06:38:43');
/*!40000 ALTER TABLE `sys_menu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-04 20:21:53
