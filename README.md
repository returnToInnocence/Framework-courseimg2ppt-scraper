 # PPT Downloader

自动化PPT课程下载工具

## 📋 功能特点

- 自动登录教育管理系统
- 批量下载PPT课程内容
- 自动截图并生成PPT文件
- 支持多课程单元处理
- 可配置的路径和参数设置

## 🚀 快速开始

### 前置要求

- Windows 10/11
- PowerShell 5.0+
- Chrome浏览器

### 安装和运行

1. **打开PowerShell**
   ```powershell
   # 以管理员身份运行PowerShell（推荐）
   ```

2. **进入项目文件夹**
   ```powershell
   cd path/to/PptDownloader
   ```

3. **首次运行 - 环境设置**
   ```powershell
   .\setup.ps1
   ```
   > 这将创建虚拟环境并安装所需依赖，会生成一个 `venv` 文件夹

4. **运行程序**
   ```powershell
   .\run.ps1
   ```

5. **后续使用**
   ```powershell
   # 环境设置完成后，每次只需运行：
   .\run.ps1
   ```

## ⚙️ 配置说明

### 1. 创建配置文件

复制 `config.ini.example` 为 `config.ini`（如果存在示例文件）或创建新的配置文件：

```ini
[credentials]
username = your_username_here
password = your_password_here

[app]
target_url = https://your-target-website.com/path
search_keyword = your_search_keyword
max_pages = 300

[chrome]
binary_location = bin/chrome-win64/chrome.exe
chromedriver_path = bin/chromedriver-win64/chromedriver.exe

[paths]
image_folder = ./temp_images
output_folder = ./output_ppt

[screenshot]
width = 1920
height = 1080
crop_area = 260,0,1650,780
```

### 2. 配置说明

| 配置项 | 描述 | 示例 |
|--------|------|------|
| `credentials` | 登录凭据 | 用户名和密码 |
| `app.target_url` | 目标网站URL | 完整的登录页面地址 |
| `app.search_keyword` | 搜索关键词 | 课程搜索关键词 |
| `chrome.binary_location` | Chrome浏览器路径 | 相对或绝对路径 |
| `chrome.chromedriver_path` | ChromeDriver路径 | 驱动程序路径 |
| `paths.image_folder` | 临时图片文件夹 | 截图存储位置 |
| `paths.output_folder` | 输出PPT文件夹 | 生成的PPT存储位置 |
