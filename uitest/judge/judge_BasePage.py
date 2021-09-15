import pytest

from base.base_action import BaseAction


class Judge_Base_Page(BaseAction):

    def Judger_is_element_exist(self, element):
        """判断元素是否存在"""
        flag = True
        try:
            self.find_el(element)
            return flag
        except:
            flag = False
            return flag

    # 详细断言异常
    def test_zero_division_long(self):
        with pytest.raises(ZeroDivisionError) as excinfo:1/0
        # 断言异常类型 type
        assert excinfo.type == ZeroDivisionError
        # 断言异常 value 值
        assert "division by zero" in str(excinfo.value)