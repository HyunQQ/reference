anay_info_data_settings_json = {'target': 'qty', 'seg_class': 'seg_dscd', 'date': 'bse_ymd', 'anal_pd': '3'}

anay_info_var_settings_json = {'bse_ymd': 'Date|Ymd|yyyymmdd', 'seg_dscd': 'String', 'qty': 'Number'}

check_data_keys = ['target', 'seg_class', 'date']
check_var_keys = [anay_info_data_settings_json['date']]  ############### 수정 필요!!!
print(check_var_keys[0])

print(name in anay_info_data_settings_json.keys() for name in check_data_keys)
print(all(name in anay_info_data_settings_json.keys() for name in check_data_keys))

print(anay_info_var_settings_json[check_var_keys[0]])
test= anay_info_var_settings_json[check_var_keys[0]].split('|')
for i in test:
    print(test)