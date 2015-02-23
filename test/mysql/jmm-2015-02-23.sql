CREATE DATABASE  IF NOT EXISTS `jmm` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `jmm`;
-- MySQL dump 10.13  Distrib 5.6.13, for Win32 (x86)
--
-- Host: 192.168.0.250    Database: jmm
-- ------------------------------------------------------
-- Server version	5.5.28

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
-- Table structure for table `ani`
--

DROP TABLE IF EXISTS `ani`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ani` (
  `i` int(11) NOT NULL,
  `n` varchar(500) DEFAULT NULL,
  `w` tinyint(4) DEFAULT NULL,
  `t` datetime DEFAULT NULL,
  PRIMARY KEY (`i`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ani`
--

LOCK TABLES `ani` WRITE;
/*!40000 ALTER TABLE `ani` DISABLE KEYS */;
INSERT INTO `ani` VALUES (1,'역시 이중에 하나 이 애니메이션이 이렇게 쓰레기일리가 없다는 것은 잘못됐다는 사실을 우리는 아직 모른다는 것은 아무리 생각해도 너희들이 나쁘지만 사랑만 있으면 상관없잖아?',1,'2015-01-05 23:30:00');
/*!40000 ALTER TABLE `ani` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mach`
--

DROP TABLE IF EXISTS `mach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mach` (
  `i` int(11) NOT NULL,
  `n` varchar(20) DEFAULT NULL,
  `a` varchar(20) DEFAULT NULL,
  `p` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`i`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mach`
--

LOCK TABLES `mach` WRITE;
/*!40000 ALTER TABLE `mach` DISABLE KEYS */;
INSERT INTO `mach` VALUES (1,'자막기계A','test1','ab0ee213d0bc9b7f69411817874fdfe6550c640b5479e5111b90ccd566c1163b'),(2,'자막기계B','test2','6016bcc377c93692f2fe19fbad47eee6fb8f4cc98c56e935db5edb69806d84f6'),(3,'자막기계C','test3','97b868b8503c20875cb0a0e37c418a7166d78304c9384ef0d864ece47d1803ac');
/*!40000 ALTER TABLE `mach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub`
--

DROP TABLE IF EXISTS `sub`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sub` (
  `ai` int(11) DEFAULT NULL,
  `mi` int(11) DEFAULT NULL,
  `e` float DEFAULT NULL,
  `u` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub`
--

LOCK TABLES `sub` WRITE;
/*!40000 ALTER TABLE `sub` DISABLE KEYS */;
INSERT INTO `sub` VALUES (1,1,1,'http://mrotaku.tistory.com/entry/2015Q1-이렇게-쓰레기-상관없잖아-1화-자막'),(1,1,2,'http://mrotaku.tistory.com/entry/2015Q1-이렇게-쓰레기-상관없잖아-2화-자막'),(1,2,1,'http://mrotaku.tistory.com/entry/2015Q1-이렇게-쓰레기-상관없잖아-1화-자막');
/*!40000 ALTER TABLE `sub` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-02-23 11:58:45
