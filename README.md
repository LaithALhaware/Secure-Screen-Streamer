# 🔒🖥️ Secure Screen Streamer

SecureScreenStreamer is a simple and secure remote desktop streaming application with built-in username and password authentication. It allows you to share your screen over a network while controlling access with login credentials. Perfect for quick and safe remote screen viewing! 👨‍💻👩‍💻


## ✨ Features

- 🔐 **Username & Password Authentication**  
- 📸 Real-time screen capture and streaming  
- 🚀 Low-latency JPEG compressed frames  
- 🖥️ Cross-platform support (Python + OpenCV)  
- ❌ Quit anytime by pressing 'q' in the viewer window  

## 🔧 Requirements
- 🐍 Python 3.x  
- 📦 OpenCV (`pip install opencv-python`)
- 📦 MSS (`pip install mss`)
- 📦 NumPy (`pip install numpy`)

  

## 🛠 Installation

- Open CMD 🖥️


| **Operating System** | **Steps**                                                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Windows** 💻        | 1. Press `Windows + R` to open the "Run" dialog box. <br> 2. Type `cmd` and hit `Enter`. <br> 3. The Command Prompt (CMD) will open. <br> Alternatively, you can search for "Command Prompt" in the Start menu and click to open it. 🔍 <br> 4. To navigate to the Desktop, type `cd %USERPROFILE%\Desktop` and hit `Enter`. 📂        |
| **Linux** 🐧          | 1. Press `Ctrl + Alt + T` to open the terminal. <br> 2. Alternatively, search for "Terminal" in your applications menu. 💨 <br> 3. To navigate to the Desktop, type `cd ~/Desktop` and hit `Enter`. 📂        |


- Clone the repository or download the project files to your local machine 📂  :
```bash
git clone https://github.com/LaithALhaware/Secure-Screen-Streamer.git
cd Secure-Screen-Streamer
```

- Install dependencies (if any):

```bash
pip install -r requirements.txt
```

## ▶️ Usage
- Start the server :
   ```bash
   python Server_Auth.py
   ```

- Client (run on the viewing computer) :
  ```bash
   python Server_Auth.py
   ```

   You will be prompted to enter:

   - 🌐 Server IP address 
   - 🔌 Server Port (default is 8888) 
   - 👤 Username `admin` or `laith` 
   - 🔑 Password `pass123` or `secure456` 



## 📝 License
This project is licensed under the **License**. See the [LICENSE.txt](LICENSE.txt) ⚖️ file for details.

---
## ❤️ Support This Project
If you find this project useful, consider supporting its development:

💰 Via PayPal: [[PayPal Link](https://www.paypal.com/ncp/payment/KC9EETJDVZQHG)]

Your support helps keep this project alive! 🚀🔥
