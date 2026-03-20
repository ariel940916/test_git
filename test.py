import ipywidgets as widgets
from IPython.display import display, clear_output

def manual_to_decimal(value_str, base):
    #將N進位字串手動轉為 10 進位整數
    digits = "0123456789ABCDEF"
    value_str = value_str.upper().strip()
    result = 0
    for char in value_str:
        #尋找字元在digits中的索引位值
        val = -1
        for i in range(base):
            if digits[i] == char:
                val = i
                break
        if val == -1: raise ValueError(f"無效字元 {char}")
        result = result * base + val
    return result

def manual_from_decimal(n, base):
    #將10進位整數轉為N進位字串
    digits = "0123456789ABCDEF"
    result = ""
    temp = n
    while temp > 0:
        result = digits[temp % base] + result
        temp //= base
    return result

#建立圖形介面

bin_input = widgets.Text(description='二進位:', placeholder='例如: 1010')
dec_input = widgets.Text(description='十進位:', placeholder='例如: 255')
hex_input = widgets.Text(description='十六進位:', placeholder='例如: FF')
btn_convert = widgets.Button(description='執行轉換', button_style='info')
btn_clear = widgets.Button(description='清空', button_style='warning')
output = widgets.Output()

def on_convert_clicked(b):
    with output:
        clear_output()
        try:
            #偵測哪一欄有輸入
            if bin_input.value.strip():
                d = manual_to_decimal(bin_input.value, 2)
            elif dec_input.value.strip():
                #十進位字串轉整數
                d = 0
                for char in dec_input.value.strip():
                    d = d * 10 + (ord(char) - ord('0'))
            elif hex_input.value.strip():
                d = manual_to_decimal(hex_input.value, 16)
            else:
                print("請輸入數值！")
                return

            #更新結果到畫面上
            bin_input.value = manual_from_decimal(d, 2)
            dec_input.value = str(d)
            hex_input.value = manual_from_decimal(d, 16)
            print(f"轉換成功！(十進位值: {d})")

        except Exception as e:
            print(f"錯誤: {e}")

def on_clear_clicked(b):
    bin_input.value = ''
    dec_input.value = ''
    hex_input.value = ''
    with output: clear_output()

btn_convert.on_click(on_convert_clicked)
btn_clear.on_click(on_clear_clicked)

#顯示介面
display(widgets.VBox([bin_input, dec_input, hex_input,
                      widgets.HBox([btn_convert, btn_clear]),
                      output]))
