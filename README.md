# RSSWX
1. 个人rss订阅回复机器人

   配置 

```json
{
  "cache": 0,
  "cacheTime": 10000, //todo 缓存
  "source": [{ //配置订阅源  
      "msg": "虎扑",
      "url": "https://rsshub.app/hupu/bbs/bxj/2",
      "size": 5
    },
    {
      "msg": "今天发生了什么？",
      "url": "https://rsshub.app/jike/topic/553870e8e4b0cafb0a1bef68",
      "size": 1
    },
    {
      "msg": "b站电子竞技排行榜",
      "url": "https://rsshub.app/bilibili/partion/ranking/171/3",
      "size": 2
    }, {
      "msg": "好奇心日报",
      "url": "https://rsshub.app/qdaily/category/5",
      "size": 5
    }, {
      "msg": "雪球",
      "url": "https://rsshub.app/xueqiu/user/8152922548",
      "size": 5
    }, {
      "msg": "豆瓣小组",
      "url": "s://rsshub.app/douban/group/camera",
      "size": 5
    }
  ],
  "subscriber": [{
      "name": "卡布达巨人" //订阅用户名

    },
    {
      "name": "pumpkin"
    }
  ]
}
```

