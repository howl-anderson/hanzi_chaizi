from hanzi_chaizi import HanziChaizi


class TestHanziChaizi:
    def setup_method(self):
        self.hc = HanziChaizi()

    def test_query_existing_char(self):
        result = self.hc.query("名")
        assert result == ["夕", "口"]

    def test_query_another_char(self):
        result = self.hc.query("明")
        assert result == ["日", "月"]

    def test_query_similar_structure(self):
        # 好 拆分为 女 和 子
        assert self.hc.query("好") == ["女", "子"]
        # 明 拆分为 日 和 月
        assert self.hc.query("明") == ["日", "月"]

    def test_query_nonexistent_char_returns_none(self):
        result = self.hc.query("xyz")
        assert result is None

    def test_query_nonexistent_char_with_default(self):
        result = self.hc.query("xyz", default=[])
        assert result == []

    def test_readme_examples(self):
        # 验证 README 中的示例
        assert self.hc.query("名") == ["夕", "口"]
