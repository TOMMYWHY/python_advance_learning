import json
import  requests
from pprint import pprint

headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        }

url ="https://zhuanlan.zhihu.com/api/columns/jirengu/articles?include=data%5B*%5D.admin_closed_comment%2Ccomment_count%2Csuggest_edit%2Cis_title_image_full_screen%2Ccan_comment%2Cupvoted_followees%2Ccan_open_tipjar%2Ccan_tip%2Cvoteup_count%2Cvoting%2Ctopics%2Creview_info%2Cauthor.is_following%2Cis_labeled%2Clabel_info"

response = requests.get(url,headers= headers)
# print(response.content.decode())
json_str = response.content.decode()
ret1 = json.loads(json_str)
ret1 = json.loads(json_str)
pprint(ret1)
# print(type(ret1))

with open("json_test.json","w",encoding="utf-8") as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent=4))
