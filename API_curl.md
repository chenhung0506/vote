# 新增user (一般)
```
curl 'http://192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/user' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1MzI0MDE0LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTIzNzYxNH0.UrfgMosBiuFvfLEA5iG_HEGaLb21b9J_h-1PWPWeGSg' \
  -H 'Cookie: JSESSIONID=DFD093176F393469210A559AE50E4936; verify=7e2ba10110f719dd65a0403305770b08; userid=4b21158a395311e88a710242ac110002; enterprise=4e2871816dac4698ac794ee87684b532; appid=b4a7b8e1438c4a9885f290b93931dde5; robotDataJson={"appid":"b4a7b8e1438c4a9885f290b93931dde5"}' \
  --data-binary '{"type":2,"username":"jason4","name":"jason4","email":"chenhung@gmail.com","phone":"","password":"d3b5732d822890bf35c59a12c9764f8a","status":1,"organization":[{"value":3,"label":"凱基銀行電銷機器人","type":1,"products":[{"productid":1,"productname":"機器人平台","privilegeSet":[{"id":"b4a7b8e1438c4a9885f290b93931dde5","role_bf":"bcd9cc9959674488974a06d2adaf5b0b"},{"id":"e2132626804c4cabbaca7aee0324da98","role_bf":"bcd9cc9959674488974a06d2adaf5b0b"},{"id":"81ec1b85272f4c4486a3242fc6b2451e","role_bf":"8cfe4df4bdb04f149ab79fe73c511a66"},{"id":"1139b73ad87a4b8595b7b685c0386c43","role_bf":"8cfe4df4bdb04f149ab79fe73c511a66"}],"rolesList":[{"value":"bcd9cc9959674488974a06d2adaf5b0b","label":"BF機器人-一般權限","product":1,"roleid":11,"disabled":false},{"value":"8cfe4df4bdb04f149ab79fe73c511a66","label":"BF機器人-創建管理員權限","product":1,"roleid":12,"disabled":false}],"roleids":[],"value":"{\"apps\":{\"b4a7b8e1438c4a9885f290b93931dde5\":[\"bcd9cc9959674488974a06d2adaf5b0b\"],\"e2132626804c4cabbaca7aee0324da98\":[\"bcd9cc9959674488974a06d2adaf5b0b\"],\"81ec1b85272f4c4486a3242fc6b2451e\":[\"8cfe4df4bdb04f149ab79fe73c511a66\"],\"1139b73ad87a4b8595b7b685c0386c43\":[\"8cfe4df4bdb04f149ab79fe73c511a66\"]},\"groups\":{}}"},{"productid":2,"productname":"電話機器人","privilegeSet":[{"id":"","role_ccbot":2},{"id":"","role_ccbot":1}],"rolesList":[{"value":1,"label":"外呼-管理員權限","product":2,"roleid":1,"disabled":false},{"value":2,"label":"外呼-一般用戶權限","product":2,"roleid":2,"disabled":false}],"roleids":[2,1],"value":"{\"apps\":{},\"groups\":{}}"}],"orgid":3,"orgtype":1}]}' \
```

# 新增user (企業管理員)
```
curl 'http://192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/user' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1MzI0MDE0LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTIzNzYxNH0.UrfgMosBiuFvfLEA5iG_HEGaLb21b9J_h-1PWPWeGSg' \
  --data-binary '{"type":1,"username":"QQQ123","name":"QQQ123","email":"emotbot@emotibot.com","phone":"","password":"d3b5732d822890bf35c59a12c9764f8a","status":1,"organization":[{"value":3,"label":"凱基銀行電銷機器人","type":1,"products":[{"productid":1,"productname":"機器人平台","privilegeSet":[{"id":"","role_bf":""}],"rolesList":[{"value":"bcd9cc9959674488974a06d2adaf5b0b","label":"BF機器人-一般權限","product":1,"roleid":11,"disabled":false},{"value":"8cfe4df4bdb04f149ab79fe73c511a66","label":"BF機器人-創建管理員權限","product":1,"roleid":12,"disabled":false}],"roleids":[],"value":"{\"apps\":{},\"groups\":{}}"},{"productid":2,"productname":"電話機器人","privilegeSet":[{"id":"","role_ccbot":2}],"rolesList":[{"value":1,"label":"外呼-管理員權限","product":2,"roleid":1,"disabled":false},{"value":2,"label":"外呼-一般用戶權限","product":2,"roleid":2,"disabled":false}],"roleids":[2],"value":"{\"apps\":{},\"groups\":{}}"}],"orgid":3,"orgtype":1}]}' \
```

