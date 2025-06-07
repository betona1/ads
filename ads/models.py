from django.db import models


class GmarketAdKeyword(models.Model):
    keyword = models.CharField("키워드", max_length=100)
    impression = models.IntegerField("노출수")
    click = models.IntegerField("클릭수")
    click_rate = models.FloatField("클릭률 (%)")
    avg_position = models.FloatField("평균노출순위")
    cpc = models.IntegerField("평균클릭비용")
    cost = models.IntegerField("총비용")
    purchase_count = models.IntegerField("구매수")
    purchase_amount = models.IntegerField("구매금액")
    conversion_rate = models.FloatField("전환율 (%)")
    roas = models.FloatField("광고수익률 (%)")
    market_id = models.CharField("지마켓아이디", max_length=50)
    ad_start_date = models.DateField("광고시작일")  # 수집 시작일
    created_at = models.DateTimeField("업로드일시", auto_now_add=True)

    class Meta:
        verbose_name = "지마켓 광고 키워드"
        verbose_name_plural = "지마켓 광고 키워드 리스트"
        db_table = "gmarket_ad_keywords"

    def __str__(self):
        return f"[{self.ad_start_date}] {self.keyword}"


class GmarketSimpleAdKeyword(models.Model):
    keyword = models.CharField("키워드", max_length=100)
    seller_name = models.CharField("사업자명", max_length=100)

    impression = models.IntegerField("노출수")
    click = models.IntegerField("클릭수")
    click_rate = models.FloatField("클릭률 (%)")

    avg_position_list = models.TextField("평균노출순위 목록")  # 예: "1.23|2.45"
    cpc_list = models.TextField("평균클릭비용 목록")  # 예: "120|140"

    cost = models.IntegerField("총비용")
    purchase_count = models.IntegerField("구매수")
    purchase_amount = models.IntegerField("구매금액")

    conversion_rate = models.FloatField("전환율 (%)")
    roas = models.FloatField("광고수익률 (%)")

    business_start_date = models.DateField("사업개시일", null=True, blank=True)
    ad_end_date = models.DateField("간편광고 종료일", null=True, blank=True)

    created_at = models.DateTimeField("등록일시", auto_now_add=True)

    class Meta:
        verbose_name = "지마켓 간편 광고 키워드"
        verbose_name_plural = "지마켓 간편 광고 키워드 리스트"
        db_table = "gmarket_simple_ad_keywords"
        unique_together = ("keyword", "seller_name")

    def __str__(self):
        return f"{self.seller_name} - {self.keyword}"
