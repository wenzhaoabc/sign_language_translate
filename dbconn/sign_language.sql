-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: db_sign
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_news`
--

DROP TABLE IF EXISTS `t_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `image` varchar(255) DEFAULT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_news`
--

LOCK TABLES `t_news` WRITE;
/*!40000 ALTER TABLE `t_news` DISABLE KEYS */;
INSERT INTO `t_news` VALUES (1,'无障碍服务团队','无障碍服务倡议解读','<h1 style=\"text-align: center;\">文明办关于提高社会无障碍服务保障的通知</h1>\r\n<p style=\"text-align: center;\"><span style=\"font-size: 14px;\">社会主义核心价值观文明办公室</span></p>\r\n<p style=\"text-align: center;\"><span style=\"font-size: 14px;\">2023年5月18日</span></p>\r\n<p style=\"text-align: left;\"><span style=\"font-size: 16px;\">各区县：</span></p>\r\n<p style=\"text-align: left;\"><span style=\"font-size: 16px;\">为切实加强我县残障人士的生活质量，现对各场所无障碍服务做出如下倡议：</span></p>\r\n<p style=\"text-align: left;\"><span style=\"font-size: 16px;\"><img src=\"https://s2.loli.net/2023/05/18/oG6LuTybQtK4EP9.png\"></span></p>\r\n<p style=\"text-align: left;\"><span style=\"font-size: 16px;\">请严格落实以上规定内容。</span></p>\r\n<p style=\"text-align: right;\"><span style=\"font-size: 16px;\">县委文明办公室</span></p>','https://s2.loli.net/2023/05/30/elGvLFitQybrmzO.png','2023-05-18 13:37:35'),(2,'转自人民政府网','国务院关于加强残障人士权益保护的倡议','<h1 style=\"text-align: center;\">文明办关于提高社会无障碍服务保障的通知</h1>\r\n<p style=\"text-align: center;\"><span style=\"font-size: 14px;\">社会主义核心价值观文明办公室</span></p>\r\n<p style=\"text-align: center;\"><span style=\"font-size: 14px;\">2023年5月18日</span></p>\r\n<p style=\"text-align: left;\"><span style=\"font-size: 16px;\">各区县：</span></p>\r\n<p style=\"text-align: left;\"><span style=\"font-size: 16px;\">为切实加强我县残障人士的生活质量，现对各场所无障碍服务做出如下倡议：</span></p>\r\n<p style=\"text-align: left;\"><span style=\"font-size: 16px;\"><img src=\"https://s2.loli.net/2023/05/18/oG6LuTybQtK4EP9.png\"></span></p>\r\n<p style=\"text-align: left;\"><span style=\"font-size: 16px;\">请严格落实以上规定内容。</span></p>\r\n<p style=\"text-align: right;\"><span style=\"font-size: 16px;\">县委文明办公室</span></p>','https://s2.loli.net/2023/05/28/2JWRquXnUpj3Hfo.png','2023-05-28 14:25:53'),(3,'光明网','传递心灵的力量：手语盲文有了“国标”','<h1 style=\"text-align: center;\">传递心灵的力量：手语盲文有了&ldquo;国标&rdquo;</h1>\r\n<span class=\"channel cf\">\r\n<span class=\"col-1-1 fl\" style=\"text-align: right;\">2021年12月12日08:33 | 来源：<a href=\"http://www.chinanews.com.cn/sh/2021/12-12/9627845.shtml\" target=\"_blank\" rel=\"noopener\">光明日报</a></span>\r\n</span>\r\n<span class=\"rm_txt_con cf\">\r\n<span class=\"otitle\">&nbsp;</span>\r\n<p>　　手语和盲文是特殊的语言文字形态，是听力和视力残疾人思维、学习和交流的重要工具，是国家语言文字的重要组成部分。然而，不同地区手语打法差异大、盲文拼写不规范等问题，一定程度上制约了我国3000多万听力和视力残疾人之间的沟通和交往，甚至影响到了他们的日常学习、就业和生活。因此，推广国家通用手语和国家通用盲文至关重要。本期《语言文字》聚焦如何更好推进手语&ldquo;普通话&rdquo;和盲文&ldquo;规范字&rdquo;的普及应用，保障视听障人士的语言文字权利。</p>\r\n<p>　　<strong>盲文信息化助推交互无障碍(作者：钟经华)</strong></p>\r\n<p>　　盲文是视力残疾人语言文字权益的核心，是提高盲人文化教育水平的关键，是盲人共享文化权益、教育权益平等的保障。推进盲文信息化、出版规范化，关乎我国1700多万视力残疾人文化素质的提高，关乎残疾人实现全面小康的进程。这是&ldquo;十三五&rdquo;物质生活脱贫后，&ldquo;十四五&rdquo;视力残疾人精神文化生活脱贫的攻坚战。</p>\r\n<p>　　&ldquo;十三五&rdquo;期间，由教育部、国家语委、中国残联发布的《国家通用盲文方案》解决了近70年来一直悬而未决的盲文读音不规范问题，在保持盲文稳定、新旧衔接的前提下，实现了盲文由&ldquo;猜&rdquo;到&ldquo;读&rdquo;的转变，结束了盲文&ldquo;猜调&rdquo;的历史。国家通用盲文能够准确地记录国家通用语言的声韵调，使我国盲人有了相当于汉语拼音功能的文字工具，能够准确地使用国家通用语言。</p>\r\n<p>　　国家通用盲文实现了读音规范化，分词连写问题成为国家通用盲文进一步规范化、信息化的绊脚石。在语料库建设过程中，我们发现了盲文分词连写问题的全貌，违反语法、语义逻辑、语用习惯的现象俯拾皆是，零散的单音节大量存在。同一个语义单元内分写，两个不同语义单元之间连写。盲人中间流传的&ldquo;该连的没连、该分的没分&rdquo;典型示例大量涌现。</p>\r\n<p>　　目前的分词连写不仅没有实现提高盲文表义能力的初衷，还成为国家通用盲文规范化、信息化最后的瓶颈。研制面向盲校教学等多领域的系统完整、逻辑自洽、细则简明、可操作性高的分词连写规则已迫在眉睫。简明分词连写规则配以高精度的智能分词连写词库，以&ldquo;规则+词库&rdquo;的组合方式能兼顾盲文教学、出版及信息化、规范化的需求。</p>\r\n<p>　　从汉字到盲文的翻译，核心难点在于分词和读音标注。盲文的分词连写规则涉及语义和语法信息，很难被计算机描述和处理，导致基于规则的方法性能不佳。针对当前汉盲翻译的问题，要引入最新的深度学习技术，基于机器学习模型自动学习盲文分词规则和多音字、轻声的辨析规则，实现高准确率的汉盲翻译。</p>\r\n<p>　　针对盲文与汉字分别存储，盲文文档容易丢失对应的汉字信息这一问题，需要研究和制定国家通用盲文全息(盲文-拼音-汉字)存储标准，在字符串级别实现盲文-拼音-汉字的对照存储，使得盲人在阅读电子盲文文档时，可以随时根据需要获取盲文、汉字、拼音中的一种或多种精确对照的信息，并可进一步将其转换为语音等其他通道信息，实现多通道、多模态的全息阅读体验。</p>\r\n<p>　　目前，盲文的校对环节还存在极大的提升空间。研究开发盲文翻译&ldquo;一明对多盲&rdquo;支持技术。对盲文校对环节明眼人和盲人一对一配合，盲人摸读盲文内容，明眼人对照原文进行检错和纠错进行彻底的技术革新，实现盲人基本独立无障碍完成校对流程，取代两人协作带来的工作流程复杂性、效率低、成本高的校对模式。</p>\r\n<p>　　针对国家通用盲文出版应用研究问题，深度开发盲文编辑软件的纠错功能，支持样本训练、样本学习，对不同用户的手动纠错结果进行数据复用。在正确理解原文内容的基础上，实现校对流程的语音朗读、盲文点显器显示，能够使用计算机键盘快捷键在原文和盲文之间进行快速而直接的查阅和比对。引入在线联网纠错服务，实现自动对汉语文本中的分词连写、标调、标点、疑难词等多种问题进行纠错校对，同时在原文和盲文中提示错误位置并返回修改建议。实现快捷键在各纠错结果之间进行查看，对纠错内容进行手动二次纠错，使盲人可无障碍操作。</p>\r\n<p>　　当前，移动电子设备上的盲文信息处理技术尚不完善，为缩小或消除&ldquo;信息鸿沟&rdquo;，需要开展移动电子设备盲文信息处理技术研究及应用。重点突破智能电子设备上的盲文信息化与交互无障碍问题。研究盲文与点位汉字编码互转的算法，为盲文的语音识别与转换奠定基础。研究盲人触摸手势采集、清洗、归一化、数据标注、数据训练、模型计算等关键技术。研究多重触控手势识别、盲文与手势关系匹配等构建方法。研究国家通用盲文与语音双向转换，实现盲文的语音识别和语音输出。</p>\r\n<p>　　此外，开展数理化公式、电路图、几何图、音乐乐谱盲文信息处理关键技术研究也是加快推进盲文规范化信息化的重要路径。</p>\r\n<p>　　<strong>特殊语言文字学科建设 为手语盲文规范化提供科学支撑(作者：顾定倩)</strong></p>\r\n<p>　　党的十八大以来，我国手语和盲文规范化行动进入了一个&ldquo;黄金期&rdquo;，取得了一系列重要成果。同时也要清醒地认识到，手语和盲文方面还有许多短版需要加快弥补。例如《第二期国家手语和盲文规范化行动计划(2021-2025年)》延续了一期行动计划的一个基本判断，即我国手语和盲文的学科建设起步晚、专业人才匮乏。因此，在二期规范化行动计划的指导思想中提出：&ldquo;加快学科专业建设和人才培养，为听力和视力残疾人公平接受高质量教育、平等参与社会生活提供语言文字支持。&rdquo;同时将&ldquo;手语和盲文学科专业建设、人才培养和基础研究能力进一步增强&rdquo;作为未来五年的基本任务之一。</p>\r\n<p>　　从一期计划到二期计划一再提出手语和盲文学科专业建设问题，是我国对手语和盲文工作认识上的一个深化。手语和盲文规范化工作进行了半个多世纪，但由于各种原因，过去很长一段时间这项工作缺乏强有力的学科支撑，缺少理论的指导，不可避免地出现了走弯路的现象。正如马克思主义的基本原理所讲：脱离实践的理论是空洞的理论，而没有理论指导的实践是盲目的实践。因此，手语和盲文规范化不仅是一项工作、一项事业，同时，手语和盲文作为特殊语言文字也是一门学科，有其自己的知识体系、研究对象、研究特征、研究方法。它们需要有专门的人来学习和研究，形成自己的专业人才队伍。手语和盲文规范化工作需要有特殊语言文字的学科理论指导，特殊语言文字的学科理论也必将在规范化工作的实践中得到丰富和发展。现在我国已经到了必须尽快推动特殊语言文字学科建设，为手语和盲文规范化工作提供科学支撑的关键节点。</p>\r\n<p>　　特殊语言文字的学科建设，需要依托专业来进行，大学是主阵地。不可否认，一个新学科的形成与发展要有学术积淀的过程，既离不开政府、社会各界的支持帮助，更离不开学校的内生动力，希望能有更多的一流院校培育特殊语言文字学科，有更多的专家学者和青年学子关注和潜心于手语和盲文的语言学研究。为此，二期计划提出了两个方面的措施：一是&ldquo;支持有条件的高等院校和研究机构设立手语和盲文相关专业，与境内外高等院校和专业研究机构开展联合培养。鼓励跨学校、跨学科培养具有复合型知识结构的手语、盲文高层次专业人才。在康复大学中设立相关专业，开设手语和盲文课程，培养复合型知识和技能结构的人才。&rdquo;二是&ldquo;参照高等院校师范专业认证标准，指导现有高等院校手语翻译专业进行学科改革，全面提升培养质量。设有特殊教育师范专业的高校应配备手语和盲文专任教师。&rdquo;</p>\r\n<p>　　以上措施明确了现阶段学科建设的两个专业方向和如何建设的路径。笔者认为，手语和盲文专业人才可以更偏重于研究生层次的培养，重点为手语和盲文的本体研究，为手语翻译专业、盲文编校审校，提供高水平的理论研究人员、教师和专业技术人员。手语翻译专业则可偏重于本科层次的培养，重在为特殊教育学校、社会公共服务部门以及自主就业提供具有一定专业水准的应用性人才。</p>\r\n<p>　　值得指出的是，我国现有手语翻译专业的几所高等院校，行政隶属不同，培养层次不同，专业的上位一级学科不同，其现行专业培养方案的逻辑框架和话语体系与国家新出台的高等院校本科生培养质量监控的文件精神相距甚远，亟须相关院校参照高等院校师范专业认证标准，认真领会&ldquo;学生中心、产出导向、持续改进&rdquo;的基本理念，将专业建设的思路统一到国家有关高等院校专业建设和认证管理的大方向来。</p>\r\n<p>　　<strong>推广国家通用手语盲文 降低语言交流成本(作者：袁伟)</strong></p>\r\n<p>　　国家通用手语和国家通用盲文是听力和视力残疾人使用的特殊语言文字，是国家语言文字的重要组成部分，具有信息承载量大、传播范围广的特点。推广国家通用手语和盲文，不断加快推进其社会应用，有利于减少不同地域听力和视力残疾人交流的语言成本，有利于为听力和视力残疾人创造更广阔的社会交流空间，有利于保障听力和视力残疾人充分融入社会交往、平等参与社会生活。</p>\r\n<p>　　2021年两会期间，全国政协委员、中国残疾人艺术团团长邰丽华用国家通用手语&ldquo;演唱&rdquo;国歌，以无声的力量震撼人心。过去的五年间，规范化、统一化的国家通用手语和国家通用盲文悄然在社会公共领域推广，促进了不同地域视听残障人士的交流交往，提升了使用者的生活质量。</p>\r\n<p>　　在今年庆祝建党百年的活动中，国家通用盲文为广大视障群众学习习近平总书记&ldquo;七一&rdquo;重要讲话提供了便利，国家通用手语助力&ldquo;手语唱红歌&middot;无声传经典&rdquo;等活动的开展。包容互助、残健融合的语言文字使用氛围日渐形成。比如，宣传防疫的国家通用手语视频，联防联控机制新闻发布会加配现场国家通用手语翻译，在农村贫困盲人和聋人就业安置项目中设置国家通用盲文和手语课程，多家电视台提供国家通用手语的新闻资讯，多地司法、医疗、交通、银行、商业、旅游等公共服务部门提供国家通用手语服务，公共场所和设施标志使用国家通用盲文，等等。</p>\r\n<p>　　虽然国家通用手语和国家通用盲文社会推广取得了一些成绩，但应清晰地看到，在加快推进语言文字事业和残疾人事业高质量发展的进程中，国家通用手语和通用盲文社会推广存在着分布不平衡、总量供给不充分、质量效益不高等问题。因此，仍要坚持大力推广与质量提升并重，全面深化国家通用手语和国家通用盲文社会推广应用，不断满足广大听力和视力残疾人多元化的社会需求。</p>\r\n<p>　　法治建设是国家通用手语和盲文社会推广的保障。加快推进出台无障碍环境建设促进法，进一步明确国家通用手语和国家通用盲文社会推广的相关要求；推动修订《国家通用语言文字法》或制定《国家通用语言文字法》实施办法时，将国家通用手语和通用盲文社会推广的相关要求纳入其中；推动落实《残疾人保障法》《无障碍环境建设条例》等法律法规关于推进信息交流无障碍的相关规定。</p>\r\n<p>　　人才供给是国家通用手语和通用盲文社会推广的基础。推动建立手语翻译的职业化机制；建设志愿服务队伍，面向多个社会领域开展国家通用手语和通用盲文志愿服务，尤其是应急通用手语和盲文服务；增加可提供国家通用手语和国家通用盲文服务的社会机构和企业的资源供给，逐步满足政府部门、法院、医院、学校、企业等公共场所的特殊语言需求；为农村残疾电商人员、进城务工残疾人员等，提供国家通用手语和国家通用盲文培训服务，助力乡村振兴。</p>\r\n<p>　　重点领域是国家通用手语和通用盲文社会推广的主阵地。聚焦党和国家以及地方重大活动，增加国家通用手语翻译和国家通用盲文书面资料供给；聚焦新闻媒体，推动设区的市级以上电视台开办国家通用手语栏目(或节目)，播出的节目配备国家通用手语；聚焦新技术应用，完善国家通用手语和盲文自动翻译技术；聚焦公共服务行业，支持飞机、铁路、轮船、地铁等公共交通为听力和视力残疾人提供国家通用手语和通用盲文服务；聚焦弘扬中华优秀文化，启动国家通用盲文数字阅读推广计划，持续编写出版手语版、盲文版《中华经典读本》，建设适宜残疾人学习需求的中华优秀文化资源。</p>\r\n<p>　　<strong>全球66个国家和地区立法确认手语的语言地位并保障其使用&mdash;&mdash;</strong></p>\r\n<p>　　<strong>立法确立手语盲文的语言地位 (作者：郑璇)</strong></p>\r\n<p>　　&ldquo;法者，治之端也。&rdquo;今年发布的《第二期国家手语和盲文规范化行动计划(2021-2025年)》多处凸显了法律保障的重要性。&ldquo;十三五&rdquo;期间，我国的手语和盲文工作虽取得了不少成果，但仍存在立法薄弱等问题需要着力攻克，因此，&ldquo;手语和盲文法制建设进一步健全&rdquo;是&ldquo;十四五&rdquo;期间的主要工作目标之一。</p>\r\n<p>　　我国的手语盲文规范化工作有着坚实的法律依据，如《残疾人保障法》《国家通用语言文字法》《残疾人教育条例》《无障碍环境建设条例》等，二期计划明确提出要推动《中华人民共和国国家通用语言文字法》修订，明确听力和视力残疾人的语言权利，确立国家通用手语和国家通用盲文的法律地位，为推广和规范使用国家通用手语和国家通用盲文提供法律保障。</p>\r\n<p>　　加强手语盲文工作的法律保障，是顺应时代趋势的必然举措。来自世界聋人联合会的数据显示，全球通过立法确认手语语言地位的国家和地区一直处于持续增长态势。截至2021年8月，全球已有66个国家和地区通过立法确认了手语的语言地位并保障其使用。中国作为联合国《残疾人权利公约》的首批缔约国之一，向来高度重视手语政策与规划工作。由中国残联、国家语委发布的多个文件明确指出，手语和盲文是听力和视力残疾人使用的特殊语言文字，是国家语言文字的重要组成部分。但迄今为止，手语和盲文的语言文字地位尚未在《国家通用语言文字法》的修订中明确体现。这是下一阶段需要努力的工作方向。</p>\r\n<p>　　加强手语盲文工作的法律保障，是我国自身发展的内在要求。一方面，将特殊人群语言文字工作纳入国家语言文字工作的大框架，对于优化语言治理、增强语言能力、保护语言资源、繁荣语言生活具有重要意义。另一方面，做好国家通用手语和通用盲文工作，不仅是语言文字问题，也是政治问题，关系到广大听力和视力残疾人是否能最大限度地、无差别地参与社会事务和获取均等资源，关系到我国社会主义制度优越性能否全面、充分、深刻地彰显出来，更关系到我国国家形象的传播和文化软实力的提升。</p>\r\n<p>　　我国人口基数庞大，语言文字使用状况复杂，手语和盲文亦不例外。我们应通过多部门的有效联动和全社会的共同努力，精准发力，久久为功，共同推动我国手语和盲文实现规范化、标准化、信息化。</p>\r\n<span class=\"zdfy clearfix\">&nbsp;</span>\r\n<span class=\"box_pic\">&nbsp;</span>\r\n<span class=\"edit cf\" style=\"text-align: right;\">(责编：杨虞波罗、初梓瑞)</span>\r\n</span>\r\n','https://s2.loli.net/2023/05/27/tW7zFkvJShCIQDw.png','2023-05-30 15:50:27'),(4,NULL,'大学生献爱心，志愿服务聋哑人士救护中心','<p>近日，一群热心的大学生在社区志愿服务活动中展现了令人钦佩的爱心和奉献精神。他们前往当地的聋哑人士救护中心，以志愿者身份为这些特殊群体提供帮助和支持。这一举措既体现了大学生积极参与社会公益的精神，也展现了他们关心弱势群体的温暖心灵。</p><p>作为社区志愿服务活动的一部分，这些大学生自发组织，积极参与了为期两周的志愿者工作。他们在聋哑人士救护中心担任辅助工作，与聋哑人士建立了密切的联系，并帮助他们解决日常生活中的困难。</p><p>志愿者们的任务包括陪伴聋哑人士进行康复训练、提供情感支持，以及协助他们完成日常生活中的各种活动。他们倾听聋哑人士的心声，与他们进行交流，为他们提供友善、尊重和理解的环境。志愿者们的付出和关爱让聋哑人士感受到了社会的温暖，帮助他们重新树立起自信和勇气。</p><p style=\"text-align: center;\"><img src=\"https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/4d8c727f229e4284beb4b9c0c1da1e1e/1686493968000.jpg\" alt=\"\" data-href=\"\" style=\"width: 550.00px;height: 275.00px;\"></p><p style=\"text-align: center;\">暖心救护中心</p><p>这次志愿服务活动不仅给聋哑人士带来了帮助和关爱，也对参与其中的大学生产生了积极的影响。通过与聋哑人士的互动，志愿者们深刻体会到了沟通的重要性，以及尊重和包容不同能力的重要性。他们感受到了奉献的快乐，懂得了关爱他人的意义，进一步培养了他们的社会责任感和同理心。</p><p>聋哑人士救护中心的工作人员对这些大学生志愿者们表示由衷的感谢。他们认为志愿者们的到来为聋哑人士带来了积极的改变，并对志愿者们的无私奉献表示崇高敬意。他们希望这种志愿服务的模式能够得到更多的关注和支持，以便能够持续地帮助更多的聋哑人士。</p><p>通过这次志愿服务活动，大学生们向社会传递了爱心和关怀的正能量。他们的行动彰显了大学生积极向上、奉献社会的精神风貌。同时，这也提醒着我们，我们每个人都可以为社会做出贡献，帮助那些需要帮助的人，让我们的社会更加温暖和谐。</p><p>让我们为这些大学生志愿者们点赞，为他们的善行喝彩！愿这份爱心和奉献精神能够感染更多的人，让我们共同努力，建设一个更加美好的社会。<br></p>','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/bf272c2e62e14f66bd270f577b037e92/OIP-C.jpg','2023-06-28 10:28:55');
/*!40000 ALTER TABLE `t_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_sign_game`
--

DROP TABLE IF EXISTS `t_sign_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_sign_game` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `user_id` int unsigned DEFAULT NULL COMMENT '用户ID',
  `correct_words` varchar(255) DEFAULT NULL COMMENT '答对的单词',
  `error_words` varchar(255) DEFAULT NULL COMMENT '错误的单词',
  `created_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `t_sign_game_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户答题闯关';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_sign_game`
