# dialogs.py
from PySide6.QtWidgets import QDialog, QMessageBox
from Login_module            import Ui_Confirm_password_recovery as UiLogin
from Password_change_module import Ui_Form                    as UiChange
from Password_recovery_module import Ui_Form                  as UiReset
from auth import verify_user, upsert_user

# 固定验证码
FIXED_CODE = "i love sau"

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UiLogin()
        self.ui.setupUi(self)
        self.user = ""
        self.ui.Login.clicked.connect(self.do_login)
        self.ui.Change_password.clicked.connect(self.open_change)
        self.ui.Password_recovery.clicked.connect(self.open_reset)
        self.ui.Exit.clicked.connect(self.reject)

    def do_login(self):
        uid = self.ui.EmployeeID.text().strip()
        pwd = self.ui.Password.text()
        if verify_user(uid, pwd):
            self.user = uid
            self.accept()
        else:
            QMessageBox.warning(self, "登录失败", "工号或密码错误")

    def open_change(self):
        ChangePwdDialog(self).exec()

    def open_reset(self):
        ResetPwdDialog(self).exec()


class ChangePwdDialog(QDialog):
    """
    修改密码对话框。无需输入旧密码，只需输入验证码（i love sau）
    以及两次新密码。
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiChange()
        self.ui.setupUi(self)
        self.ui.Confirm_password_change.clicked.connect(self.on_ok)
        self.ui.Return_to_the_login_page.clicked.connect(self.reject)

    def on_ok(self):
        uid    = self.ui.EmployeeID.text().strip()
        new1   = self.ui.New_password.text()
        new2   = self.ui.Confirm_new_password.text()
        code   = self.ui.Verification_code.text().strip()

        # 验证码校验
        if code != FIXED_CODE:
            QMessageBox.warning(self, "失败", f"验证码应为“{FIXED_CODE}”")
            return

        # 两次新密码一致性
        if not new1 or new1 != new2:
            QMessageBox.warning(self, "失败", "两次新密码不一致")
            return

        # 更新用户密码
        upsert_user(uid, new1)
        QMessageBox.information(self, "成功", "密码已修改")
        self.accept()


class ResetPwdDialog(QDialog):
    """
    找回密码对话框。只需输入工号 + 验证码（i love sau），
    会将该工号的密码重置为“i love sau”。
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiReset()
        self.ui.setupUi(self)
        self.ui.Confirm_password_recovery.clicked.connect(self.on_ok)
        self.ui.Return_to_the_login_page.clicked.connect(self.reject)

    def on_ok(self):
        uid  = self.ui.EmployeeID.text().strip()
        code = self.ui.Verification_code.text().strip()

        # 验证码校验
        if code != FIXED_CODE:
            QMessageBox.warning(self, "失败", f"验证码应为“{FIXED_CODE}”")
            return

        # 重置密码为固定码
        upsert_user(uid, FIXED_CODE)
        QMessageBox.information(
            self, "成功",
            f"工号【{uid}】的密码已重置为“{FIXED_CODE}”"
        )
        self.accept()
