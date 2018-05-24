## 系统常用命令

```

2.clear 清屏   或者command + k(苹果终端)
3.# 超级管理  $  普通用户
4.adduser + 用户名    (创建用户)
  passwd + 用户名     (改新建用户的密码)
  userdel 删用户
5.logout/exit  退出登录 断开与服务器的连接
6.shutdown/init0 关服务器
7.init6/reboot 重启
8.ps 查看自己使用的shell  ps -ef/ps -aux查看详细进程
9.w/who(查看登录用户) /whoami(查看自己)/last查看历史登录用户
10.uname 查看使用系统名
11.hostname 查看主机名
12.sudo以管理员身份执行
13.su + 用户名  切换用户
14.echo
15.ssh 用户名@ip-address   远程登录其他服务器
16.& 将进程放后台执行
17.df查看磁盘使用情况l
18.kill 关进程 -9强制关闭
19.netstat -nap 查看端口号
20.systemctl start 系统启动 ;restart重启/stop停止  status查状态 / (centos7以前版本用 service 进程 start)    enable开机自启  disable 关闭开机自启
21.firewalld 防火墙  -cmd 配置防火墙 
firewall -cmd --add-port=80/tcp --permanent

```

## 特别重要命令

```
1. 制表键(tab)  敲一下是自动补全,两下是提示你的命令补全
2.man + 命令 查看命令使用手册 -q退出
命令 --help(查看帮助(参数))
whatis + ()  (简短描述)
3.pwd 查看当前目录
4.whereis/which + () 查看文件路径
5.control c  终止命令执行
6.命令后面+& 后台运行 ;  加 > result.txt & 将结果保存在result.txt里面 ;  加 > result.txt 2> error.txt & 将正确的放在result.txt里面  将出错的内容放在error.txt里面 
7. | 管道过滤
```

### 文件相关操作

```
1.mkdir 创建目录
2.rmdir 删除目录(只能删空目录) ; rm -rf 删文件,或者文件夹(可以删非空,慎用); rm -r(递归 删文件) ;f代表不询问直接删除
3.touch 文件不存在创建空文件,文件存在修改文件最后使用时间 更改内容时间(mtime) 更改权限时间(ctime) 更改最后访问时间(atime)
4.查看目录下文件 ls/ll/ls -l/ls -a(查看隐藏)/ls -la/ls -R(递归展开)
5.cd 进某个目录; cd ..(进入上一级目录); cd ../..(返回上两级目录) 相对目录 ;    cd /home/....  绝对路径
6.cat 查看文件内容 ;cat | less 一页一页查看 ;head/tail -n  只看前面/后面n行 
7.root/home(用户主目录) ; etc(配置); usr
8.cp 拷贝
9.上下键可以查看前面的命令;   history(查看以前的命令)  !+命令编号  再次执行该编号命令
10.mv(move) 剪切(移动文件,文件夹)  改名
11.wget -O filename 网址   获取网络资源保存为filename
12.grep 搜索内容(文件里面搜字符串)      grep (内容/正则表达式) .(目录) -R(递归) -N(行号)
13.find 搜文件
14. > 输出重定向 将执行结果放在>号后面的文件里面 ; 两个> 追加模式 ;> 2> 错误输出重定向
15.jobs 查看后台任务 ;fg %n将后台任务放前台执行 , bg %n 再次将前台任务放后台执行
16.wc 查看文件有多少行 多少单词  多少字节数
17.sort 排序  uniq 去相邻行重复
diff 查看文件的差异 file 查看文件详细信息
18. date 日期  cal  日历
19.vim .vimrc 进行vim配置
20.scp 文件名 用户名@ip地址:路径地址
21.ln filename path  创建硬链接(数据很大的情况下备份) ; ln -s filename1 filename2 将file1创建软链接(相当于快捷方式,不具有备份功能) 
22.tar -xvf(详细过程)/xf(静默)-解归档         tar -cvf filename *(*当前路径下所有文件)-归档
23.gzip/gunzip 压缩/解压 ; xz -z/d   压缩/解压缩-后面跟-1到9表示压缩比
24.起别名    alias 别名='系统命令名'  ; unalias 别名 (删除别名)
25.chmod u+x 修改权限  (u,代表所有者,o代表其他用户,g代表同组用户)(x 执行,r阅读,w编辑) rwx对应二进制的数据可以一次性修改 777表示所有都可以读写执行 776代表所有者和其他用户有所有权限,同组用户只要读写权限ss


```

