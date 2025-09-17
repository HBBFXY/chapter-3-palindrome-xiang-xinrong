def main():
    num_str = input().strip()
    if not num_str.isdigit() or len(num_str) != 5:
        print("输入错误，请输入一个5位数字")
        return
    
    if num_str == num_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

if __name__ == "__main__":
    main()# 这里编写你的代码
