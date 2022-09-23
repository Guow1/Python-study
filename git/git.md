git status 获取当前状态
git add . 将项目中的文件添加到本地仓库
git commit -m "upgrade template to 20210317"  将文件提交到仓库
git pull
git branch　　　　查看本地分支
git branch -v　　   查看本地分支的具体信息（commit id，例如：f65ded9 和 commit 信息）
git branch -r　　　查看远程分支
git branch -a　　   查看本地和远程分支
git branch -vv         查看本地分支和远程分支的对应关系
git branch <new-branch-name>　　　　　　　　　　新建本地分支
git branch <new-branch-name> <commit id> 　　　　给 commit id 新建一个分支
git branch -d <branch-name> [<branch-name>]　　   删除（多个）本地分支
git branch -m <new-anem>　　　　　　　　　　　　在当前分支中修改当前分支的名字
git checkout <branch-name>　　切换到另外的一个分支
git diff <branch-name>
git push 推送分支
