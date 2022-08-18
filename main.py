{
    "code": 0,
    "msg": "请求成功",
    "data": [
        {
            "name": "产值积分",
            "value": "1-2",
            "parentId": "0--1",
            "points": 0,
            "processId": null,
            "unit": null,
            "projectId": null,
            "childProjectTree": [
                {
                    "name": "1",
                    "value": "2-864",
                    "parentId": "1-2",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "1",
                            "value": "3-865",
                            "parentId": "2-864",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "1",
                                    "value": "4-1519",
                                    "parentId": "3-865",
                                    "points": 1.0000,
                                    "processId": "5",
                                    "unit": "学时",
                                    "projectId": 1519,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "test",
                    "value": "2-2331",
                    "parentId": "1-2",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "test",
                            "value": "3-2346",
                            "parentId": "2-2331",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "test1",
                                    "value": "4-2443",
                                    "parentId": "3-2346",
                                    "points": 1.0000,
                                    "processId": "5",
                                    "unit": "小时",
                                    "projectId": 2443,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "公共积分",
            "value": "1-3",
            "parentId": "0--1",
            "points": 0,
            "processId": null,
            "unit": null,
            "projectId": null,
            "childProjectTree": [
                {
                    "name": "出勤规范",
                    "value": "2-503",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "常规缺勤扣分",
                            "value": "3-911",
                            "parentId": "2-503",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "每缺勤1小时减13分，不足1小时的按1小时计算",
                                    "value": "4-1530",
                                    "parentId": "3-911",
                                    "points": 13.0000,
                                    "processId": "5",
                                    "unit": "小时",
                                    "projectId": 1530,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "无效率出勤",
                            "value": "3-913",
                            "parentId": "2-503",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "无效率出勤每1小时减13分，不足1小时的按1小时计算",
                                    "value": "4-1531",
                                    "parentId": "3-913",
                                    "points": 13.0000,
                                    "processId": "5",
                                    "unit": "小时",
                                    "projectId": 1531,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "迟到、早退",
                            "value": "3-915",
                            "parentId": "2-503",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "工作日出勤，以每月考勤数据为准",
                                    "value": "4-1532",
                                    "parentId": "3-915",
                                    "points": 10.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1532,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "旷工",
                            "value": "3-917",
                            "parentId": "2-503",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "无故不来上班",
                                    "value": "4-1533",
                                    "parentId": "3-917",
                                    "points": 300.0000,
                                    "processId": "5",
                                    "unit": "天",
                                    "projectId": 1533,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "周末出勤",
                            "value": "3-992",
                            "parentId": "2-503",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "周末没出勤一小时15分，每天150分封顶",
                                    "value": "4-1587",
                                    "parentId": "3-992",
                                    "points": 15.0000,
                                    "processId": "5",
                                    "unit": "小时",
                                    "projectId": 1587,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "公司层面培训/会议",
                            "value": "3-2310",
                            "parentId": "2-503",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "迟到、早退",
                                    "value": "4-2416",
                                    "parentId": "3-2310",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 2416,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "逾期请假",
                                    "value": "4-2417",
                                    "parentId": "3-2310",
                                    "points": 30.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 2417,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "异常出勤",
                                    "value": "4-2418",
                                    "parentId": "3-2310",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 2418,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "其他",
                    "value": "2-525",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "外部投诉",
                            "value": "3-985",
                            "parentId": "2-525",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "一般投诉",
                                    "value": "4-1582",
                                    "parentId": "3-985",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1582,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "严重投诉",
                                    "value": "4-1583",
                                    "parentId": "3-985",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1583,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "客户投诉",
                                    "value": "4-1584",
                                    "parentId": "3-985",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1584,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "员工出勤",
                    "value": "2-783",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "年假",
                            "value": "3-900",
                            "parentId": "2-783",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "年假未休完，奖励100分/天",
                                    "value": "4-1520",
                                    "parentId": "3-900",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "天",
                                    "projectId": 1520,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "职业素养",
                    "value": "2-839",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "职业素养",
                            "value": "3-840",
                            "parentId": "2-839",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "女士带妆上班：底妆、眉毛、口红缺一不可",
                                    "value": "4-1521",
                                    "parentId": "3-840",
                                    "points": 3.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1521,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "女士带妆上班：底妆、眼影、眉毛、口红缺一不可",
                                    "value": "4-1522",
                                    "parentId": "3-840",
                                    "points": 5.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1522,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "男士仪容仪表：面部清洁，无胡渣；发型干净整洁，不过长或过短，前不遮眉，侧不及耳，后不长过衣领",
                                    "value": "4-1523",
                                    "parentId": "3-840",
                                    "points": 3.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1523,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "男士着装：着装正式、职业，穿商务皮鞋；衣服无褶皱、鞋面干净",
                                    "value": "4-1524",
                                    "parentId": "3-840",
                                    "points": 5.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1524,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "及时处理意外事件或重大事故，使公司免遭损害",
                                    "value": "4-1525",
                                    "parentId": "3-840",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1525,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "对于有危害公司权益的事情，能事先揭发、制止",
                                    "value": "4-1526",
                                    "parentId": "3-840",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1526,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "提供显著提升公司经营业绩的重要管理办法",
                                    "value": "4-1527",
                                    "parentId": "3-840",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1527,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "社会公德",
                    "value": "2-849",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "助人为乐",
                            "value": "3-852",
                            "parentId": "2-849",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "对不法行为挺身而出，见义勇为等",
                                    "value": "4-1529",
                                    "parentId": "3-852",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1529,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "拾金不昧",
                            "value": "3-909",
                            "parentId": "2-849",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "捡到金钱财物等贵重物品及时归还",
                                    "value": "4-1528",
                                    "parentId": "3-909",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1528,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "1",
                    "value": "2-860",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "1",
                            "value": "3-861",
                            "parentId": "2-860",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "1",
                                    "value": "4-1506",
                                    "parentId": "3-861",
                                    "points": 1.0000,
                                    "processId": "5",
                                    "unit": "条",
                                    "projectId": 1506,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "13",
                    "value": "2-867",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "12",
                            "value": "3-882",
                            "parentId": "2-867",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "21",
                                    "value": "4-1513",
                                    "parentId": "3-882",
                                    "points": 12.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1513,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "fdaf",
                    "value": "2-873",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "fsaf",
                            "value": "3-874",
                            "parentId": "2-873",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "fas",
                                    "value": "4-1511",
                                    "parentId": "3-874",
                                    "points": 112.0000,
                                    "processId": "5",
                                    "unit": "项",
                                    "projectId": 1511,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "123",
                    "value": "2-876",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "123",
                            "value": "3-877",
                            "parentId": "2-876",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "123",
                                    "value": "4-1512",
                                    "parentId": "3-877",
                                    "points": 123.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1512,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "行政规范",
                    "value": "2-919",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "着装礼仪",
                            "value": "3-920",
                            "parentId": "2-919",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "穿拖鞋/背心/睡衣/裤衩等进入园区",
                                    "value": "4-1534",
                                    "parentId": "3-920",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1534,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "1.穿拖鞋、背心、睡衣、裤衩等进入园区\n2.参加大型会议、活动等未按要求着装\n3.出现以上之一行为的，按此标准执行",
                                    "value": "4-2419",
                                    "parentId": "3-920",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 2419,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "行为规范",
                            "value": "3-922",
                            "parentId": "2-919",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "随地吐痰、乱丢垃圾、乱扔烟头、乱倒茶渣、非吸烟区吸烟、破坏园区花草树木景观及设施设备等公物、乱涂乱画、乱粘贴条幅海报等物品、说脏话、大声喧哗等不文明行为",
                                    "value": "4-1535",
                                    "parentId": "3-922",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1535,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "员工家属及小孩在公司物流通道、办公区域、危险区域（假山、水塘、带电区域等）逗留玩耍，翻越围墙、划车等",
                                    "value": "4-1536",
                                    "parentId": "3-922",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1536,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "不使用会议室未及时取消",
                                    "value": "4-1537",
                                    "parentId": "3-922",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1537,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "车辆管理",
                            "value": "3-926",
                            "parentId": "2-919",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "非停车区域内乱停乱放，停放在人行道、道路拐角、出入口、消防通道、物流通道等位置",
                                    "value": "4-1538",
                                    "parentId": "3-926",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1538,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "园区超速行驶（≥15km/h）",
                                    "value": "4-1539",
                                    "parentId": "3-926",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1539,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "园区开车未礼让行人、在园区抢道/别车/逆行等危险驾驶行为",
                                    "value": "4-1540",
                                    "parentId": "3-926",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1540,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "用餐规范",
                            "value": "3-930",
                            "parentId": "2-919",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "在办公楼内就餐/携带或食用味道大的食物等",
                                    "value": "4-1541",
                                    "parentId": "3-930",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1541,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "未按要求清理用餐桌面、食堂用餐插队、霸占座位",
                                    "value": "4-1542",
                                    "parentId": "3-930",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1542,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "不遵守公司用餐时间规定，提前用餐",
                                    "value": "4-1543",
                                    "parentId": "3-930",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1543,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "宿舍规范",
                            "value": "3-934",
                            "parentId": "2-919",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "衣服晾晒在公共区域",
                                    "value": "4-1544",
                                    "parentId": "3-934",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1544,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "带宠物进入宿舍",
                                    "value": "4-1545",
                                    "parentId": "3-934",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1545,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "卫生检查不合格，办公区域所有人员扣分",
                                    "value": "4-1546",
                                    "parentId": "3-934",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1546,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "宿舍门口、走廊处堆放私人物品",
                                    "value": "4-1547",
                                    "parentId": "3-934",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1547,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "未经允许私自带外部人员入住公司宿舍",
                                    "value": "4-1548",
                                    "parentId": "3-934",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1548,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "私自调换房间及其房间内设施",
                                    "value": "4-1549",
                                    "parentId": "3-934",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1549,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "其他违反宿舍管理制度行为",
                                    "value": "4-1550",
                                    "parentId": "3-934",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1550,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "洗手间规范",
                            "value": "3-942",
                            "parentId": "2-919",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "踩马桶上上厕所/如厕后不冲洗/洗手间内吸烟/卫生间茶渣乱倒",
                                    "value": "4-1551",
                                    "parentId": "3-942",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1551,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "如厕期间玩手机，影响他人使用",
                                    "value": "4-1552",
                                    "parentId": "3-942",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1552,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "将卫生间护手霜等物品带走作为私人物品",
                                    "value": "4-1553",
                                    "parentId": "3-942",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1553,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "办公区域",
                            "value": "3-946",
                            "parentId": "2-919",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "下班未关电脑/灯/空调/打印机等设备,公共区域扣办公室负责人积分",
                                    "value": "4-1554",
                                    "parentId": "3-946",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1554,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "使用大功率电器、私搭电线，造成事故的公司保留追责权利,公共区域扣办公室负责人积分",
                                    "value": "4-1555",
                                    "parentId": "3-946",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1555,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "卫生检查不合格，办公区域所有人员扣分",
                                    "value": "4-1556",
                                    "parentId": "3-946",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1556,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "处罚管理",
                    "value": "2-950",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "通报批评",
                            "value": "3-951",
                            "parentId": "2-950",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "通报当事人",
                                    "value": "4-1557",
                                    "parentId": "3-951",
                                    "points": 300.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1557,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "通报当事人直属上级和部门经理分别负连带责任",
                                    "value": "4-1558",
                                    "parentId": "3-951",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "人",
                                    "projectId": 1558,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "行政处分",
                            "value": "3-954",
                            "parentId": "2-950",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "警告当事人",
                                    "value": "4-1559",
                                    "parentId": "3-954",
                                    "points": 500.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1559,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "警告当事人直属上级和部门经理分别负连带责任",
                                    "value": "4-1560",
                                    "parentId": "3-954",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "人",
                                    "projectId": 1560,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "记过当事人",
                                    "value": "4-1561",
                                    "parentId": "3-954",
                                    "points": 1000.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1561,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "记过当事人直属上级和部门经理分别负连带责任",
                                    "value": "4-1562",
                                    "parentId": "3-954",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "人",
                                    "projectId": 1562,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "记大过当事人",
                                    "value": "4-1563",
                                    "parentId": "3-954",
                                    "points": 5000.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1563,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "记大过当事人直属上级和部门经理分别负连带责任",
                                    "value": "4-1564",
                                    "parentId": "3-954",
                                    "points": 500.0000,
                                    "processId": "5",
                                    "unit": "人",
                                    "projectId": 1564,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "降级当事人",
                                    "value": "4-1565",
                                    "parentId": "3-954",
                                    "points": 8000.0000,
                                    "processId": "5",
                                    "unit": "人",
                                    "projectId": 1565,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "职业规范",
                    "value": "2-962",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "人员稳定",
                            "value": "3-963",
                            "parentId": "2-962",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "年度在职流失率20%-30%，部门经理减分",
                                    "value": "4-1566",
                                    "parentId": "3-963",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1566,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "年度在职流失率30%以上，部门经理减分",
                                    "value": "4-1567",
                                    "parentId": "3-963",
                                    "points": 300.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1567,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "文件管理",
                            "value": "3-966",
                            "parentId": "2-962",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "未及时接收、传达公文、资料的每次扣20分",
                                    "value": "4-1568",
                                    "parentId": "3-966",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1568,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "上班期间行为规范",
                            "value": "3-968",
                            "parentId": "2-962",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "工作时间串岗、闲聊",
                                    "value": "4-1569",
                                    "parentId": "3-968",
                                    "points": 20.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1569,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "工作时间聚众打牌、酗酒的",
                                    "value": "4-1570",
                                    "parentId": "3-968",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1570,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "上班时间上网聊天/看电影/打游戏/睡觉/下载/浏览/安装与工作无关的内容;利用公司网络群发与工作无关邮件的、脱岗等",
                                    "value": "4-1571",
                                    "parentId": "3-968",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1571,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "利用工作时间,擅自兼职的",
                                    "value": "4-1572",
                                    "parentId": "3-968",
                                    "points": 500.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1572,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "工作态度",
                            "value": "3-973",
                            "parentId": "2-962",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "工作态度粗暴，搬弄是非、使用辱骂性的语言伤他人等影响工作秩序的行为",
                                    "value": "4-1573",
                                    "parentId": "3-973",
                                    "points": 500.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1573,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "顶撞上级、不服从管理",
                                    "value": "4-1574",
                                    "parentId": "3-973",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1574,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "职业品德",
                            "value": "3-976",
                            "parentId": "2-962",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "歪曲事实、恶意诋毁公司领导和同事",
                                    "value": "4-1575",
                                    "parentId": "3-976",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1575,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "弄虚作假行为：伪造病休证明、积分提报等",
                                    "value": "4-1576",
                                    "parentId": "3-976",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1576,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "对下属正常申诉打击报复经查属实的",
                                    "value": "4-1577",
                                    "parentId": "3-976",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1577,
                                    "childProjectTree": []
                                }
                            ]
                        },
                        {
                            "name": "违纪行为",
                            "value": "3-980",
                            "parentId": "2-962",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "能够预防的事故不积极采取措施",
                                    "value": "4-1578",
                                    "parentId": "3-980",
                                    "points": 500.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1578,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "携带易燃、易爆、危险品进入仓库但尚未给公司造成损失",
                                    "value": "4-1579",
                                    "parentId": "3-980",
                                    "points": 1000.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1579,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "违反部门工作流程给工作造成损失",
                                    "value": "4-1580",
                                    "parentId": "3-980",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1580,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "泄漏公司机密或捏造谣言或酿成意外灾害，致使公司蒙受损失的",
                                    "value": "4-1581",
                                    "parentId": "3-980",
                                    "points": 2000.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1581,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "荣誉嘉奖",
                    "value": "2-997",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "荣誉嘉奖",
                            "value": "3-998",
                            "parentId": "2-997",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "荣获研究院质量与创新类嘉奖",
                                    "value": "4-1589",
                                    "parentId": "3-998",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "项",
                                    "projectId": 1589,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "荣获研究院嘉奖",
                                    "value": "4-1590",
                                    "parentId": "3-998",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1590,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "荣获部门嘉奖",
                                    "value": "4-1591",
                                    "parentId": "3-998",
                                    "points": 30.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1591,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "荣获研究院质量与创新类嘉奖",
                                    "value": "4-2025",
                                    "parentId": "3-998",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 2025,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "技能大赛",
                    "value": "2-1002",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "技能大赛",
                            "value": "3-1003",
                            "parentId": "2-1002",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "韬奋杯全国决赛获奖",
                                    "value": "4-1592",
                                    "parentId": "3-1003",
                                    "points": 300.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1592,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "韬奋杯代表省队参加国家大赛",
                                    "value": "4-1593",
                                    "parentId": "3-1003",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1593,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "韬奋杯入围省内选拔赛",
                                    "value": "4-1594",
                                    "parentId": "3-1003",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1594,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "获得年度大赛奖项或表彰（说考卷、论文大赛、试题命制、一二轮课题大赛、扫雷杯编校大赛、金手指大赛、优秀编辑等）",
                                    "value": "4-1595",
                                    "parentId": "3-1003",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1595,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "获得季度大赛奖项-“i黑马杯”编校竞赛等",
                                    "value": "4-1596",
                                    "parentId": "3-1003",
                                    "points": 30.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1596,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "入选研究院年度十大精品课题",
                                    "value": "4-1597",
                                    "parentId": "3-1003",
                                    "points": 50.0000,
                                    "processId": "5",
                                    "unit": "次",
                                    "projectId": 1597,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "期刊发表",
                    "value": "2-1010",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "期刊发表",
                            "value": "3-1011",
                            "parentId": "2-1010",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "在国家级核心刊物发表论文",
                                    "value": "4-1598",
                                    "parentId": "3-1011",
                                    "points": 300.0000,
                                    "processId": "5",
                                    "unit": "篇",
                                    "projectId": 1598,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "在省级刊物发表论文",
                                    "value": "4-1599",
                                    "parentId": "3-1011",
                                    "points": 200.0000,
                                    "processId": "5",
                                    "unit": "篇",
                                    "projectId": 1599,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "测试1",
                    "value": "2-1014",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "测试1",
                            "value": "3-1015",
                            "parentId": "2-1014",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "测试1",
                                    "value": "4-1514",
                                    "parentId": "3-1015",
                                    "points": 10.0000,
                                    "processId": "5",
                                    "unit": "人",
                                    "projectId": 1514,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "test",
                    "value": "2-2318",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "test",
                            "value": "3-2319",
                            "parentId": "2-2318",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "test",
                                    "value": "4-2421",
                                    "parentId": "3-2319",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "个",
                                    "projectId": 2421,
                                    "childProjectTree": []
                                },
                                {
                                    "name": "tewt",
                                    "value": "4-2438",
                                    "parentId": "3-2319",
                                    "points": 10.0000,
                                    "processId": "5",
                                    "unit": "小时",
                                    "projectId": 2438,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "测试0",
                    "value": "2-2365",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "测试",
                            "value": "3-2366",
                            "parentId": "2-2365",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "测",
                                    "value": "4-2448",
                                    "parentId": "3-2366",
                                    "points": 0.0000,
                                    "processId": "5",
                                    "unit": "小时",
                                    "projectId": 2448,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "C_自动化测试",
                    "value": "2-2478",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "C_自动化测试",
                            "value": "3-2479",
                            "parentId": "2-2478",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "积分自动化测试标准",
                                    "value": "4-3219",
                                    "parentId": "3-2479",
                                    "points": 100.0000,
                                    "processId": "5",
                                    "unit": "项",
                                    "projectId": 3219,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "测试积分1",
                    "value": "2-2541",
                    "parentId": "1-3",
                    "points": 0,
                    "processId": null,
                    "unit": null,
                    "projectId": null,
                    "childProjectTree": [
                        {
                            "name": "测试积分1",
                            "value": "3-2542",
                            "parentId": "2-2541",
                            "points": 0,
                            "processId": null,
                            "unit": null,
                            "projectId": null,
                            "childProjectTree": [
                                {
                                    "name": "测试积分1",
                                    "value": "4-3259",
                                    "parentId": "3-2542",
                                    "points": 150.0000,
                                    "processId": "5",
                                    "unit": "项",
                                    "projectId": 3259,
                                    "childProjectTree": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}