from django.contrib import admin
from .models import GmarketAdKeyword, GmarketSimpleAdKeyword

@admin.register(GmarketAdKeyword)
class GmarketAdKeywordAdmin(admin.ModelAdmin):
    list_display = (
        'keyword',             # 키워드
        'impression',          # 노출수
        'click',               # 클릭수
        'click_rate',          # 클릭률
        'avg_position',        # 평균노출순위
        'cpc',                 # 평균클릭비용
        'cost',                # 총비용
        'purchase_count',      # 구매수
        'purchase_amount',     # 구매금액
        'conversion_rate',     # 전환율
        'roas',                # 광고수익률
        'market_id',           # 지마켓 ID
        'ad_start_date',       # 광고시작일
    )

    search_fields = ('keyword',)
    ordering = ('keyword','purchase_amount','impression','click')  # 기본 정렬: 키워드 오름차순
    list_per_page = 50

@admin.register(GmarketSimpleAdKeyword)
class GmarketSimpleAdKeywordAdmin(admin.ModelAdmin):
    list_display = (
        'keyword',               # 키워드
        'seller_name',           # 사업자명
        'impression',            # 노출수
        'click',                 # 클릭수
        'click_rate',            # 클릭률
        'cost',                  # 총비용
        'purchase_count',        # 구매수
        'purchase_amount',       # 구매금액
        'conversion_rate',       # 전환율
        'roas',                  # 광고수익률
        'business_start_date',   # 사업개시일
        'ad_end_date',           # 간편광고 종료일
    )

    search_fields = ('keyword',)
    ordering = ('keyword','purchase_amount','impression','click')  # 기본 정렬: 키워드 오름차순
    list_per_page = 50

    list_per_page = 50