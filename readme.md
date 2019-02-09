# tabelog

## 基本情况
1. 起始于： 2018年5月   
2. 相关国家和地区： 日本


## 数据的获取
- 通过web页面解析  
  访问: https://tabelog.com/kyoto/A2601/A260201/xxxx  
  餐馆id确认方法: 其实为001, 结束的id通过测试, 找出最后一个能获取餐馆的id   
- 注意:需要登录日文或英文页面,才能正常访问,中文界面没有js返回

## 代码地址
[gitlab](https://gitlab.yunfutech.com/uber_crawler/tabelog.git)  
脚本操作见 readme.md


## 进展
2018-05： 提交第一版数据  
正常...

## 追加要求

每次的结果，用wps转成xlsx文件，两份都打包上传

## 使用说明(每次启动前修改mongodb_util.py中的日期)

1. 频率: 每月一次, 目前运行服务器: 东京3/4/5 预计三天

2. VERSION值为latest,表示最新版本,每次拿取数据时,将latest修改为当时的日期版本,这样下次就可以直接运行当前内容

3. 结果输出路径: crawlerOutput/latest/tabelog/cityname.csv

4. 根据需要的城市, 运行tabelog_v1.py,附加城市对应的id  
   命令行进行了封装, 也可以运行run.py中特定语句即可

5. 爬虫目前在东京服务器运行, 每次启动三台服务器, 6个城市分散运行, 大约需要三天时间, 所以每月28或29号开始启动.

6. 数据提交: 每次的结果, 先修改文件夹latest为当时日期版本，然后用wps转成xlsx文件，两份都打包上传

7. **暂停继续功能**:  
    每个城市运行, 将自动保存进度到独立的文件cityname_has_get.txt, 删除后重新开始运行

8. **反爬说明**:  
    网站会在服务器时间: 23:15(大约北京时间6点左右)左右检查并封锁ip, 需要在上班后查看进度并重启3台服务器切换ip.
    
9. 数据保存
    ```
        数据保存至东京0的mongo数据库中,运行脚本导出数据
    ```

