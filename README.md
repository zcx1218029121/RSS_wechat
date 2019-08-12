# RSSWX
1. 安装依赖 

   python 环境

   

   请在cmd中输入

   ```
   pip install -U wxpy
   ```

   

2. 配置  json

```json
{
  "cache": 0, //是否启用缓存
  "cacheTime": 10000, //缓存超时时间 单位ms
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

2. 配置源

​         https://docs.rsshub.app/ 定制RSS链接

```
{
      "msg": "好奇心日报",
      "url": "https://rsshub.app/qdaily/category/5",
      "size": 5
    }
```

  msg 是指定回复的用词 

 url 是订阅源的链接

size 是返回的条目数 （并不建议配置太多）

3. 配置订阅者

   ```
   {
         "name": "哈士奇" //订阅用户名 
       }
   ```

在这里配置订阅好友的信息

> 配置好json后请验证是否正确



4. 启动订阅机器人
```
python start.py
```