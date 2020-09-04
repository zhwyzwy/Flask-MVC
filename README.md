common	`存放公共部分`\
|----	libs	`公共方法或者类`\
|----	models	`所有数据库model`

config	`配置文件`\
|----	base_setting.py 	`基础配置`\
|----	local_setting.py	`本地开发环境配置`\
|----	product_setting.py		`生产环境配置`\

docs	`文档存放`\
|---- Mysql.md	`数据库变更记录`

jobs	`定时任务`\
|---- tasks	`定时任务存放目录`

web	`HTTP`\
|---- controllers	`C层`\
|---- interceptors	`拦截器`\
|---- templates 	`模板文件`\
|---- stati 	`静态文件`

application.py	`封装flask全局变量。app、数据库等`\
manager.py	`启动入口`\
www.py	`HTTP模块初始化`\
requirements.txt	`扩展`\
uwsgi.ini	`生产环境uwsgi`