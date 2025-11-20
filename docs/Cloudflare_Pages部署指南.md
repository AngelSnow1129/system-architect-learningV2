# ☁️ Cloudflare Pages 部署指南

> 完整的 Cloudflare Pages 部署教程 - 从零开始到上线

## 📋 目录

- [为什么选择 Cloudflare Pages](#为什么选择-cloudflare-pages)
- [准备工作](#准备工作)
- [部署方式](#部署方式)
  - [方式1：Git 集成部署（推荐）](#方式1git-集成部署推荐)
  - [方式2：Wrangler CLI 部署](#方式2wrangler-cli-部署)
  - [方式3：直接上传部署](#方式3直接上传部署)
- [配置优化](#配置优化)
- [自定义域名](#自定义域名)
- [常见问题](#常见问题)
- [最佳实践](#最佳实践)

---

## 🌟 为什么选择 Cloudflare Pages

### 优势对比

| 特性 | Cloudflare Pages | GitHub Pages | Netlify | Vercel |
|------|------------------|--------------|---------|--------|
| **速度** | ⚡⚡⚡⚡⚡ | ⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡⚡⚡ |
| **全球 CDN** | ✅ 275+ 城市 | ✅ 有限 | ✅ 全球 | ✅ 全球 |
| **免费流量** | ✅ 无限 | ✅ 100GB/月 | ✅ 100GB/月 | ✅ 100GB/月 |
| **免费构建** | ✅ 500次/月 | ✅ 无限 | ✅ 300分钟/月 | ✅ 100小时/月 |
| **自定义域名** | ✅ 100个 | ✅ 1个 | ✅ 无限 | ✅ 无限 |
| **HTTPS** | ✅ 自动 | ✅ 自动 | ✅ 自动 | ✅ 自动 |
| **部署速度** | ⚡ 1-2分钟 | ⚡ 2-5分钟 | ⚡ 1-3分钟 | ⚡ 1-3分钟 |
| **回滚** | ✅ 一键 | ❌ | ✅ 一键 | ✅ 一键 |
| **预览部署** | ✅ | ❌ | ✅ | ✅ |

### 核心优势

1. **🚀 极速访问**
   - 全球 275+ 个数据中心
   - 自动选择最近节点
   - 平均响应时间 < 50ms

2. **💰 完全免费**
   - 无限请求
   - 无限带宽
   - 无限网站数量

3. **🔒 安全可靠**
   - 自动 HTTPS
   - DDoS 防护
   - Web 应用防火墙

4. **⚙️ 易于使用**
   - 零配置部署
   - 自动构建
   - 一键回滚

---

## 🛠️ 准备工作

### 1. 注册 Cloudflare 账号

访问 [Cloudflare 注册页面](https://dash.cloudflare.com/sign-up)

- 使用邮箱注册
- 验证邮箱
- 完成账号设置

### 2. 准备项目代码

#### 选项A：使用 Git 仓库（推荐）

```bash
# 如果还没有 Git 仓库
git init
git add .
git commit -m "Initial commit"

# 推送到 GitHub
git remote add origin https://github.com/username/repo.git
git push -u origin main
```

#### 选项B：准备本地文件

确保项目结构完整：
```
项目根目录/
├── web/              # 网站文件
├── keypoint/         # 学习资料
├── images/           # 图片资源
├── _headers          # HTTP 头配置
├── _redirects        # 重定向规则
└── wrangler.toml     # Wrangler 配置
```

---

## 🚀 部署方式

### 方式1：Git 集成部署（推荐）

这是最推荐的方式，支持自动部署和版本管理。

#### 步骤1：登录 Cloudflare Dashboard

1. 访问 [Cloudflare Dashboard](https://dash.cloudflare.com)
2. 使用账号登录

#### 步骤2：创建 Pages 项目

1. 点击左侧菜单 **"Workers & Pages"**
2. 点击 **"Create application"** 按钮
3. 选择 **"Pages"** 标签
4. 点击 **"Connect to Git"**

![创建项目](https://developers.cloudflare.com/assets/pages-create-project.png)

#### 步骤3：连接 Git 仓库

1. 选择 Git 提供商（GitHub 或 GitLab）
2. 点击 **"Connect GitHub"** 或 **"Connect GitLab"**
3. 授权 Cloudflare 访问你的仓库
4. 选择要部署的仓库
5. 点击 **"Begin setup"**

![连接仓库](https://developers.cloudflare.com/assets/pages-connect-git.png)

#### 步骤4：配置构建设置

```yaml
项目名称: architect-learning
（或自定义名称，将成为默认域名的一部分）

生产分支: main
（或 master，取决于你的主分支名称）

构建命令: （留空）
（本项目是纯静态网站，无需构建）

构建输出目录: /
（项目根目录）

根目录: /
（可选，如果项目在子目录中则填写子目录路径）
```

![构建设置](https://developers.cloudflare.com/assets/pages-build-settings.png)

#### 步骤5：环境变量（可选）

本项目无需配置环境变量，可以跳过此步骤。

如果需要，可以添加：
```
变量名: ENVIRONMENT
值: production
```

#### 步骤6：部署

1. 点击 **"Save and Deploy"**
2. 等待部署完成（通常 1-2 分钟）
3. 部署成功后会显示访问链接

![部署成功](https://developers.cloudflare.com/assets/pages-deploy-success.png)

#### 步骤7：访问网站

部署成功后，你会获得一个默认域名：
```
https://architect-learning.pages.dev
```

点击链接即可访问你的网站！

#### 自动部署

配置完成后，每次推送代码到 Git 仓库，Cloudflare Pages 会自动：
1. 检测到代码变更
2. 触发新的部署
3. 构建并发布新版本
4. 更新网站内容

```bash
# 更新网站只需推送代码
git add .
git commit -m "更新内容"
git push
```

---

### 方式2：Wrangler CLI 部署

使用命令行工具部署，适合开发者和自动化场景。

#### 步骤1：安装 Node.js

确保已安装 Node.js（建议 v16 或更高版本）

```bash
# 检查版本
node --version
npm --version
```

下载地址：https://nodejs.org/

#### 步骤2：安装 Wrangler

```bash
# 使用 npm 全局安装
npm install -g wrangler

# 或使用 yarn
yarn global add wrangler

# 或使用 pnpm
pnpm add -g wrangler
```

验证安装：
```bash
wrangler --version
```

#### 步骤3：登录 Cloudflare

```bash
wrangler login
```

这会打开浏览器，要求你授权 Wrangler 访问你的 Cloudflare 账号。

#### 步骤4：部署项目

```bash
# 在项目根目录执行
wrangler pages deploy . --project-name=architect-learning

# 或使用配置文件（如果有 wrangler.toml）
wrangler pages deploy .
```

参数说明：
- `.` - 当前目录
- `--project-name` - 项目名称（首次部署时需要）

#### 步骤5：查看部署结果

部署成功后会显示：
```
✨ Success! Uploaded 150 files (2.5 sec)

✨ Deployment complete! Take a peek over at
   https://architect-learning.pages.dev
```

#### 后续更新

```bash
# 直接部署即可
wrangler pages deploy .
```

#### 高级用法

```bash
# 部署到特定分支
wrangler pages deploy . --branch=dev

# 指定项目名称
wrangler pages deploy . --project-name=my-project

# 查看部署历史
wrangler pages deployment list

# 查看项目列表
wrangler pages project list
```

---

### 方式3：直接上传部署

最简单的方式，无需 Git 或命令行。

#### 步骤1：准备文件

1. 确保项目文件完整
2. 可以压缩为 ZIP 文件（可选）

#### 步骤2：上传部署

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com)
2. 点击 **"Workers & Pages"**
3. 点击 **"Create application"**
4. 选择 **"Pages"** 标签
5. 点击 **"Upload assets"**

![直接上传](https://developers.cloudflare.com/assets/pages-direct-upload.png)

#### 步骤3：上传文件

两种方式：

**方式A：拖拽文件夹**
- 直接将项目文件夹拖拽到上传区域

**方式B：选择 ZIP 文件**
- 点击上传区域
- 选择压缩好的 ZIP 文件

#### 步骤4：配置项目

```
项目名称: architect-learning
```

#### 步骤5：部署

1. 点击 **"Deploy site"**
2. 等待上传和部署完成
3. 获取访问链接

#### 更新网站

要更新网站内容：
1. 进入项目页面
2. 点击 **"Upload new version"**
3. 重新上传文件
4. 部署新版本

---

## ⚙️ 配置优化

### 1. HTTP 头配置（_headers）

创建 `_headers` 文件来优化安全和性能：

```
# 全局安全头
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin

# HTML 文件缓存
/*.html
  Cache-Control: public, max-age=3600, must-revalidate

# Markdown 文件缓存
/*.md
  Cache-Control: public, max-age=3600

# JavaScript 和 CSS 缓存
/*.js
  Cache-Control: public, max-age=31536000, immutable

/*.css
  Cache-Control: public, max-age=31536000, immutable

# 图片缓存
/images/*
  Cache-Control: public, max-age=31536000, immutable
```

### 2. 重定向配置（_redirects）

创建 `_redirects` 文件来配置 URL 重定向：

```
# 重定向根目录到 web 目录
/  /web/index.html  200

# 重定向常用路径
/chapters  /web/chapters.html  200
/nav  /web/nav.html  200
/viewer  /web/viewer.html  200

# 404 页面
/*  /web/index.html  404
```

### 3. Wrangler 配置（wrangler.toml）

创建 `wrangler.toml` 文件用于 CLI 部署：

```toml
name = "architect-learning"
compatibility_date = "2024-01-01"

[site]
bucket = "."

[build]
command = ""
cwd = ""
watch_dirs = ["web", "keypoint", "images"]

[dev]
port = 8000
local_protocol = "http"
```

---

## 🌐 自定义域名

### 添加自定义域名

#### 步骤1：进入域名设置

1. 进入你的 Pages 项目
2. 点击 **"Custom domains"** 标签
3. 点击 **"Set up a custom domain"**

#### 步骤2：输入域名

```
输入你的域名: www.example.com
或: example.com
```

#### 步骤3：配置 DNS

Cloudflare 会提供 DNS 配置说明：

**如果域名在 Cloudflare**（推荐）：
- 自动配置，无需手动操作
- 点击 **"Activate domain"** 即可

**如果域名在其他服务商**：
- 添加 CNAME 记录：
  ```
  类型: CNAME
  名称: www（或 @）
  值: architect-learning.pages.dev
  ```

#### 步骤4：等待生效

- DNS 配置通常在 5-10 分钟内生效
- HTTPS 证书自动签发（可能需要几分钟）

#### 步骤5：验证

访问你的自定义域名，确认网站正常运行。

### 多个域名

可以添加多个域名指向同一个网站：
- `example.com`
- `www.example.com`
- `app.example.com`

---

## ❓ 常见问题

### Q1: 部署后页面显示空白？

**原因**：可能是路径配置问题

**解决方案**：
1. 检查 `Build output directory` 是否设置为 `/`
2. 确保 `web/index.html` 文件存在
3. 使用 `_redirects` 文件配置根路径重定向

### Q2: 图片无法显示？

**原因**：图片路径不正确

**解决方案**：
1. 确保 `images` 文件夹已上传
2. 检查图片路径是否正确（相对路径）
3. 查看浏览器控制台的错误信息

### Q3: Markdown 文件无法加载？

**原因**：跨域或路径问题

**解决方案**：
1. 确保所有 `.md` 文件已上传
2. 检查 `config.js` 中的路径配置
3. 使用浏览器开发者工具查看网络请求

### Q4: 如何回滚到之前的版本？

**步骤**：
1. 进入项目页面
2. 点击 **"Deployments"** 标签
3. 找到要回滚的版本
4. 点击 **"Rollback to this deployment"**

### Q5: 如何查看部署日志？

**步骤**：
1. 进入项目页面
2. 点击 **"Deployments"** 标签
3. 点击具体的部署
4. 查看 **"Build log"** 和 **"Function log"**

### Q6: 免费版有什么限制？

**免费版额度**：
- ✅ 无限请求
- ✅ 无限带宽
- ✅ 500 次构建/月
- ✅ 100 个自定义域名
- ✅ 无限网站数量

对于本项目来说，免费版完全够用！

### Q7: 如何删除项目？

**步骤**：
1. 进入项目页面
2. 点击 **"Settings"** 标签
3. 滚动到底部
4. 点击 **"Delete project"**
5. 确认删除

### Q8: 支持哪些 Git 平台？

**支持的平台**：
- ✅ GitHub
- ✅ GitLab
- ❌ Bitbucket（暂不支持）

### Q9: 如何设置环境变量？

**步骤**：
1. 进入项目页面
2. 点击 **"Settings"** 标签
3. 点击 **"Environment variables"**
4. 添加变量名和值
5. 选择环境（Production/Preview）
6. 保存

### Q10: 部署失败怎么办？

**排查步骤**：
1. 查看部署日志
2. 检查文件结构是否完整
3. 确认构建命令是否正确
4. 查看 Cloudflare 状态页面
5. 联系 Cloudflare 支持

---

## 💡 最佳实践

### 1. 使用 Git 集成

**优势**：
- 自动部署
- 版本控制
- 预览部署
- 团队协作

**推荐工作流**：
```bash
# 开发分支
git checkout -b feature/new-content
# 修改内容
git add .
git commit -m "添加新内容"
git push origin feature/new-content

# 创建 Pull Request
# Cloudflare 会自动创建预览部署

# 合并到主分支
git checkout main
git merge feature/new-content
git push origin main
# 自动部署到生产环境
```

### 2. 优化缓存策略

**HTML 文件**：短期缓存
```
Cache-Control: public, max-age=3600, must-revalidate
```

**静态资源**：长期缓存
```
Cache-Control: public, max-age=31536000, immutable
```

**动态内容**：不缓存
```
Cache-Control: no-cache, no-store, must-revalidate
```

### 3. 使用预览部署

**功能**：
- 每个 Pull Request 自动创建预览部署
- 独立的预览 URL
- 不影响生产环境

**用途**：
- 测试新功能
- 审查代码变更
- 团队协作

### 4. 监控网站性能

**使用 Analytics**：
1. 进入项目页面
2. 点击 **"Analytics"** 标签
3. 查看：
   - 访问量
   - 流量统计
   - 性能指标
   - 错误日志

### 5. 设置通知

**配置通知**：
1. 进入项目设置
2. 配置部署通知
3. 选择通知方式：
   - Email
   - Webhook
   - Slack

### 6. 使用 Web Analytics

**启用分析**：
1. 进入项目设置
2. 启用 **"Web Analytics"**
3. 添加跟踪代码到网站
4. 查看访问数据

### 7. 优化图片

**建议**：
- 使用 WebP 格式
- 压缩图片大小
- 使用 CDN 加速
- 懒加载图片

### 8. 安全配置

**推荐设置**：
```
# _headers 文件
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
```

---

## 📚 相关资源

### 官方文档
- [Cloudflare Pages 文档](https://developers.cloudflare.com/pages/)
- [Wrangler CLI 文档](https://developers.cloudflare.com/workers/wrangler/)
- [配置参考](https://developers.cloudflare.com/pages/platform/build-configuration/)

### 社区资源
- [Cloudflare 社区](https://community.cloudflare.com/)
- [Discord 频道](https://discord.gg/cloudflaredev)
- [GitHub 讨论](https://github.com/cloudflare/pages-action/discussions)

### 视频教程
- [Cloudflare Pages 入门](https://www.youtube.com/watch?v=IeHC4NwkEfc)
- [部署静态网站](https://www.youtube.com/watch?v=MTc4zZWljYw)

---

## 🎉 总结

Cloudflare Pages 是部署静态网站的最佳选择：

✅ **快速** - 全球 CDN 加速  
✅ **免费** - 无限流量和请求  
✅ **简单** - 零配置部署  
✅ **安全** - 自动 HTTPS 和 DDoS 防护  
✅ **可靠** - 99.99% 可用性保证  

现在就开始部署你的学习平台吧！

---

**需要帮助？**

- 📧 Email: support@cloudflare.com
- 💬 社区: https://community.cloudflare.com/
- 📖 文档: https://developers.cloudflare.com/pages/

---

**祝部署顺利！** 🚀