### vim操作

```
1.w保存;q退出;!强制
2.dw 删一个单词 dd删除整行,d$删除到行尾
3.:inoremap pymain if __name__ == '__main__':
4.命令模式到行尾 $ 行首是 ^
5.命令模式下按u 撤销上一步操作
6.查找替换  命令模式下 /查找 ;
:1,$s/one/two/g  将全文中的one替换成two
```

### yum,rpm安装软件操作

```
1.yum list install 查看已经安装的软件
2.yum search 查看里面有没有某个软件
3.yum install 安装
4.yum remove 卸载
5.yum update 更新
6.rpm -ivh 安装 ; -e 移除 ;-qa | grep 查询是否安装
7.rpm -qa | grep jdk | xargs rpm -e   将前面搜索出来的包含jdk的文件 当成参数传给rpm -e 可以直接将搜索出来的结果删除

8.先执行config的文件,再执行make && make install 源文件安装(进入文件解压缩目录执行)

9.解压能直接使用的软件,将执行文件夹放PATH环境变量 export PATH=$PATH:执行文件路径(临时) 永久是在.bash_profig 下面该PATH环境变量    ; .bashrc可以永久改别名
```

### nginx

```
index 主页   /etc/nginx/nginx.conf  为nginx配置文件
启动:nginx
```

### mysql

```
连接数据库:mysql -u root -p
未设置密码
```

### redis

```
参考网站:http://redisdoc.com    http://redis.cn
1.后台启动:redis-server myredis.conf > redis.log &
2.客户端连接:redis-cli -h 172.18.61.77(内网ip) -p 6379(端口号)
3.验证密码:auth 117501(密码)
4.shutdown save/nosave 关闭服务器

命令
参考网站:http://redisdoc.com    http://redis.cn
set key value
get key (keys * 查看所有键)
set key value ex 100  设置存活时间100s
ttl key 查看存活时间 (-2表示不再存活,-1表示一直存活)
bgsave 后台保存
flushdb 清空当前数据库 flushall 清理所有数据库

```

### shell

```
菜鸟教程
bash
```

### 防火墙

```
Firewall开启常见端口命令：
firewall-cmd --zone=public --add-port=80/tcp --permanent
Firewall关闭常见端口命令：
firewall-cmd --zone=public --remove-port=80/tcp --permanent
开启防火墙命令：
systemctl start firewalld.service
重启防火墙命令：
firewall-cmd --reload  或者   service firewalld restart
设置开机启动
systemctl enable firewalld
查看状态
systemctl status firewalld或者 firewall-cmd --state

```

### git版本控制

```
本地仓库操作

git init 初始化版本控制
1.git add 将文件拉入版本控制  git add . 把当前目录下的所有文件纳入版本控制
2.git commit -m '注释'  提交版本控制
3.git status 查看暂存区的文件
4.git log 查看提交的日志  后面加 --pretty=oneline是在一行显示
5.git reset --hard +版本号   ,返回历史版本(版本号用git log查看 commit后面的)
6.git reflog 查看以前所有版本日志(包括已经删除的历史版本)
7.git checkout -- 把暂存区的内容撤掉(把文件撤回后要重新修改后提交到暂存区)



本地仓库与服务器仓库连接

8.git clone 克隆项目
9.git push origin master 将本地项目推送到服务器
10.git pull 将服务器的代码更新到本地
11.怎么将本地的仓库上传到 服务器:  1.git remote add origin url  添加服务器仓库 
12.git push -u origin master(第一次要加-u后面不用) 将本地的代码上传到服务器
```

```
流程:

本地建仓库再托管到远端服务器
mkdir hello
cd hello
------------------------------
git init
git add .
git status
git commit -m 'xyz'
git log
git reset --hard id
git reflog
git remote add origin <url>
git push -u origin master
git pull

远端服务器项目已经存在
git clone <url>
cd hello
git add .
git checkout --
git commit -m 'abc'
git push origin master
git pull


分支
1.git branch 后接分支名字是新建分支  不接分支名是查看分支
2.git checkout 切换分支
3.git rm  删除文件 要接着操作 git add  git commit -m
4.git merge 分支名  将分支合并到master

Git日常工作流程
git clone <url>
cd <dir>
git branch <name>
git checkout <name>
----------------------
git add .
git commit -m 'xyz'
git push origin <name>
----------------------
git checkout master
git merge <name>
git push origin master
```

















