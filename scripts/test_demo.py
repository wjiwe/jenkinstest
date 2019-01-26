import allure


class TestDemo:

    @allure.step(title="登录测试流程")
    def test_01(self):
        allure.attach("登录", "输入用户名")
        print("helloworld!")
        assert 1

    def test_02(self):
        print("helloworld!")
        assert 0
