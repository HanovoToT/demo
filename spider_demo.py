import requests
from bs4 import BeautifulSoup
import os

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

target_url = 'https://www.baidu.com'
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
output_file = os.path.join(desktop_path, 'baidu_data.txt')

try:
    response = requests.get(target_url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # 写入标题
        f.write(f"页面标题: {soup.title.string}\n\n")
        
        # 写入所有链接
        f.write("页面链接:\n")
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):
                f.write(f"{href}\n")
    
    print(f"数据已保存到: {output_file}")

except Exception as e:
    print(f"发生错误: {e}")