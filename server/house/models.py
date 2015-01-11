from django.db import models


class HouseMetrics(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    place = models.TextField(null=False, blank=False)
    temperature = models.FloatField(null=False, blank=False)
    tempertime = models.DateTimeField(null=False, blank=False)
    lon = models.FloatField(null=False, blank=False)
    lat = models.FloatField(null=False, blank=False)
    memo = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='house_metrics')

    class Meta:
        db_table = 'house_metrics'
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        保存時の処理
        """
        # 日付をDatetimeに変換
        super(HouseMetrics, self).save(*args, **kwargs)
        # limit the number of instances retained
        metrics = HouseMetrics.objects.all()
        if len(metrics) > 50000:
            metrics[0].delete()
