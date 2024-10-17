from hanzi_chaizi import HanziChaizi


def test_query():
    hc = HanziChaizi()
    result = hc.query("名")

    assert result == ["夕", "口"]
