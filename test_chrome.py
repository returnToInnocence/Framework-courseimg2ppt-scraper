from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

def test_chrome_setup():
    print("开始测试Chrome和chromedriver配置...")
    
    try:
        # 检查文件是否存在
        chrome_path = r'bin\chrome-win64\chrome.exe'
        chromedriver_path = r'bin\chromedriver-win64\chromedriver.exe'
        
        print(f"检查Chrome路径: {chrome_path}")
        if os.path.exists(chrome_path):
            print("✓ Chrome文件存在")
        else:
            print("✗ Chrome文件不存在")
            return False
            
        print(f"检查chromedriver路径: {chromedriver_path}")
        if os.path.exists(chromedriver_path):
            print("✓ chromedriver文件存在")
        else:
            print("✗ chromedriver文件不存在")
            return False
        
        # 配置Chrome选项
        chrome_options = Options()
        chrome_options.binary_location = chrome_path
        
        # 添加一些基本选项
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        # 如果你不想看到浏览器窗口，可以取消下面这行的注释
        # chrome_options.add_argument('--headless')
        
        # 创建Service对象
        service = Service(executable_path=chromedriver_path)
        
        print("正在启动Chrome浏览器...")
        
        # 初始化浏览器
        browser = webdriver.Chrome(service=service, options=chrome_options)
        
        print("✓ Chrome浏览器启动成功")
        
        # 测试基本操作
        print("正在访问测试网站...")
        browser.get("https://www.baidu.com")
        
        print("✓ 网站访问成功")
        
        # 获取网页标题
        title = browser.title
        print(f"网页标题: {title}")
        
        # 等待几秒钟让您看到浏览器
        print("等待5秒钟...")
        time.sleep(5)
        
        # 关闭浏览器
        browser.quit()
        print("✓ 浏览器已关闭")
        
        print("🎉 测试完成！Chrome和chromedriver配置正确")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

if __name__ == "__main__":
    test_chrome_setup() 