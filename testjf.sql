/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : localhost:3306
 Source Schema         : testjf

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 25/07/2022 18:17:18
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for inquire
-- ----------------------------
DROP TABLE IF EXISTS `inquire`;
CREATE TABLE `inquire`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sentence` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `hr` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of inquire
-- ----------------------------
INSERT INTO `inquire` VALUES (1, '通过工号查询指定积分数据', 'select fullDeptName from sys_department where deptId in (select su.deptId from sys_user su where su.empNo =%s)', 0);
INSERT INTO `inquire` VALUES (2, '通过职务查询员工', 'select n.empNo from (sys_title su left join sys_duty m on su.titleId=m.titleId) left join sys_user n on m.dutyId=n.dutyId where su.titleName in (%s) and n.useStatus=0', 0);
INSERT INTO `inquire` VALUES (3, '查询个人部门积分的数据', 'select created_time,apply_item_id,apply_integral*apply_num,dept_id from tb_integral where informant_id =%s and dimension_id=%s order by created_time desc', 0);
INSERT INTO `inquire` VALUES (4, '查询个人某维度总积分', 'select sum(apply_integral*apply_num) from tb_integral where informant_id =%s and dimension_id =%s', 0);
INSERT INTO `inquire` VALUES (5, '通过工号查询指定积分数据', 'select dept_id,apply_integral,created_time from tb_integral where apply_item_id=%s and informant_id=%s', 0);
INSERT INTO `inquire` VALUES (6, '查询所属部门全称', 'select fullDeptName from sys_department where deptId in (select su.deptId from sys_user su where su.empNo=%s)', 1);
INSERT INTO `inquire` VALUES (7, '通过岗位查询所属部门', 'select fullDeptName from sys_department where deptId in (select su.deptId from sys_duty su where su.dutyName in (%s))', 0);
INSERT INTO `inquire` VALUES (8, '通过岗位ID查询所属部门', 'select fullDeptName from sys_department where deptid=%s ', 0);
INSERT INTO `inquire` VALUES (9, '查询部门总人数', 'select count(*) from sys_user su left join sys_department m on m.deptId=su.deptId where m.fullDeptName LIKE (\'%%%s%%\')', 0);
INSERT INTO `inquire` VALUES (10, '查询部门ID', 'select deptId from sys_user where empNo=%s', 0);
INSERT INTO `inquire` VALUES (11, '查询用户名字', 'select empName from sys_user where empNo=%s', 0);
INSERT INTO `inquire` VALUES (12, '查询岗位ID', 'select dutyId from sys_user where empNo=%s', 0);
INSERT INTO `inquire` VALUES (13, '岗位名称查询岗位ID', 'select dutyId from sys_duty where dutyName in (%s)', 0);
INSERT INTO `inquire` VALUES (14, '岗位名称查询级别', 'select title.dutyLevel from sys_duty duty left join sys_title title on title.titleId=duty.titleId where duty.dutyName in (%s)', 0);
INSERT INTO `inquire` VALUES (15, '入职年限查询，不满一年计算为0', 'select emp.hireDate from emp_employeefile emp left join sys_user us on emp.empId=us.empId where us.empNo=%s', 1);
INSERT INTO `inquire` VALUES (16, '岗位ID查询工号', 'select empNo from sys_user where dutyId=%s', 0);
INSERT INTO `inquire` VALUES (17, '兼职表岗位ID查询工号', 'select empNo from sys_user where empId=(select su.empId from emp_parttimeduty su where su.dutyId=%s)', 0);
INSERT INTO `inquire` VALUES (18, '查询上级领导的岗位ID', 'select parentid from sys_duty where dutyId in (select u.dutyId from sys_user u where u.empno =%s) ', 1);
INSERT INTO `inquire` VALUES (19, '通过类别名称及分值查询填报积分项的apply_item_id', 'select id from tb_points_project where category in (%s) and points in (%s) and is_delete=0', 0);
INSERT INTO `inquire` VALUES (20, '通过类别名称查询填报积分项的apply_item_id ', 'select id from tb_points_project where category in (%s) and is_delete=0', 0);
INSERT INTO `inquire` VALUES (21, '通过填报积分项标准查询apply_item_id ', 'select id from tb_points_project where standard in (%s) and is_delete=0', 0);
INSERT INTO `inquire` VALUES (22, '根据工作标准查询填报项 ', 'select points,unit,dimension_id,id from tb_points_project where standard in (%s) and is_delete=0', 0);
INSERT INTO `inquire` VALUES (23, '查询审批编号', 'select approval_id from tb_integral where informant_id=%s and status=1 and remark in (%s)', 0);
INSERT INTO `inquire` VALUES (25, '查询积分员', 'select emp_no from tb_integral_manager  where depart_id=%s', 0);
INSERT INTO `inquire` VALUES (26, '查询职务id', 'select titleId from sys_duty where dutyid=(select u.dutyid from sys_user u where u.empNo=%s )', 0);
INSERT INTO `inquire` VALUES (27, '职务id查询级别', 'select dutyLevel from sys_title where titleId=%s', 0);
INSERT INTO `inquire` VALUES (28, '查询部门信息', 'select deptLevel,fullDeptName,deptId from sys_department where deptId in (select su.deptId from sys_user su where su.empNo=%s)', 1);
INSERT INTO `inquire` VALUES (29, '通过部门全称查询部门ID', 'select deptid from sys_department where fullDeptName in (%s)', 1);

-- ----------------------------
-- Table structure for interface
-- ----------------------------
DROP TABLE IF EXISTS `interface`;
CREATE TABLE `interface`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `api` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Post` int(0) NULL DEFAULT NULL,
  `code` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of interface
-- ----------------------------
INSERT INTO `interface` VALUES (1, 'token', 'http://oauth.jtyjy.com/api/oneLogin/sso?serverId=29&empno=%s&pwd=123456', 0, 0);
INSERT INTO `interface` VALUES (2, '填报积分', 'http://testjf.jtyjy.com/api/integral/save/%s?%s', 1, 1);
INSERT INTO `interface` VALUES (3, '审核积分提报', 'http://testjf.jtyjy.com/api/integral/audit/%s?%s', 1, 1);
INSERT INTO `interface` VALUES (4, '新建积分任务', 'http://testjf.jtyjy.com/api/integralTask/addTask?%s', 1, 0);

SET FOREIGN_KEY_CHECKS = 1;
