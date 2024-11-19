import requests
from bs4 import BeautifulSoup
import json

# 目標網頁的URL
url = 'https://www.ifreesite.com/phone/china-area-code.htm'

# 發送HTTP GET請求
response = requests.get(url)

# 確認是否成功取得網頁內容
if response.status_code == 200:
    # 使用BeautifulSoup解析網頁內容
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 找到所有的表格行
    rows = soup.find_all('tr')
    
    # 初始化要存儲所有國家資訊的列表
    countries = []

    # 遍歷每一行，提取國家名稱和國際電話區號
    for row in rows[1:]:  # 從第二行開始，跳過標題行
        # 找到該行的所有列
        cols = row.find_all('td')
        if len(cols) >= 3:
            # 提取國家名稱、英文名稱和國際電話區號
            cn_name = cols[1].get_text().strip()
            en_name = cols[2].get_text().strip()
            code = cols[0].get_text().strip()
            
            # 將資訊存儲為字典格式
            country_info = {
                'cn': cn_name,
                'en': en_name,
                'code': code
            }
            
            # 將國家資訊添加到列表中
            countries.append(country_info)

    # 將列表存儲為JSON檔案
    with open('country_codes_chian.json', 'w', encoding='utf-8') as f:
        json.dump(countries, f, ensure_ascii=False, indent=4)
    
    print("JSON檔案已生成：country_codess_chian.json")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")