# buaa_health_checkin
北航健康打卡脚本

放在服务器上定时健康打卡 or 搭配快捷指令一键SSH调用打卡

## How to use
1. 安装依赖：pip install selenium
2. 自行下载[chromedriver](https://chromedriver.chromium.org), 将对应的webdriver文件放在项目一级目录下
3. 一级目录下创建accout.json文件，在json文件内填入account, password，对应统一账号和密码。
4. 运行src/main.py即可完成打卡。
