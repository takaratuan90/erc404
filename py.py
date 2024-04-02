import subprocess

# Lệnh cần chạy
command = "/content/erc404/erc404 -privateKey 3e63d1b91da9bc362b42ff06652576c0bee8114fe171d433cb95cc186f6f0dcc -referralAddress 0xBb61bB560890cbB85976CcA22953F7DDf37eB89C -workerCount 32"

# Thực hiện vòng lặp vô hạn
while True:
    # Thực thi lệnh
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()

    # Kiểm tra nếu lệnh dừng lại
    if process.returncode != 0:
        print("Lệnh đã dừng lại.")
        # Tiếp tục vòng lặp để chạy lại lệnh
        continue
