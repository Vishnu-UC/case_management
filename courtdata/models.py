from django.db import models


class MstPartyRepresentationType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_party_representation_type'
        verbose_name = "Party Representation Type"

    def __str__(self):
        return self.name


class MstPartyType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_party_type'
        verbose_name = "Party Type"

    def __str__(self):
        return self.name


class Attorney(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'attorney'
        verbose_name = "Attorney"

    def __str__(self):
        return self.name


class MstCaseTypeCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_case_type_category'
        verbose_name = "Case Type Category"

    def __str__(self):
        return self.name


class MstCaseTypeGroup(models.Model):
    mst_case_type_category = models.ForeignKey(MstCaseTypeCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_case_type_group'
        verbose_name = "Case Type Group"
        unique_together = ("mst_case_type_category", "name")

    def __str__(self):
        return self.name


class MstCaseType(models.Model):
    mst_case_type_group = models.ForeignKey(MstCaseTypeGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_case_type'
        verbose_name = "Case Type"
        unique_together = ("mst_case_type_group", "name")

    def __str__(self):
        return self.name


class MstCaseStatusCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_case_status_category'
        verbose_name = "Case Status Category"

    def __str__(self):
        return self.name


class MstCaseStatus(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_case_status'
        verbose_name = "Case Status"

    def __str__(self):
        return self.name


class MstJurisdiction(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_jurisdiction'
        verbose_name = "Jurisdiction"

    def __str__(self):
        return self.name


class MstCourthouse(models.Model):
    mst_jurisdiction = models.ForeignKey(MstJurisdiction, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'mst_courthouse'
        verbose_name = "Courthouse"
        unique_together = ("mst_jurisdiction", "name")

    def __str__(self):
        return self.name


class CourtCase(models.Model):
    case_key = models.CharField(max_length=400, unique=True)
    case_name = models.CharField(max_length=400)
    case_number = models.CharField(max_length=400)
    filing_date = models.DateField()
    mst_case_type = models.ForeignKey(MstCaseType, on_delete=models.CASCADE)
    mst_case_status = models.ForeignKey(MstCaseStatus, on_delete=models.CASCADE)
    mst_case_status_category = models.ForeignKey(MstCaseStatusCategory, on_delete=models.CASCADE)
    mst_courthouse = models.ForeignKey(MstCourthouse, on_delete=models.CASCADE)
    judge_name = models.CharField(max_length=400)
    created_date = models.DateTimeField()
    last_update_date = models.DateTimeField()

    class Meta:
        db_table = 'court_case'
        verbose_name = "Court Case"

    def __str__(self):
        return self.case_key


class Party(models.Model):
    court_case = models.ForeignKey(CourtCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mst_party_type = models.ForeignKey(MstPartyType, on_delete=models.CASCADE)
    mst_party_representation_type = models.ForeignKey(MstPartyRepresentationType, on_delete=models.CASCADE)
    attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)

    class Meta:
        db_table = 'party'
        verbose_name = "Party"

    def __str__(self):
        return self.name