--

LOCK TABLES `t_sign_game` WRITE;
/*!40000 ALTER TABLE `t_sign_game` DISABLE KEYS */;
INSERT INTO `t_sign_game` VALUES (1,NULL,'23,34,56','12,24,25','2023-05-30 14:01:46'),(2,NULL,'44,52,34,21,19,24,26,27,30','10','2023-05-30 14:15:41'),(5,NULL,'18,36,21,25,50,40,49','39,20,12','2023-07-22 13:33:25'),(6,37,'38,39,32,50,19,48','13,23,37,28','2023-07-23 07:14:28');
/*!40000 ALTER TABLE `t_sign_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_user`
--

DROP TABLE IF EXISTS `t_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `phone` varchar(16) NOT NULL COMMENT '用户手机号',
  `username` varchar(128) DEFAULT NULL COMMENT '用户名',
  `password` varchar(256) NOT NULL COMMENT '用户密码(已哈希)',
  `avatar` varchar(256) DEFAULT NULL COMMENT '用户头像URL',
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user`
--

LOCK TABLES `t_user` WRITE;
/*!40000 ALTER TABLE `t_user` DISABLE KEYS */;
INSERT INTO `t_user` VALUES (1,'15294766354','周慧敏','password123','https://s2.loli.net/2022/11/05/8j6akmQ9xViINKG.jpg','2023-03-28 06:46:41'),(9,'18105022730','qbdl','likejie','https://musicstyle.oss-cn-shanghai.aliyuncs.com/images/751950dfc13d4b08adccdf81f69401ad/image.png','2023-04-28 06:02:33'),(10,'18105022780','qbdl','likejie','https://musicstyle.oss-cn-shanghai.aliyuncs.com/images/84d17769d08043e4936fc9a87a5d6371/image.png','2023-04-28 06:04:47'),(11,'18705022730','qbdl','likeiej','https://musicstyle.oss-cn-shanghai.aliyuncs.com/images/c589ef2bbe06446c87418485ae02d79b/image.png','2023-04-28 11:10:03'),(34,'15294773148','昵称','123ABCabc','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/88d6995ef62049eeab0eca6795b4d5ce/IMG_20230530141843400.jpeg','2023-05-30 06:18:45'),(36,'18105022731','qbdl','1234567890','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/9421a068bbf040798fd9a44307cd399a/IMG_20230723145041893.png','2023-07-23 06:50:48'),(37,'15123784757','CheloWood','123456','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/54865363174340578aad042dd72d506b/IMG_20230723151247529.webp','2023-07-23 07:12:56');
/*!40000 ALTER TABLE `t_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_word`
--

DROP TABLE IF EXISTS `t_word`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_word` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '词ID',
  `word` varchar(16) NOT NULL COMMENT '单词',
  `description` varchar(255) NOT NULL COMMENT '手势说明',
  `notes` varchar(255) NOT NULL COMMENT '手势动作要点说明',
  `tags` varchar(32) DEFAULT NULL,
  `img` varchar(255) NOT NULL COMMENT '手势动作说明简图url',
  `video` varchar(255) DEFAULT NULL COMMENT '手势动作动图',
  `type` varchar(16) DEFAULT NULL COMMENT '所属类别',
  PRIMARY KEY (`id`),
  KEY `word` (`word`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='单个手势词表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_word`
--

LOCK TABLES `t_word` WRITE;
/*!40000 ALTER TABLE `t_word` DISABLE KEYS */;
INSERT INTO `t_word` VALUES (9,'天津','右手食、中指直立稍分开，掌心向左，在头一侧向前微动两下。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/afb2f1f7a7fc431980ba5631d8eb7acd/天津.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/53658dd0bb2f48eca48c862ff641b34e/北京.mp4','地名'),(10,'北京','右手伸食、中指，指尖先点一下左胸部，再点一下右胸部（表示北京的简称“京”时，右手伸食、中指，指尖抵于左胸部，然后划至右胸部）。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/cf9d44ddb4a44cac931dcccc171c9657/北京.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/53658dd0bb2f48eca48c862ff641b34e/北京.mp4','地名'),(11,'上海','双手伸小指，一上一下相互勾住。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/4e4d33c06b7841668e48c2431c7ff702/上海.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/53658dd0bb2f48eca48c862ff641b34e/北京.mp4','地名'),(12,'福建','（一）一手五指张开，掌心贴胸部逆时针转动一圈。\n（二）双手斜伸，手背向斜上方，边从两侧下方向中间上方移动边指尖搭成“ ∧”形。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/7b114121f04f42999dcb77baa0bf7d76/福建.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/53658dd0bb2f48eca48c862ff641b34e/北京.mp4','地名'),(13,'河南','（一）双手侧立，掌心相对，相距窄些，向前做曲线形移动。\n（二）双手五指弯曲，食、中、无名、小指指尖朝下，手腕向下转动一下。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/f3dda2842b8f4dddac494b62f0eff385/河南.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/53658dd0bb2f48eca48c862ff641b34e/北京.mp4','地名'),(14,'爷爷（祖父）','一手打手指字母“Y”的指式，手背向外，从颏部向下移动两下。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/4f7b8a301c66464f80854c27d26a7caa/爷爷.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/2d5c302ba838417487beac2c35d05d0a/祖父.mp4','亲属称谓'),(15,'奶奶','一手打手指字母“N”的指式，在脸颊处向下划动两下。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/4d6937c8de1441198f564f07b66e1d9c/奶奶.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/14f853c8b0ce4fed9d10aca2f0c6986c/祖母.mp4','亲属称谓'),(16,'外婆','（一）左手横立；右手伸食指，指尖朝下，在左手背外向下指。\n（二）一手五指微曲，指尖抵于脑后，向前点动一下，仿发髻的形状。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/81f83db3ebd84375875b7397b172b244/外婆.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/14f853c8b0ce4fed9d10aca2f0c6986c/祖母.mp4','亲属称谓'),(17,'父亲（爸爸）','右手伸拇指，指尖左侧贴在嘴唇上。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/3943aa0879994954a2883b85d16b43f9/父亲.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/7c603758065548548ace1431d8c58368/父亲.mp4','亲属称谓'),(18,'母亲（妈妈）','右手食指直立，指尖左侧贴在嘴唇上；也用于表示生物中母、雌的概念。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/eb5358d445714c3e920d011bb6401c25/母亲.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/729366d19659445abd3ef792670db3d1/妈妈.mp4','亲属称谓'),(19,'共产党','双手食、中指搭成“共”字形，手背向上，右手向下碰三下左手；专用于表示共产党。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/8fa0c687b9634283902a596913af8757/共产党.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/2d1fd05bd92a42dd80031bbd61d8198e/领导.mp4','政党'),(20,'九三学社','（一）一手食指弯曲，中节指指背向上，虎口朝内。\n（二）一手中、无名、小指直立分开，掌心向外。\n（三）一手五指撮合，指尖朝内，按向前额。\n（四）左手五指撮合，指尖朝上；右手伸食指，指尖朝下，绕左手转动一圈。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/4421c84839da4c03840003b33dd493bf/九三学社.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/c1e6432fcd58402ba9de8ef1ce76c19d/顺从.mp4','政党'),(21,'民主党派','（一）左手食指与右手拇、食指搭成“民”字的一部分。\n（二）一手伸拇指，贴于胸部。\n（三）一手打手指字母“D”的指式。\n（四）一手五指张开，指尖朝上，然后撮合。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/14c451da9ec04e48a25c6f42fafe41d6/民主党派.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/c1e6432fcd58402ba9de8ef1ce76c19d/顺从.mp4','政党'),(22,'立春','（一）左手横伸；右手食、中指分开，指尖朝下，立于左手掌心上。\n（二）左手握拳，手背向上；右手食指点一下左手食指根部关节。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/d936539b02864bfaa1a8675d02a2a70e/立春.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/22e53a8181504cca8ba792b5dc0ba8fa/雨天.mp4','节气'),(23,'雨水','（一）双手五指微曲，指尖朝下，在头前快速向下动几下，表示雨点落下。\n（二）一手伸食指，指尖贴于下嘴唇。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/ed3be4d9623d4a6eb818d97ee0ae14fa/雨水.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/22e53a8181504cca8ba792b5dc0ba8fa/雨天.mp4','节气'),(24,'惊蛰','（一）双手拇、食指相捏，置于眼角处，然后突然张开，眼同时睁大，面露吃惊的表情。\n（二）左手横伸，掌心向下；右手伸食指，边弯动边从左手掌心下移至左手背上，表示休眠的小虫惊蛰后复苏。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/2a41dc922b2148e0a88758f2ab2eca0f/惊蛰.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/22e53a8181504cca8ba792b5dc0ba8fa/雨天.mp4','节气'),(25,'寒露','（一）双手握拳屈肘，小臂颤动几下，如哆嗦状，表示冷。\n（二）左手横伸；右手拇、食指捏成圆形，置于左手掌心上，微晃几下。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/3559ae8aaa6147f989c38a60da6cbd2b/寒露.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/22e53a8181504cca8ba792b5dc0ba8fa/雨天.mp4','节气'),(26,'白族','（一）一手五指弯曲，掌心向外，指尖弯动两下。\n（二）一手五指张开，指尖朝上，然后撮合。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/a90a952f0af646ea83957a7588d0c7df/白族.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/cbe90496fe474220b2896536772f4741/民族.mp4','民族'),(27,'布依族','（一）双手五指并拢，掌心向内，交叉相搭，贴于前额，然后向两侧移动再折而向后移动，掌心相对，仿布依族头饰。\n（二）一手五指张开，指尖朝上，然后撮合。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/14828c8ad80c4a1c82a79941c0dfc483/布依族.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/cbe90496fe474220b2896536772f4741/民族.mp4','民族'),(28,'傣族','（一）双手五指并拢，掌心向内，交叉相搭，贴于前额，然后向两侧移动再折而向后移动，掌心相对，仿布依族头饰。\n（二）一手五指张开，指尖朝上，然后撮合。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/f16f277ebebb4e608b1b5e505670e472/傣族.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/cbe90496fe474220b2896536772f4741/民族.mp4','民族'),(29,'自行车','双手握拳，手背向上，在胸前前后交替转动两下，如骑自行车状。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/bf64df62b8f74635ba9a0c283009a0d9/自行车.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/fef557e6c2b24c698241c3645c4ea204/自行车.mp4','交通工具'),(30,'飞机','一手伸拇、食、小指，手背向上，从低向高移动，如飞机起飞状。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/2a9ab0fd1cbe4bfd834335c8858444d1/飞机.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/e2a29a98030a4b799eb6368e1e32db9e/飞机.mp4','交通工具'),(31,'猫','双手拇、食指相捏，其他三指横伸，指尖相对，手背向外，在嘴边分别向两侧横划一下，仿猫的胡须。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/266ad81f660a4b0989dffa22d1c33995/猫.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/c4a1e2aacb3344a1b72c4cfbcfdcd839/猫.mp4','动植物'),(32,'狗','左手五指撮合成尖形，指尖朝前；右手食、中指分开，指尖朝上，置于左手背上，仿狗的头部外形。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/7755c70c1df74e1192199fba1f812365/狗.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/43ab1c8bfe434bf2abb9108c1b6b26ef/狗.mp4','动植物'),(33,'骆驼','双手手背拱起，一前一后，同时向前移动两下，表示骆驼上的驼峰。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/eb78f208a9864417aba58a5d952b97e7/骆驼.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/40803fa26a4546ac891e56b81485c71c/骆驼.mp4','动植物'),(34,'鹰','一手食指弯曲如钩，指尖朝内，手背向上，手腕置于嘴部，表示鹰的喙。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/dd84c66f93be4cc2913175539e44c868/鹰.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/e6f33e7617674f759b10778efa5f462d/鹰.mp4','动植物'),(35,'雨','双手五指微曲，指尖朝下，在头前快速向下动几下，表示雨点落下。（可根据实际决定动作的力度）','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/5f6f4ad8b225425c97ffa5f11fb351d0/雨.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/87fdedc37c124a1ba5121c21c21d17a7/雨.mp4','天气'),(36,'太阳','双手拇、食指搭成圆形，虎口朝内，从头右侧向头顶做弧形移动，表示太阳升起。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/a3b321c2fa3b4d2ca774fa151c09e6b2/太阳.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/dade4fc8fc9e489abda1072ad30d84b5/太阳.mp4','天气'),(37,'云','一手（或双手）五指成“コ”形，虎口朝内，在头前上方平行转动两下。','无','常用词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/4815f8fc848a453d8e58d8c684aa75fb/云.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/e113ac68d3e24e8a83d50712002d825e/云.mp4','天气'),(38,'再见','一手上举，掌心向外，左右摆动几下，面带笑容。（可根据实际表示再见的动作）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/4a3526e0f92341c6aef3d95fc0533fca/再见.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/680b0c1463af4981bdf42b1913cf8b36/再见.mp4','常用词'),(39,'感谢','一手（或双手）伸拇指，向前弯动两下，面带笑容。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/237c5a111c434c2cbdfb3326d6307017/感谢.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/06201bd263ea45be8e2576a1f035fb5d/感谢.mp4','常用词'),(40,'你','一手伸食指，手背向上（或一手平伸，掌心向上），指向对方。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/876c1e187afc4032a7479652e3ebb0fe/你.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/f954ec15dda84df1b320d0b582663d45/你.mp4','代词'),(41,'我','一手伸食指，指一下自己（或一手手掌拍一下胸部）。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/53967a5f9e634890b899bc88dc013d6b/我.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/6c0e7c89e19a4491bd8c46806d3785ae/我.mp4','代词'),(42,'他','一手伸食指（或一手斜伸，掌心向上），指向侧方第三者。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/80f8b8a3484c46beada8a20c77dcee35/他.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/9175af73e04140d4a9bd842d03f52ed3/他.mp4','代词'),(43,'你们','（一）一手伸食指，手背向上（或一手平伸，掌心向上），指向对方。（二）一手横伸，掌心向下，顺时针平行转动半圈，眼睛同时看向对方。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/f0ca423f886e4fcd99122ff72aff4421/你们.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/b9d90a3f31c343cfb84176cc57c196e8/你们的.mp4','代词'),(44,'他们','（一）一手伸食指（或一手斜伸，掌心向上），指向侧方第三者。（二）一手五指并拢，掌心向下，在身体一侧顺时针平行转动半圈。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/9b6cbe0b10ff4b33ac89d3a3a3dc0be1/他们.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/ff3a81ff3a7c4191a80f12aa7c2e6433/他们.mp4','代词'),(45,'看','一手食、中指分开，指尖朝前，手背向上，从眼部向前一指。（可根据实际表示看的动作）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/899d0c81ccae4d6fad58cde12a2248c5/看.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/b95dce16540b41f7949e8d01a9aa18fe/看.mp4','动词'),(46,'走','一手食、中指分开，指尖朝下，交替向前移动。（可根据实际表示走的动作）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/6cdd7e81f741449a9c14559a586ebdb6/走.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/475b5bf8503c43bb81c1a91c57043e80/走.mp4','动词'),(47,'跑','双手握拳屈肘，前后交替摆动两下，如跑步状。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/8aff77e9eb4042269f99fcb704e5e2a9/跑.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/9a6435fd394845058d1e300bef78cd77/奔跑.mp4','动词'),(48,'跳','左手横伸；右手食、中指微曲，先立于左手掌心上，然后迅速向上弹起。（可根据实际表示跳的动作）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/b6ef80e4da164e84a94b28a1f79113bc/跳.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/5166677e2466496cb418be24c6a39a76/跳.mp4','动词'),(49,'吃','一手伸食、中指，向嘴边拨动一（或两）下，如用筷子吃饭状。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/4c3c186d13ac43c39861f4cd574b4e59/吃.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/12238a558d1e4f92897ab804e258f04e/吃.mp4','动词'),(50,'喝','一手五指成半圆形，如拿杯子状，模仿喝水的动作。（可根据实际表示喝的动作）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/c5420b0539304cbcbef44383a4812413/喝.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/b85c577233674da2b78c366775f8099a/喝.mp4','动词'),(51,'拍','一手平伸，掌心向下，向下拍动两下。（可根据实际表示拍的动作）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/ddb5db57f9d741efab2a0387729e9c76/拍.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/d2a22f4e727a4d43b19747e6f7616fc5/敲打.mp4','动词'),(52,'打','一手握拳，向前下方挥动一下。（可根据实际表示打的动作）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/0f50936fef214c42abfbeacf78078060/打.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/f7a987c66bda408e9176ab0a286b62d2/打.mp4','动词'),(53,'好','一手伸拇指，面露赞赏的表情。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/a4ea8ce2b0834884805fce36c85b67b9/好.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/d538b883ee5647e597581e4a0b1b7627/好.mp4','形容词'),(54,'少','一手拇、食指相捏，拇指尖微弹一下。（可根据实际表示少的状态）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/c702c0603fb0486e9056c79d2133a256/少.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/839e39b60cfe4d29807eb6eca173934e/少许.mp4','形容词'),(55,'大','双手侧立，掌心相对，同时向两侧移动，幅度要大些。（可根据实际表示大的状态）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/323acb7e151449d793594bd7f8e938d2/大.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/c1c0a1b358fd44fc9fc2cd491518fd42/大.mp4','形容词'),(56,'小','一手拇、小指相捏，指尖朝上。（可根据实际表示小的状态）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/951c3c446c56474f8a14f6b14fc34612/小.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/99ec40d35e9a4c8fa3ddb8dc37adf425/小.mp4','形容词'),(57,'漂亮','一手伸拇、食、中指，食、中指并拢，先置于鼻部，然后边向外移动边缩回食、中指。','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/d1757f347e6a4b07a65f45e70d5a4b66/漂亮.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/656b26480eac4d83aa6daa1a61e85760/漂亮的.mp4','形容词'),(58,'远','一手拇指尖按于食指根部，食指尖朝前，手背向下，向前上方移动。（可根据实际表示远的状态）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/98fa1eec0c76410b86a2919366593be6/远.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/fe1d01fe63aa478d807a0c04f1821376/远的.mp4','形容词'),(59,'近(附近、临近、濒临)','双手拇、食指相捏，虎口朝上，相互靠近。（可根据实际表示近的状态）','无','常用300词','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/63801b7c88b34a91ad761a8f2d9e1258/近.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/27678f72d0b54359b3681c9775286506/最近的.mp4','形容词'),(60,'测试','测试说明','测试说明','测试说明','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/70e7b0df0410415f8e185b7ace8c9924/OIP-C.jpg','https://musicstyle.oss-cn-shanghai.aliyuncs.com/files/8a96953d0a4b4d649cfd2ca2979fdbb8/video-min-memery.mp4','其它');
/*!40000 ALTER TABLE `t_word` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_word_freq`
--

DROP TABLE IF EXISTS `t_word_freq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_word_freq` (
  `word_id` int unsigned NOT NULL COMMENT '单词ID',
  `count` int unsigned NOT NULL COMMENT '操作次数',
  PRIMARY KEY (`word_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='单词点击频率';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_word_freq`
--

LOCK TABLES `t_word_freq` WRITE;
/*!40000 ALTER TABLE `t_word_freq` DISABLE KEYS */;
INSERT INTO `t_word_freq` VALUES (9,5),(10,2),(11,1),(12,4),(13,1),(20,4),(21,4),(22,5),(23,4),(24,2),(28,1),(32,4),(40,1),(45,7),(48,2);
/*!40000 ALTER TABLE `t_word_freq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_word_love`
--

DROP TABLE IF EXISTS `t_word_love`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_word_love` (
  `word_id` int unsigned NOT NULL COMMENT '单词ID',
  `user_id` int unsigned NOT NULL COMMENT '用户ID',
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  KEY `word_id` (`word_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `t_word_love_ibfk_1` FOREIGN KEY (`word_id`) REFERENCES `t_word` (`id`),
  CONSTRAINT `t_word_love_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `t_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户收藏的单词';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_word_love`
--

LOCK TABLES `t_word_love` WRITE;
/*!40000 ALTER TABLE `t_word_love` DISABLE KEYS */;
INSERT INTO `t_word_love` VALUES (10,1,'2023-04-05 03:17:36'),(11,1,'2023-04-05 13:05:29'),(12,1,'2023-04-05 13:18:40'),(10,1,'2023-04-05 13:31:42'),(29,34,'2023-05-30 06:26:58');
/*!40000 ALTER TABLE `t_word_love` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-28 10:39:31