# 刪除 user 
```
curl 'http://192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/user/2fd1c331e68443e690b67e227ec942c6/delete_user' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'X-Userid: 4b21158a395311e88a710242ac110002' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1MzI0MDE0LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTIzNzYxNH0.UrfgMosBiuFvfLEA5iG_HEGaLb21b9J_h-1PWPWeGSg' \
  -H 'Cookie: JSESSIONID=DFD093176F393469210A559AE50E4936; verify=7e2ba10110f719dd65a0403305770b08; userid=4b21158a395311e88a710242ac110002; enterprise=4e2871816dac4698ac794ee87684b532; appid=b4a7b8e1438c4a9885f290b93931dde5; robotDataJson={"appid":"b4a7b8e1438c4a9885f290b93931dde5"}' \
  --data-binary '{"id":"558136a463c54ec985f9c5caa5c444f0","status":0}' \
```

# 查詢 機器人列表
```
curl 'http://192.168.3.216/auth/v5/enterprise/4e2871816dac4698ac794ee87684b532/apps' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1MzI0MDE0LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTIzNzYxNH0.UrfgMosBiuFvfLEA5iG_HEGaLb21b9J_h-1PWPWeGSg' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36' \
  -H 'X-Userid: 4b21158a395311e88a710242ac110002' \
  -H 'Cookie: JSESSIONID=DFD093176F393469210A559AE50E4936; verify=7e2ba10110f719dd65a0403305770b08; userid=4b21158a395311e88a710242ac110002; enterprise=4e2871816dac4698ac794ee87684b532; appid=b4a7b8e1438c4a9885f290b93931dde5; robotDataJson={"appid":"b4a7b8e1438c4a9885f290b93931dde5"}' \
  --compressed \
  --insecure
```

curl 'http://192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/user' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'X-Locale: zh-tw' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'X-Userid: 4b21158a395311e88a710242ac110002' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1MzI0MDE0LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTIzNzYxNH0.UrfgMosBiuFvfLEA5iG_HEGaLb21b9J_h-1PWPWeGSg' \
  -H 'If-Modified-Since: 0' \
  -H 'enterpriseId: 4e2871816dac4698ac794ee87684b532' \
  -H 'X-Appid: ' \
  -H 'Origin: http://192.168.3.216' \
  -H 'Referer: http://192.168.3.216/' \
  -H 'Accept-Language: zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6' \
  -H 'Cookie: JSESSIONID=DFD093176F393469210A559AE50E4936; verify=7e2ba10110f719dd65a0403305770b08; userid=4b21158a395311e88a710242ac110002; enterprise=4e2871816dac4698ac794ee87684b532; appid=b4a7b8e1438c4a9885f290b93931dde5; robotDataJson={"appid":"b4a7b8e1438c4a9885f290b93931dde5"}' \
  --data-binary '{"type":2,"username":"jason65","name":"jason65","email":"chenhung@1.com","phone":"","password":"d3b5732d822890bf35c59a12c9764f8a","status":1,"organization":[{"value":3,"label":"凱基銀行電銷機器人","type":1,"products":[{"productid":1,"productname":"機器人平台","privilegeSet":[{"id":"","role_bf":""}],"rolesList":[{"value":"bcd9cc9959674488974a06d2adaf5b0b","label":"BF機器人-一般權限","product":1,"roleid":11,"disabled":false},{"value":"8cfe4df4bdb04f149ab79fe73c511a66","label":"BF機器人-創建管理員權限","product":1,"roleid":12,"disabled":false}],"roleids":[],"value":"{\"apps\":{},\"groups\":{}}"},{"productid":2,"productname":"電話機器人","privilegeSet":[{"id":"","role_ccbot":2}],"rolesList":[{"value":1,"label":"外呼-管理員權限","product":2,"roleid":1,"disabled":false},{"value":2,"label":"外呼-一般用戶權限","product":2,"roleid":2,"disabled":false}],"roleids":[2],"value":"{\"apps\":{},\"groups\":{}}"}],"orgid":3,"orgtype":1}]}' \
  --compressed \
  --insecure

