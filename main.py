# main.py
import sys
from PySide6.QtWidgets import QApplication
from db      import init_all_tables
from dialogs import LoginDialog
from main_window import MainWindow   # 这个 MainWindow 就是封装了 Interface_module.py 的 Ui_Form

def main():
    # 1) 初始化所有表（users + 4 张刀具表）
    init_all_tables()

    # 2) 启动 Qt 应用
    app = QApplication(sys.argv)

    # 3) 弹出登录对话框
    login = LoginDialog()
    if login.exec() == LoginDialog.Accepted:
        # 登录成功，login.user 中保存了工号
        # 直接打开主界面：Interface_module
        wnd = MainWindow(login.user)
        wnd.resize(1050, 900)
        wnd.show()
        sys.exit(app.exec())
    else:
        # 用户点击“退出”或登录失败
        sys.exit()

if __name__ == "__main__":
    main()
