# game
```json
{
  "column": [
    {
      "sortable": true,
      "prop": "game",
      "type": "string",
      "label": "游戏",
      "width": "80"
    },
    {
      "sortable": false,
      "prop": "name",
      "type": "string",
      "label": "名称",
      "width": ""
    },
    {
      "sortable": false,
      "prop": "address",
      "type": "string",
      "label": "地址",
      "width": ""
    },

    {
      "sortable": false,
      "prop": "map",
      "type": "string",
      "label": "地图",
      "width": "200"
    },
    {
      "sortable": false,
      "prop": "player",
      "type": "string",
      "label": "玩家",
      "width": "120"
    },
    {
      "sortable": false,
      "prop": "CPU",
      "type": "string",
      "label": "CPU",
      "width": "140"
    },
    {
      "sortable": false,
      "prop": "memory",
      "type": "string",
      "label": "内存",
      "width": "100"
    },
    {
      "sortable": false,
      "prop": "status",
      "type": "string",
      "label": "状态",
      "width": "80"
    }
  ],
  "data": [
    {
      "game": "L4D2",
      "name": "Benny's L4D2 Per",
      "address": "game.bennythink.com:27015",
      "map":"沼泽激战",
      "player": "3/4",
      "CPU": "122min 27.295s",
      "memory": "312.12M",
      "status": [
        true,
        "active (running) since Sun 2018-09-30 17:57:56 CST; 1 day 19h ago"
      ]
    },
    {
      "game": "CSGO",
      "name": "Benny's CSGO Private Server",
      "address": "game.bennythink.com:27015",
      "map":"沙漠之城",
      "player": "20/24",
      "CPU": "0.2",
      "memory": "312.12M",
      "status": [
        false,
        "嗝屁啦"
      ]
    }
  ]
}

```
# web
```json
{
  "column": [
    {
      "sortable": false,
      "prop": "name",
      "type": "string",
      "label": "名称",
      "width": "140"
    },
    {
      "sortable": false,
      "prop": "address",
      "type": "string",
      "label": "地址",
      "width": ""
    },
    {
      "sortable": false,
      "prop": "arch",
      "type": "string",
      "label": "架构",
      "width": "80"
    },
    {
      "sortable": false,
      "prop": "app",
      "type": "string",
      "label": "程序",
      "width": "100"
    },
    {
      "sortable": true,
      "prop": "cpu",
      "type": "string",
      "label": "CPU",
      "width": "140"
    },
    {
      "sortable": true,
      "prop": "memory",
      "type": "string",
      "label": "内存",
      "width": "100"
    },
    {
      "sortable": false,
      "prop": "status",
      "type": "string",
      "label": "状态",
      "width": "80"
    }
  ],
  "data": [
    {
      "name": "JetBrains 激活器",
      "address": "https://jbls.bennythink.com/",
      "arch": "LNF",
      "app": "Flask",
      "cpu": "261min 29.511s",
      "memory": "331.92M",
      "status": [
        false,
        "激活服务已停止"
      ]
    },
    {
      "name": "天气预报",
      "address": "https://weather.bennythink.com/",
      "arch": "LNT",
      "app": "Tornado",
      "cpu": "261min 29.511s",
      "memory": "311.92M",
      "status": [
        true,
        "天气预报运行中"
      ]
    }
  ]
}
```
# ss
```json
{
  "column": [
    {
      "sortable": true,
      "prop": "address",
      "type": "string",
      "label": "地址",
      "width": ""
    },
    {
      "sortable": false,
      "prop": "method",
      "type": "string",
      "label": "加密方式",
      "width": "120"
    },
    {
      "sortable": false,
      "prop": "port_pass",
      "type": "string",
      "label": "端口密码",
      "width": ""
    },
    {
      "sortable": false,
      "prop": "CPU",
      "type": "string",
      "label": "CPU",
      "width": "150"
    },
    {
      "sortable": false,
      "prop": "memory",
      "type": "string",
      "label": "内存",
      "width": "100"
    },
    {
      "sortable": false,
      "prop": "network",
      "type": "string",
      "label": "流量",
      "width": "180"
    },
    {
      "sortable": false,
      "prop": "status",
      "type": "string",
      "label": "状态",
      "width": "80"
    },
    {
      "sortable": true,
      "prop": "ping",
      "type": "string",
      "label": "延迟",
      "width": "90"
    }
  ],
  "data": [
    {
      "address": "8.8.8.8",
      "method": "AES-256-CFB",
      "port_pass": [
        {
          "port": 21,
          "password": "2311-21"
        },
        {
          "port": 21,
          "password": "2311-21"
        },
        {
          "port": 75,
          "password": "2311-21"
        },
        {
          "port": 312,
          "password": "321-21"
        },
        {
          "port": 32,
          "password": "2311-21"
        },
        {
          "port": 12345,
          "password": "telnet-23"
        }
      ],
      "CPU": "56min 38.230s",
      "memory": "12.12M",
      "network": "41.6K in, 200.1K out",
      "status": [
        true,
        "运行中"
      ],
      "ping": 231
    },
    {
      "address": "1.1.1.1",
      "method": "AES-256-CFB",
      "port_pass": [
        {
          "port": 1,
          "password": "2311-21"
        },
        {
          "port": 189,
          "password": "21-21"
        },
        {
          "port": 12345,
          "password": "-23"
        }
      ],
      "CPU": "56min 38.230s",
      "memory": "12.12M",
      "network": "41.6K in, 200.1K out",
      "status": [
        false,
        "已停止运行"
      ],
      "ping": 191
    }
  ]
}

```
# login
post
```json
{
"password":"1234"
}
```