# 撈全部機器人ID
```
curl -X GET 'http://172.17.0.1/auth/v4/enterprise/3d39aee236ca4437b61378f9737175c2/apps' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiIxNTFhNGFkZmI5MTc0ZGU4YTBiMWY0ZjY5MDRmZGE4YiIsInVzZXJfaWQiOiIxNSIsInVzZXJfbmFtZSI6IkFETUlOXzEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiLCJkaXNwbGF5X25hbWUiOiJBRE1JTl8xIiwiZW1haWwiOiJhYmNAYWJjLmNvbSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiLCJwaG9uZSI6IjA5MTExMTExMTEgICAgICAgICAgIiwidHlwZSI6MSwicm9sZXMiOnsiZ3JvdXBzIjpbXSwiYXBwcyI6W119LCJwcm9kdWN0IjpbIiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiXSwic3RhdHVzIjoxLCJlbnRlcnByaXNlIjoiM2QzOWFlZTIzNmNhNDQzN2I2MTM3OGY5NzM3MTc1YzIiLCJjdXN0b20iOm51bGx9LCJleHAiOjE2MDg3ODMwODcsImlzcyI6InNpbXBsZS1hdXRoIiwibmJmIjoxNjA4Njk2Njg3fQ.ruYHOnDFqhwdtpwr_wRLPNPGdECiFd1GDAR8BcCHZcI' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'enterpriseId: 3d39aee236ca4437b61378f9737175c2' 
```

# 撈 BFOP 機器人 role list
```
curl 'http://192.168.3.216/permit/roles/4e2871816dac4698ac794ee87684b532' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1NjE0NzAyLCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTUyODMwMn0.YG77RbaF_dCCNcKjMOtYld-aPVpowyxUoJNxYkP-q2I' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'X-Userid: 4b21158a395311e88a710242ac110002' \
  -H 'X-Appid: b4a7b8e1438c4a9885f290b93931dde5' \
  -H 'enterpriseId: 4e2871816dac4698ac794ee87684b532'
```

curl 'http://192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/user/bea51b7b71244483a4b48e7c7249acaa/put_user' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1NzcxODk5LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTY4NTQ5OX0.QP20DnAmEP8BOLa3TOz3mK8b8TB7-JFiCphF7MSig8c' \
  -H 'enterpriseId: 4e2871816dac4698ac794ee87684b532' \
  --data-binary '{"id":"bea51b7b71244483a4b48e7c7249acaa","type":2,"username":"test1109","name":"test1109","email":"test1109@test1109.com","phone":"","status":1,"organization":[{"value":3,"label":"凱基銀行電銷機器人","type":1,"products":[{"productid":1,"productname":"機器人平台","privilegeSet":[{"id":"b4a7b8e1438c4a9885f290b93931dde5","role_bf":"bcd9cc9959674488974a06d2adaf5b0b"}],"rolesList":[{"value":"bcd9cc9959674488974a06d2adaf5b0b","label":"BF_BOT_MEMBER","product":1,"roleid":11,"disabled":false},{"value":"8cfe4df4bdb04f149ab79fe73c511a66","label":"BF_BOT_MANAGER","product":1,"roleid":12,"disabled":false}],"roleids":[],"value":"{\"apps\":{\"b4a7b8e1438c4a9885f290b93931dde5\":[\"bcd9cc9959674488974a06d2adaf5b0b\"]},\"groups\":{}}"},{"productid":2,"productname":"電話機器人","privilegeSet":[{"id":"","role_ccbot":1},{"id":"","role_ccbot":2}],"rolesList":[{"value":1,"label":"CC_BOT_MANAGER","product":2,"roleid":1,"disabled":false},{"value":2,"label":"CC_BOT_MEMBER","product":2,"roleid":2,"disabled":false}],"roleids":[1,2],"value":"{\"apps\":{},\"groups\":{}}"}],"orgid":3,"orgtype":1}]}' \

  192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/users





新增企業管理員
  curl 'http://192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/user' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1ODYzNTQ0LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTc3NzE0NH0.ynCeLuw8EkDIJT9yiMZ0Go8MGaA1oIYml_cF60_ab6s' \
  --data-binary '{"type":1,"username":"jason_admin2","name":"jason_admin","email":"jasonadmin@jasonadmin.com","phone":"","password":"d3b5732d822890bf35c59a12c9764f8a","status":1,"organization":[{"value":3,"label":"凱基銀行電銷機器人","type":1,"products":[{"productid":1,"productname":"機器人平台","privilegeSet":[],"rolesList":[{"value":"bcd9cc9959674488974a06d2adaf5b0b","label":"BF_BOT_MEMBER","product":1,"roleid":11,"disabled":false},{"value":"8cfe4df4bdb04f149ab79fe73c511a66","label":"BF_BOT_MANAGER","product":1,"roleid":12,"disabled":false}],"roleids":[],"value":"{\"apps\":{},\"groups\":{}}"},{"productid":2,"productname":"電話機器人","privilegeSet":[{"id":"","role_ccbot":2}],"rolesList":[{"value":1,"label":"CC_BOT_MANAGER","product":2,"roleid":1,"disabled":false},{"value":2,"label":"CC_BOT_MEMBER","product":2,"roleid":2,"disabled":false}],"roleids":[2],"value":"{\"apps\":{},\"groups\":{}}"}],"orgid":3,"orgtype":1}]}' \


