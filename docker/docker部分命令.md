docker login --username=xxx address

docker build -t address/project-001 .

①查看docker镜像：
docker images

②查看容器：
查看正在运行的容器 docker ps
查看所有容器(含停止、异常等状态的容器) docker ps -a

③获取镜像
docker pull 镜像名

④创建容器
docker run -itd --name amz_api amz_tasks sh
docker run [args] 镜像名:镜像标签 执行命令
该指令会以busybox镜像为基础创建一个名为 anyrobot-test的容器，容器内执行的程序为"sh"。并且返回一个字符串，这是容器的ID ,用于唯一标识一个容器

⑤停止容器
docker stop 容器名或容器ID

⑥docker rm 容器名或容器

⑦进入容器
docker exec -it 容器名或容器ID 执行命令(一般为bash或sh)

⑧查看容器信息
docker inspect 容器名或ID

⑦在容器与主机间复制文件
从主机将文件传入容器：
docker cp 文件名 容器名:容器内路径
以一名为ruby的文件为例
从容器内将文件取到主机：
docker cp 容器名:容器内文件路径 主机存放路
以容器内的/usr目录为例