隱藏 user 
curl 'http://192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/user/335710270fc2423d944c31e87935c114/put_status' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1ODY1NTQ2LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTc3OTE0Nn0.YSNHEif61C11x3LPWgRw0-qOTYDWk95q04fRLJiU4Z0' \
  --data-binary '{"id":"335710270fc2423d944c31e87935c114","status":1}'

改密碼
curl 'http://192.168.3.216/permit/enterprise/4e2871816dac4698ac794ee87684b532/user/c9bc3823c2b246b8a6d7832d55cd39b3/put_pwd' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOiIxIiwidXNlcl9uYW1lIjoiZGVwbG95ZXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICIsImRpc3BsYXlfbmFtZSI6IlNZU1RFTSIsImVtYWlsIjoiYWRtaW5AZW1vdGlib3QuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiwicGhvbmUiOiIgICAgICAgICAgICAgICAgICAgICIsInR5cGUiOjAsInJvbGVzIjp7Imdyb3VwcyI6W10sImFwcHMiOltdfSwicHJvZHVjdCI6WyIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIl0sInN0YXR1cyI6MiwiZW50ZXJwcmlzZSI6bnVsbCwiY3VzdG9tIjpudWxsfSwiZXhwIjoxNjA1ODU5OTA3LCJpc3MiOiJzaW1wbGUtYXV0aCIsIm5iZiI6MTYwNTc3MzUwN30.xArEugzXDsW1x4dVT9QQx712vYaY0NEN45VzqDbVzfA' \
  -H 'enterpriseId: 4e2871816dac4698ac794ee87684b532' \
  -H 'X-Appid: b4a7b8e1438c4a9885f290b93931dde5' \
  -H 'Cookie: verify=7e2ba10110f719dd65a0403305770b08; userid=4b21158a395311e88a710242ac110002; enterprise=4e2871816dac4698ac794ee87684b532; appid=b4a7b8e1438c4a9885f290b93931dde5; robotDataJson={"appid":"b4a7b8e1438c4a9885f290b93931dde5"}; JSESSIONID=91948CAD2C64E11EF2AABD602C9AE51D' \
  --data-binary '{"id":"c9bc3823c2b246b8a6d7832d55cd39b3","type":2,"username":"333333","name":"test","email":"333@adb.com","phone":"123213","password":"d3b5732d822890bf35c59a12c9764f8a","status":1,"verify_password":"7e2ba10110f719dd65a0403305770b08"}' \


UAT環境
host=172.31.1.165
營運環境
host=172.18.255.183

# SSO 登入
http://localhost:8330/customized/SSOLogin
http://botu.kgibank.com/customized/SSOLogin


# 查詢 USER 角色及其他資料
http://localhost:8330/customized/ManageUser?ActionType=QUERY&objectType=UserAuth&Userid=051045
# 查詢角色清單
http://localhost:8330/customized/ManageUser?ActionType=QUERY&objectType=RoleAuth
# 查詢使用者清單
http://localhost:8330/customized/getUserList

# 新增 USER （ADMIN)
http://localhost:8330/customized/ManageUser?Userid=ADMIN_1&UserCName=29608&UserEmail=abc@abc.com&UserTel=0911111111&Role=ADMIN&ActionType=ADD
# 新增 USER （MANAGER)
http://localhost:8330/customized/ManageUser?Userid=MANAGER_1&UserCName=MANAGER_1&UserEmail=abc@abc.com&UserTel=0911111111&Role=MANAGER&ActionType=ADD
# 新增 USER （MEMBER)
http://localhost:8330/customized/ManageUser?Userid=XXXXXXXXXXX&UserCName=XXXXXXXXXXX&UserEmail=abc@abc.com&UserTel=0911111111&Role=MEMBER&ActionType=ADD

# 更新 USER
http://localhost:8330/customized/ManageUser?Userid=XXXXXXXXXXX&UserCName=XXXXXXXXXXXXX&UserEmail=abcd@abc.com&UserTel=0911122211&Role=MEMBER&ActionType=UPDATE

# 刪除 USER
http://localhost:8330/customized/ManageUser?ActionType=DEL&Userid=XXXXXXXXXX

http://localhost:8330/customized/ManageUser?ActionType=DEL&Userid=MANAGER_6




http://172.31.1.165/customized/ManageUser?Userid=MEMBER_3&UserCName=MEMBER_3&UserEmail=abc@abc.com&UserTel=0911111111&Role=MANAGER&ActionType=ADD