# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountingAccount(models.Model):
    name = models.CharField(unique=True, max_length=60)
    current_balance = models.DecimalField(max_digits=16, decimal_places=2)
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    balance_updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Accounting_account'


class AccountingC24Bankaccount(models.Model):
    ac_num = models.CharField(max_length=20)
    branch = models.CharField(max_length=200)
    ifsc = models.CharField(max_length=15)
    ac_type = models.CharField(max_length=2)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    acc = models.ForeignKey(AccountingAccount, models.DO_NOTHING, unique=True, blank=True, null=True)
    bank = models.ForeignKey('GenericdataBank', models.DO_NOTHING)
    is_verified = models.BooleanField()
    verified_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    is_primary = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Accounting_c24bankaccount'


class AccountingCaregiverpayment(models.Model):
    payment_date = models.DateField()
    payment_by = models.CharField(max_length=3)
    amount = models.SmallIntegerField()
    payment_remarks = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounting_caregiverpayment'
        unique_together = (('cg', 'booking', 'payment_date', 'payment_by'),)


class AccountingCollectiondetails(models.Model):
    approve_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    bank = models.ForeignKey('GenericdataBank', models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey('AccountingCollections', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounting_collectiondetails'


class AccountingCollections(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    payment_to = models.CharField(max_length=4, blank=True, null=True)
    type = models.SmallIntegerField()
    payment_date = models.DateField()
    description = models.TextField()
    status = models.SmallIntegerField()
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, blank=True, null=True)
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey('BillingCollectioninvoices', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    transaction_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Accounting_collections'


class AccountingPayments(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    request_date = models.DateField()
    type = models.SmallIntegerField()
    description = models.TextField()
    process_date = models.DateField(blank=True, null=True)
    status = models.SmallIntegerField()
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    visit = models.ForeignKey('RequestbookingC24Visit', models.DO_NOTHING, blank=True, null=True)
    discount = models.ForeignKey('DiscountsDiscountmaster', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Accounting_payments'


class AccountingPosting(models.Model):
    posting_type = models.SmallIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    created = models.DateTimeField()
    account = models.ForeignKey(AccountingAccount, models.DO_NOTHING)
    trans = models.ForeignKey('AccountingTransaction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounting_posting'


class AccountingTransaction(models.Model):
    transaction_type = models.SmallIntegerField()
    particulars_value = models.CharField(max_length=25, blank=True, null=True)
    particulars_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    execution_time = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Accounting_transaction'


class AccountingVisitcpavalues(models.Model):
    charge_fee = models.FloatField()
    charge_equip_rent = models.SmallIntegerField()
    charge_travel_a = models.SmallIntegerField()
    charge_consumable_a = models.SmallIntegerField()
    charge_other_a = models.SmallIntegerField()
    pay_fee = models.FloatField()
    pay_travel_a = models.SmallIntegerField()
    pay_consumable_a = models.SmallIntegerField()
    pay_other_a = models.SmallIntegerField()
    penalty = models.SmallIntegerField()
    incentive = models.SmallIntegerField()
    discount = models.SmallIntegerField()
    caregiver_invoice = models.ForeignKey('BillingCaregiverinvoices', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    customer_invoice = models.ForeignKey('BillingCollectioninvoices', models.DO_NOTHING, blank=True, null=True)
    modified = models.DateTimeField()
    visit = models.ForeignKey('RequestbookingC24Visit', models.DO_NOTHING)
    discount_remarks = models.TextField(blank=True, null=True)
    incentive_remarks = models.TextField(blank=True, null=True)
    penalty_remarks = models.TextField(blank=True, null=True)
    discount_type = models.SmallIntegerField(blank=True, null=True)
    incentive_type = models.SmallIntegerField(blank=True, null=True)
    penalty_type = models.SmallIntegerField(blank=True, null=True)
    discount_code = models.ForeignKey('DiscountsDiscountmaster', models.DO_NOTHING, blank=True, null=True)
    caregiver_payout = models.ForeignKey('CaregiverfinancePayout', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Accounting_visitcpavalues'


class AllocationmanagerAllocationresponse(models.Model):
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    response_status = models.ForeignKey('AllocationmanagerAllocationresponsestatus', models.DO_NOTHING)
    searched = models.BooleanField()
    rating_response = models.ForeignKey('AllocationmanagerProviderratingresponse', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AllocationManager_allocationresponse'


class AllocationmanagerAllocationresponsecategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'AllocationManager_allocationresponsecategory'


class AllocationmanagerAllocationresponsestatus(models.Model):
    category = models.ForeignKey(AllocationmanagerAllocationresponsecategory, models.DO_NOTHING)
    response_type = models.ForeignKey('AllocationmanagerAllocationresponsetype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AllocationManager_allocationresponsestatus'


class AllocationmanagerAllocationresponsetype(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'AllocationManager_allocationresponsetype'


class AllocationmanagerBookingassignment(models.Model):
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    assign_to = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'AllocationManager_bookingassignment'


class AllocationmanagerBookingassignmenthistory(models.Model):
    remarks = models.TextField(blank=True, null=True)
    changes = models.CharField(max_length=150, blank=True, null=True)
    tstamp = models.DateTimeField()
    assign_to = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey(AllocationmanagerBookingassignment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AllocationManager_bookingassignmenthistory'


class AllocationmanagerBookingopeningtime(models.Model):
    open_time = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    open_by = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AllocationManager_bookingopeningtime'


class AllocationmanagerBookingparking(models.Model):
    park_till = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, unique=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AllocationManager_bookingparking'


class AllocationmanagerMatchfilter(models.Model):
    booking_field_name = models.CharField(max_length=100)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    provider_field_name = models.CharField(max_length=100)
    service = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AllocationManager_matchfilter'


class AllocationmanagerProviderbacklist(models.Model):
    remarks = models.TextField()
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    end_time = models.DateTimeField()
    start_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'AllocationManager_providerbacklist'


class AllocationmanagerProviderbufferqueueconfig(models.Model):
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'AllocationManager_providerbufferqueueconfig'


class AllocationmanagerProviderrating(models.Model):
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'AllocationManager_providerrating'


class AllocationmanagerProviderratingconfig(models.Model):
    service = models.CharField(max_length=2)
    rating_type = models.SmallIntegerField()
    min_range = models.IntegerField()
    max_range = models.IntegerField()
    rating = models.IntegerField()
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'AllocationManager_providerratingconfig'


class AllocationmanagerProviderratingresponse(models.Model):
    app = models.IntegerField()
    request_work = models.IntegerField()
    new_provider = models.IntegerField()
    no_show = models.IntegerField()
    location = models.IntegerField()
    language = models.IntegerField()
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    distance = models.IntegerField()
    no_communication = models.IntegerField()
    visit_completed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'AllocationManager_providerratingresponse'


class AllocationmanagerStaticfilter(models.Model):
    field_name = models.CharField(max_length=100, blank=True, null=True)
    field_value = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'AllocationManager_staticfilter'


class AppapiCxquestionmaster(models.Model):
    question = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    question_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'AppAPI_cxquestionmaster'


class AppapiCxquestionmasterOptions(models.Model):
    cxquestionmaster = models.ForeignKey(AppapiCxquestionmaster, models.DO_NOTHING)
    cxresponseoptions = models.ForeignKey('AppapiCxresponseoptions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AppAPI_cxquestionmaster_options'
        unique_together = (('cxquestionmaster', 'cxresponseoptions'),)


class AppapiCxquestionresponse(models.Model):
    text_response = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    question = models.ForeignKey(AppapiCxquestionmaster, models.DO_NOTHING)
    response = models.ForeignKey('AppapiCxresponseoptions', models.DO_NOTHING)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AppAPI_cxquestionresponse'


class AppapiCxresponseoptions(models.Model):
    value = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'AppAPI_cxresponseoptions'


class AvailabilityAskforworkmissedcall(models.Model):
    phone = models.CharField(max_length=128)
    no_of_times = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Availability_askforworkmissedcall'


class AvailabilityAvailabilityindex(models.Model):
    slot = models.BigIntegerField()
    available = models.NullBooleanField()
    created = models.DateTimeField()
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Availability_availabilityindex'


class AvailabilityAvailabilityprops(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'Availability_availabilityprops'


class AvailabilityProviderslot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Availability_providerslot'


class BatchprocessmodelBatchprocessentry(models.Model):
    call_time = models.DateTimeField()
    call_agent = models.ForeignKey('AuthUser', models.DO_NOTHING)
    call_params = models.CharField(max_length=200)
    call_process_tag = models.CharField(max_length=200)
    batch_task_id = models.CharField(max_length=200)
    batch_task_status = models.CharField(max_length=100)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'BatchProcessModel_batchprocessentry'


class BillingAdvancepayment(models.Model):
    start_date = models.DateField()
    no_of_visits = models.SmallIntegerField(blank=True, null=True)
    duration = models.SmallIntegerField(blank=True, null=True)
    price_negotiated = models.DecimalField(max_digits=16, decimal_places=2)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2)
    no_of_cg = models.SmallIntegerField(blank=True, null=True)
    service = models.CharField(max_length=2, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    discount_code = models.ForeignKey('DiscountsDiscountmaster', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Billing_advancepayment'


class BillingBookingratestandardization(models.Model):
    service = models.CharField(max_length=2)
    procedure = models.CharField(max_length=200, blank=True, null=True)
    duration = models.SmallIntegerField()
    no_of_cg = models.SmallIntegerField()
    price = models.FloatField()
    no_of_patient = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    category = models.ForeignKey('BillingBookingratestandardizationcategory', models.DO_NOTHING)
    region = models.ForeignKey('GeographyRegion', models.DO_NOTHING)
    short_description = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Billing_bookingratestandardization'


class BillingBookingratestandardizationcategory(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Billing_bookingratestandardizationcategory'


class BillingCaregiverinvoices(models.Model):
    invoice_date = models.DateField()
    total_visits = models.IntegerField()
    total_amount = models.DecimalField(max_digits=16, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    invoice_status = models.SmallIntegerField()
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    payment_received_date = models.DateField(blank=True, null=True)
    penalty = models.DecimalField(max_digits=16, decimal_places=2)
    invoice_name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Billing_caregiverinvoices'


class BillingCollectioninvoices(models.Model):
    invoice_date = models.DateField()
    total_visits = models.IntegerField()
    total_amount = models.DecimalField(max_digits=16, decimal_places=2)
    prev_balance = models.DecimalField(max_digits=16, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    invoice_status = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    payment_received_date = models.DateField(blank=True, null=True)
    discount = models.DecimalField(max_digits=16, decimal_places=2)
    invoice_name = models.TextField(blank=True, null=True)
    invoice_identifier = models.TextField(blank=True, null=True)
    bad_debt = models.DecimalField(max_digits=16, decimal_places=2)
    previous_invoice_list = models.CharField(max_length=200, blank=True, null=True)
    invoice_stage = models.SmallIntegerField(blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Billing_collectioninvoices'


class BillingInternalinvoice(models.Model):
    actual_payable = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    total_visits = models.IntegerField(blank=True, null=True)
    generation_date = models.DateField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, blank=True, null=True)
    receivables_trans = models.ForeignKey(AccountingTransaction, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Billing_internalinvoice'


class BillingLedgerdetail(models.Model):
    credit_balance = models.DecimalField(max_digits=16, decimal_places=2)
    debit_balance = models.DecimalField(max_digits=16, decimal_places=2)
    payment_type = models.SmallIntegerField(blank=True, null=True)
    created_by = models.DateTimeField()
    modified = models.DateTimeField()
    collection = models.ForeignKey(AccountingCollections, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    invoices = models.ForeignKey(BillingCollectioninvoices, models.DO_NOTHING, blank=True, null=True)
    refund = models.ForeignKey(AccountingPayments, models.DO_NOTHING, blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2)
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2)
    refund_type = models.SmallIntegerField(blank=True, null=True)
    invoice_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Billing_ledgerdetail'


class BillingPaymentreceipt(models.Model):
    receipt_date = models.DateField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    method = models.TextField(blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Billing_paymentreceipt'


class BroadcastengineBroadcastlog(models.Model):
    booking_cost = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'BroadcastEngine_broadcastlog'


class BroadcastengineBroadcastlogCaregivers(models.Model):
    broadcastlog = models.ForeignKey(BroadcastengineBroadcastlog, models.DO_NOTHING)
    c24provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'BroadcastEngine_broadcastlog_caregivers'
        unique_together = (('broadcastlog', 'c24provider'),)


class BroadcastengineConfig(models.Model):
    no_of_attempts = models.IntegerField()
    no_of_caregiver = models.IntegerField()
    minutes = models.IntegerField()
    service = models.CharField(max_length=2)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    region = models.ForeignKey('GeographyRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'BroadcastEngine_config'


class CampaignmanagerCampaign(models.Model):
    name = models.CharField(unique=True, max_length=100)
    objective = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    campaigntype = models.ForeignKey('CampaignmanagerCampaigntype', models.DO_NOTHING)
    discounttype = models.ForeignKey('CampaignmanagerDiscounttype', models.DO_NOTHING)
    host_prefix = models.CharField(max_length=255, blank=True, null=True)
    url_prefix = models.TextField(blank=True, null=True)
    fb_ad_id = models.CharField(max_length=50, blank=True, null=True)
    service = models.SmallIntegerField(blank=True, null=True)
    targeted_condition = models.CharField(max_length=100, blank=True, null=True)
    keywords = models.CharField(max_length=40, blank=True, null=True)
    city = models.ForeignKey('GeographyCity', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CampaignManager_campaign'


class CampaignmanagerCampaignDiscount(models.Model):
    campaign = models.ForeignKey(CampaignmanagerCampaign, models.DO_NOTHING)
    discountmaster = models.ForeignKey('DiscountsDiscountmaster', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CampaignManager_campaign_discount'
        unique_together = (('campaign', 'discountmaster'),)


class CampaignmanagerCampaignad(models.Model):
    ad_id = models.CharField(unique=True, max_length=50)
    campaign = models.ForeignKey(CampaignmanagerCampaign, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CampaignManager_campaignad'


class CampaignmanagerCampaigntype(models.Model):
    marketing_channel = models.SmallIntegerField()
    marketing_medium = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'CampaignManager_campaigntype'


class CampaignmanagerDiscounttype(models.Model):
    discount_parameter = models.SmallIntegerField()
    discount = models.DecimalField(max_digits=16, decimal_places=2)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'CampaignManager_discounttype'


class CaregiverfinanceAdvance(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    type = models.SmallIntegerField()
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=16, decimal_places=2)
    total_installment = models.SmallIntegerField()
    first_installment_date = models.DateField(blank=True, null=True)
    last_installment_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    emi_type = models.SmallIntegerField()
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_advance'


class CaregiverfinanceAdvanceledger(models.Model):
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2)
    credit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    debit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    advance = models.ForeignKey(CaregiverfinanceAdvance, models.DO_NOTHING)
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_advanceledger'


class CaregiverfinanceCaregiverpayoutcyclelog(models.Model):
    payout_date = models.DateTimeField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    run_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_caregiverpayoutcyclelog'


class CaregiverfinanceCgincentive(models.Model):
    quant_count = models.CharField(max_length=25, blank=True, null=True)
    break_count = models.CharField(max_length=25, blank=True, null=True)
    is_valid = models.BooleanField()
    has_achieved = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    incentive_desc = models.ForeignKey('CaregiverfinanceIncentivedesc', models.DO_NOTHING, blank=True, null=True)
    amount_achieved = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_cgincentive'


class CaregiverfinanceDeposit(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    type = models.SmallIntegerField()
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=16, decimal_places=2)
    total_installment = models.SmallIntegerField()
    first_installment_date = models.DateField(blank=True, null=True)
    last_installment_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    emi_type = models.SmallIntegerField()
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_deposit'


class CaregiverfinanceDepositledger(models.Model):
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2)
    credit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    debit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    deposit = models.ForeignKey(CaregiverfinanceDeposit, models.DO_NOTHING)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_depositledger'


class CaregiverfinanceFileexceptions(models.Model):
    exception_file_record = models.TextField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    file_name = models.ForeignKey('CaregiverfinanceFileuploadlog', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_fileexceptions'


class CaregiverfinanceFileuploadlog(models.Model):
    file_name = models.TextField(unique=True)
    upload_date = models.DateTimeField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    upload_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_fileuploadlog'


class CaregiverfinanceGeneralledger(models.Model):
    reference_code = models.SmallIntegerField()
    reference_pk = models.BigIntegerField()
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2)
    credit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    debit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_generalledger'


class CaregiverfinanceIncentive(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_incentive'


class CaregiverfinanceIncentivedesc(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    incentive_type = models.CharField(max_length=20)
    quant_unit = models.CharField(max_length=20)
    quant_measure = models.CharField(max_length=25, blank=True, null=True)
    warn_limit = models.CharField(max_length=25, blank=True, null=True)
    break_limit = models.CharField(max_length=25, blank=True, null=True)
    quant_logic = models.CharField(max_length=10)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    max_amount = models.DecimalField(max_digits=16, decimal_places=2)
    min_amount = models.DecimalField(max_digits=16, decimal_places=2)
    quant_min = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_incentivedesc'


class CaregiverfinancePayment(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    payment_mode = models.SmallIntegerField()
    account_no = models.TextField(blank=True, null=True)
    ifsc_code = models.TextField(blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    bank_name = models.ForeignKey('GenericdataBank', models.DO_NOTHING, blank=True, null=True)
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    payment_to = models.SmallIntegerField()
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_payment'


class CaregiverfinancePayout(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    total_visits = models.IntegerField()
    type = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    total_fees = models.DecimalField(max_digits=16, decimal_places=2)
    total_incentive = models.DecimalField(max_digits=16, decimal_places=2)
    total_penalty = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_date = models.DateField()
    caregiver_payout_id = models.TextField(blank=True, null=True)
    commission = models.DecimalField(max_digits=16, decimal_places=2)
    commission_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_payout'


class CaregiverfinancePenalty(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    type = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_penalty'


class CaregiverfinanceRefund(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    type = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_refund'


class CaregiverfinanceTds(models.Model):
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    created = models.DateTimeField()
    remarks = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'CaregiverFinance_tds'


class CompanyAllocation(models.Model):
    contact_num = models.CharField(max_length=128, blank=True, null=True)
    auth_user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'Company_allocation'


class CompanyCallcenter(models.Model):
    contact_num = models.CharField(max_length=128, blank=True, null=True)
    curr_stat = models.CharField(max_length=3)
    out_of_office_num = models.CharField(max_length=128, blank=True, null=True)
    will_take_calls_from_home = models.BooleanField()
    auth_user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)
    shift = models.SmallIntegerField()
    shift_end_time = models.TimeField(blank=True, null=True)
    shift_start_time = models.TimeField(blank=True, null=True)
    emp_typ = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'Company_callcenter'
        unique_together = (('contact_num', 'shift'),)


class CompanyCallcenterCallDirectionPreference(models.Model):
    callcenter = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING)
    calldirectionpreference = models.ForeignKey('CompanyCalldirectionpreference', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Company_callcenter_call_direction_preference'
        unique_together = (('callcenter', 'calldirectionpreference'),)


class CompanyCallcenterCallingRoles(models.Model):
    callcenter = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING)
    callingrole = models.ForeignKey('CompanyCallingrole', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Company_callcenter_calling_roles'
        unique_together = (('callcenter', 'callingrole'),)


class CompanyCallcenterCateringTo(models.Model):
    callcenter = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING)
    careservice = models.ForeignKey('GenericdataCareservice', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Company_callcenter_catering_to'
        unique_together = (('callcenter', 'careservice'),)


class CompanyCallcenterChannelPreference(models.Model):
    callcenter = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING)
    channelpreference = models.ForeignKey('CompanyChannelpreference', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Company_callcenter_channel_preference'
        unique_together = (('callcenter', 'channelpreference'),)


class CompanyCallcenterCities(models.Model):
    callcenter = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING)
    city = models.ForeignKey('GeographyCity', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Company_callcenter_cities'
        unique_together = (('callcenter', 'city'),)


class CompanyCallcenterServicePreference(models.Model):
    callcenter = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING)
    servicepreference = models.ForeignKey('CompanyServicepreference', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Company_callcenter_service_preference'
        unique_together = (('callcenter', 'servicepreference'),)


class CompanyCallcenteruseractionhistory(models.Model):
    action = models.CharField(max_length=3)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    ccuser = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING)
    end_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Company_callcenteruseractionhistory'


class CompanyCalldirectionpreference(models.Model):
    direction = models.SmallIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Company_calldirectionpreference'


class CompanyCallingrole(models.Model):
    srole = models.CharField(primary_key=True, max_length=3)
    role_full_name = models.CharField(unique=True, max_length=45)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    description = models.CharField(max_length=255)
    reciever_side = models.CharField(max_length=2)
    g2add = models.ForeignKey('AuthGroup', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Company_callingrole'


class CompanyChannelpreference(models.Model):
    channel = models.SmallIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Company_channelpreference'


class CompanyServicepreference(models.Model):
    service = models.SmallIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Company_servicepreference'


class CompanyTrainer(models.Model):
    contact_num = models.CharField(max_length=128, blank=True, null=True)
    auth_user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'Company_trainer'


class ComplaintsComplaincontext(models.Model):
    meant_for = models.SmallIntegerField()
    complain_type = models.CharField(max_length=10)
    complain_by = models.SmallIntegerField()
    complain_for = models.SmallIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Complaints_complaincontext'


class ComplaintsDailycomplaints(models.Model):
    type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    context = models.ForeignKey(ComplaintsComplaincontext, models.DO_NOTHING)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Complaints_dailycomplaints'


class ComplaintsFaq(models.Model):
    question = models.CharField(max_length=800)
    answer = models.TextField(blank=True, null=True)
    priority = models.IntegerField()
    is_active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    context = models.ForeignKey('ComplaintsFaqcontext', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Complaints_faq'


class ComplaintsFaqcontext(models.Model):
    meant_for = models.SmallIntegerField()
    faq_type = models.CharField(max_length=10)
    faq_for = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Complaints_faqcontext'


class ContentBlogcategory(models.Model):
    name = models.CharField(max_length=60)
    keywords = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    what_it_means = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Content_blogcategory'


class ContentCarelisticle(models.Model):
    name = models.CharField(max_length=120)
    short_descr = models.CharField(max_length=155)
    img = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()
    priority = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100)
    credits = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    is_live = models.BooleanField()
    meta_description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Content_carelisticle'


class ContentCarelisticleCategories(models.Model):
    carelisticle = models.ForeignKey(ContentCarelisticle, models.DO_NOTHING)
    blogcategory = models.ForeignKey(ContentBlogcategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Content_carelisticle_categories'
        unique_together = (('carelisticle', 'blogcategory'),)


class ContentHealthtip(models.Model):
    tip = models.TextField()
    ttype = models.SmallIntegerField()
    sent_date = models.DateField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Content_healthtip'


class ContentListiclesection(models.Model):
    subheading = models.CharField(max_length=150)
    image = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    listicle = models.ForeignKey(ContentCarelisticle, models.DO_NOTHING)
    modified = models.DateTimeField()
    order_on_page = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'Content_listiclesection'
        unique_together = (('listicle', 'order_on_page'),)


class DashboardAffiliate(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)
    releationship_manager = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    lead_type = models.SmallIntegerField()
    type_of_partnership = models.SmallIntegerField()
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    from_campaign = models.ForeignKey(CampaignmanagerCampaign, models.DO_NOTHING, blank=True, null=True)
    phnum = models.ForeignKey('InteractionmanagerPhonenumber', models.DO_NOTHING)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dashboard_affiliate'


class DashboardAffiliateservice(models.Model):
    service = models.CharField(max_length=5)
    total_number_of_lead = models.IntegerField(blank=True, null=True)
    cost_per_lead = models.IntegerField(blank=True, null=True)
    keywords_specified = models.CharField(max_length=1500, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    run_rate_estimated = models.IntegerField(blank=True, null=True)
    cost_per_conversion = models.IntegerField(blank=True, null=True)
    revenue_sharing = models.IntegerField(blank=True, null=True)
    cost_per_impression = models.IntegerField(blank=True, null=True)
    cost_per_click = models.IntegerField(blank=True, null=True)
    affiliate = models.ForeignKey(DashboardAffiliate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Dashboard_affiliateservice'


class DashboardCallactivity(models.Model):
    customer_activity = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField()
    active = models.BooleanField()
    parameter = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Dashboard_callactivity'


class DashboardCustomercallactivitylog(models.Model):
    status = models.CharField(max_length=20, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    call_activity = models.ForeignKey(DashboardCallactivity, models.DO_NOTHING)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING)
    updated_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dashboard_customercallactivitylog'


class DashboardFrequentyaskedquestions(models.Model):
    module = models.SmallIntegerField()
    question = models.TextField()
    description = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Dashboard_frequentyaskedquestions'


class DevicemanagerAppinstall(models.Model):
    registration_token = models.CharField(max_length=255, blank=True, null=True)
    opened_count = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    app = models.ForeignKey('DevicemanagerCareapp', models.DO_NOTHING)
    device = models.ForeignKey('DevicemanagerDevice', models.DO_NOTHING)
    care_user = models.ForeignKey('UsermanagementCareuser', models.DO_NOTHING, blank=True, null=True)
    last_ping = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DeviceManager_appinstall'
        unique_together = (('device', 'app'),)


class DevicemanagerCareapp(models.Model):
    package_name = models.CharField(max_length=255)
    version = models.CharField(max_length=60)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'DeviceManager_careapp'


class DevicemanagerDevice(models.Model):
    device_id = models.CharField(unique=True, max_length=80)
    operating_system = models.IntegerField()
    registration_token = models.CharField(max_length=255, blank=True, null=True)
    is_test = models.BooleanField()
    os_version = models.CharField(max_length=12, blank=True, null=True)
    app_version = models.CharField(max_length=60, blank=True, null=True)
    last_latitude = models.DecimalField(max_digits=22, decimal_places=18, blank=True, null=True)
    last_longitude = models.DecimalField(max_digits=22, decimal_places=18, blank=True, null=True)
    app_opened_count = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    care_user = models.ForeignKey('UsermanagementCareuser', models.DO_NOTHING, blank=True, null=True)
    p_registration_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DeviceManager_device'


class DevicemanagerGcmcall(models.Model):
    call_duration = models.CharField(max_length=30, blank=True, null=True)
    call_type = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    start_time = models.CharField(max_length=30, blank=True, null=True)
    end_time = models.CharField(max_length=30, blank=True, null=True)
    from_number = models.CharField(max_length=30, blank=True, null=True)
    to_number = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DeviceManager_gcmcall'


class DevicemanagerGcmmessage(models.Model):
    sms = models.CharField(max_length=250, blank=True, null=True)
    smstime = models.CharField(db_column='smsTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=30, blank=True, null=True)
    from_number = models.CharField(max_length=30, blank=True, null=True)
    to_number = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DeviceManager_gcmmessage'


class DevicemanagerLocationping(models.Model):
    identifier = models.CharField(max_length=200, blank=True, null=True)
    location = models.TextField()  # This field type is a guess.
    battery = models.SmallIntegerField(blank=True, null=True)
    reported = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    careuser = models.ForeignKey('UsermanagementCareuser', models.DO_NOTHING, blank=True, null=True)
    device = models.ForeignKey(DevicemanagerDevice, models.DO_NOTHING, blank=True, null=True)
    accuracy = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    bearing = models.FloatField(blank=True, null=True)
    location_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DeviceManager_locationping'


class DevicemanagerNotification(models.Model):
    nid = models.CharField(primary_key=True, max_length=100)
    typ = models.IntegerField()
    extra_info = models.TextField(blank=True, null=True)
    sender_string = models.CharField(max_length=80, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    opened_count = models.IntegerField()
    delivered_count = models.IntegerField()
    landing = models.CharField(max_length=120, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    admin_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    expired_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DeviceManager_notification'


class DevicemanagerNotificationToDevices(models.Model):
    notification = models.ForeignKey(DevicemanagerNotification, models.DO_NOTHING)
    device = models.ForeignKey(DevicemanagerDevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DeviceManager_notification_to_devices'
        unique_together = (('notification', 'device'),)


class DevicemanagerProviderphone(models.Model):
    imei = models.CharField(unique=True, max_length=30)
    sim = models.CharField(unique=True, max_length=50, blank=True, null=True)
    battery = models.SmallIntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    created = models.DateTimeField()
    modified = models.DateTimeField()
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    phone = models.ForeignKey('InteractionmanagerPhonenumber', models.DO_NOTHING, blank=True, null=True)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'DeviceManager_providerphone'


class DiscountsDiscountmaster(models.Model):
    code = models.CharField(unique=True, max_length=10)
    service = models.CharField(max_length=45)
    description = models.TextField()
    discount_type = models.SmallIntegerField()
    discount_parameter = models.SmallIntegerField()
    discount_value = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    minimum_visits = models.SmallIntegerField()
    new_customer = models.BooleanField()
    referral_flag = models.BooleanField()
    referral_type = models.SmallIntegerField(blank=True, null=True)
    referral_parameter = models.SmallIntegerField(blank=True, null=True)
    referral_value = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    max_amount = models.DecimalField(max_digits=8, decimal_places=2)
    advance_flag = models.BooleanField()
    terms = models.TextField(blank=True, null=True)
    discount_scope = models.SmallIntegerField(blank=True, null=True)
    use_multiple = models.BooleanField()
    visit_number_discount = models.DecimalField(max_digits=8, decimal_places=2)
    lead_type = models.CharField(max_length=71, blank=True, null=True)
    duration = models.CharField(max_length=7, blank=True, null=True)
    max_discounts_per_month = models.SmallIntegerField(blank=True, null=True)
    maximum_visits = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Discounts_discountmaster'


class DiscountsDiscountmasterApplicableRegion(models.Model):
    discountmaster = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING)
    region = models.ForeignKey('GeographyRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Discounts_discountmaster_applicable_region'
        unique_together = (('discountmaster', 'region'),)


class DiscountsDiscountmasterTeam(models.Model):
    discountmaster = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Discounts_discountmaster_team'
        unique_together = (('discountmaster', 'group'),)


class DiscountsDiscountprocesslog(models.Model):
    process_flag = models.BooleanField()
    process_start_date = models.DateField()
    processed_date = models.DateField(blank=True, null=True)
    process_text = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    discount_code = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING)
    remarks = models.TextField(blank=True, null=True)
    validity = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Discounts_discountprocesslog'


class FeedbackAttribute(models.Model):
    attribute_type = models.SmallIntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    enabled = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Feedback_attribute'


class FeedbackCaregiverfeedbackrecord(models.Model):
    score = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, blank=True, null=True)
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    feedback_log = models.ForeignKey('FeedbackFeedbacklog', models.DO_NOTHING)
    question = models.ForeignKey('FeedbackQuestiontext', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Feedback_caregiverfeedbackrecord'


class FeedbackCustomerfeedbackrecord(models.Model):
    score = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, blank=True, null=True)
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING)
    feedback_log = models.ForeignKey('FeedbackFeedbacklog', models.DO_NOTHING)
    question = models.ForeignKey('FeedbackQuestiontext', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Feedback_customerfeedbackrecord'


class FeedbackFeedbacklog(models.Model):
    feedback_date = models.DateField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    feedback_survey = models.ForeignKey('FeedbackFeedbacksurvey', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Feedback_feedbacklog'


class FeedbackFeedbacknotes(models.Model):
    remarks = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    feedback_log = models.ForeignKey(FeedbackFeedbacklog, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Feedback_feedbacknotes'


class FeedbackFeedbackrecord(models.Model):
    score = models.SmallIntegerField()
    scale = models.SmallIntegerField()
    date = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    question = models.ForeignKey('FeedbackQuestion', models.DO_NOTHING)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Feedback_feedbackrecord'


class FeedbackFeedbacksurvey(models.Model):
    name = models.TextField()
    enabled = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Feedback_feedbacksurvey'


class FeedbackQuestion(models.Model):
    text = models.CharField(max_length=800)
    meant_for = models.SmallIntegerField()
    scale = models.SmallIntegerField()
    scale_display = models.CharField(max_length=6, blank=True, null=True)
    negative = models.BooleanField()
    enabled = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    base = models.ForeignKey('FeedbackQuestionbase', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Feedback_question'


class FeedbackQuestionbase(models.Model):
    text = models.CharField(max_length=400)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    attr_judged = models.ForeignKey(FeedbackAttribute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Feedback_questionbase'


class FeedbackQuestiontext(models.Model):
    text = models.CharField(max_length=800)
    meant_for = models.SmallIntegerField()
    scale = models.SmallIntegerField()
    negative = models.BooleanField()
    enabled = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    attribute = models.ForeignKey(FeedbackAttribute, models.DO_NOTHING)
    survey = models.ForeignKey(FeedbackFeedbacksurvey, models.DO_NOTHING)
    option_type = models.SmallIntegerField()
    feedback_day = models.SmallIntegerField(blank=True, null=True)
    scale_to_display = models.ForeignKey('FeedbackScaledisplay', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Feedback_questiontext'


class FeedbackScaledisplay(models.Model):
    options = models.TextField()
    sub_options = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Feedback_scaledisplay'


class FeedbackServiceattribute(models.Model):
    significance = models.SmallIntegerField()
    critical = models.BooleanField()
    attribute = models.ForeignKey(FeedbackAttribute, models.DO_NOTHING)
    service = models.ForeignKey('GenericdataCareservice', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Feedback_serviceattribute'
        unique_together = (('attribute', 'service'),)


class FollowupEvent(models.Model):
    event = models.CharField(max_length=10)
    event_type = models.CharField(max_length=10, blank=True, null=True)
    event_data = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10)
    status_reason = models.CharField(max_length=10, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    agent = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Followup_event'


class FollowupEventlog(models.Model):
    status = models.CharField(max_length=10)
    status_reason = models.CharField(max_length=10, blank=True, null=True)
    tstamp = models.DateTimeField()
    agent = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(FollowupEvent, models.DO_NOTHING)
    changes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Followup_eventlog'


class FollowupEventtrack(models.Model):
    open_json = models.TextField(blank=True, null=True)
    close_json = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    agent = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Followup_eventtrack'


class FollowupMaster(models.Model):
    status = models.SmallIntegerField()
    reminder_date = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    agent = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'Followup_master'


class FollowupMasterlog(models.Model):
    reminder_date = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField()
    agent = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    master = models.ForeignKey(FollowupMaster, models.DO_NOTHING)
    changes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Followup_masterlog'


class GenericdataBank(models.Model):
    name = models.CharField(unique=True, max_length=60)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GenericData_bank'


class GenericdataCareservice(models.Model):
    internal_name = models.CharField(unique=True, max_length=45)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    short = models.CharField(primary_key=True, max_length=3)
    customer_name = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'GenericData_careservice'


class GenericdataLanguage(models.Model):
    name = models.CharField(unique=True, max_length=40)
    modified = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GenericData_language'


class GenericdataServicesurestrictions(models.Model):
    price_min = models.SmallIntegerField()
    price_max = models.SmallIntegerField()
    max_multiple = models.SmallIntegerField(blank=True, null=True)
    service = models.ForeignKey(GenericdataCareservice, models.DO_NOTHING)
    unit = models.ForeignKey('GenericdataServiceunit', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'GenericData_servicesurestrictions'
        unique_together = (('unit', 'service'),)


class GenericdataServiceunit(models.Model):
    num_hours = models.SmallIntegerField(blank=True, null=True)
    earliest_start = models.SmallIntegerField()
    latest_end = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GenericData_serviceunit'


class GeographyCareaddress(models.Model):
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_modified = models.BooleanField()
    google_vicinity = models.CharField(max_length=400, blank=True, null=True)
    google_est_types = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    google_phnum = models.CharField(max_length=20, blank=True, null=True)
    google_place_id = models.CharField(max_length=40, blank=True, null=True)
    all_google_addr_txt = models.TextField(blank=True, null=True)
    aliases = models.CharField(max_length=400, blank=True, null=True)
    last_update_time = models.DateTimeField()
    some_identifier = models.CharField(unique=True, max_length=250, blank=True, null=True)
    create_time = models.DateTimeField()
    accuracy = models.SmallIntegerField()
    city = models.ForeignKey('GeographyCity', models.DO_NOTHING, blank=True, null=True)
    cust_landmark = models.CharField(max_length=100, blank=True, null=True)
    cust_precise = models.CharField(max_length=100, blank=True, null=True)
    g_address_lines = models.TextField(blank=True, null=True)
    g_locality = models.CharField(max_length=100, blank=True, null=True)
    center = models.TextField(blank=True, null=True)  # This field type is a guess.
    address_tag = models.SmallIntegerField(blank=True, null=True)
    address_2 = models.TextField(blank=True, null=True)
    pin_code = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField()
    nickname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Geography_careaddress'


class GeographyCity(models.Model):
    name = models.CharField(unique=True, max_length=40)
    modified = models.DateTimeField()
    created = models.DateTimeField()
    region = models.ForeignKey('GeographyRegion', models.DO_NOTHING, blank=True, null=True)
    center = models.TextField(blank=True, null=True)  # This field type is a guess.
    poly = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Geography_city'


class GeographyLocality(models.Model):
    name = models.CharField(unique=True, max_length=50)
    create_time = models.DateTimeField()
    city = models.ForeignKey(GeographyCity, models.DO_NOTHING, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    aliases = models.CharField(max_length=400, blank=True, null=True)
    all_google_addr_txt = models.TextField(blank=True, null=True)
    google_est_types = models.CharField(max_length=200, blank=True, null=True)
    google_phnum = models.CharField(max_length=20, blank=True, null=True)
    google_place_id = models.CharField(max_length=40, blank=True, null=True)
    google_vicinity = models.CharField(max_length=400, blank=True, null=True)
    is_modified = models.BooleanField()
    last_update_time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()
    website = models.CharField(max_length=200, blank=True, null=True)
    is_micro_loc = models.BooleanField()
    center = models.TextField(blank=True, null=True)  # This field type is a guess.
    loc_name = models.CharField(max_length=50, blank=True, null=True)
    poly = models.TextField(blank=True, null=True)  # This field type is a guess.
    address_2 = models.TextField(blank=True, null=True)
    pin_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Geography_locality'


class GeographyLocalitysamplepoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    center = models.TextField(blank=True, null=True)  # This field type is a guess.
    formatted_address = models.TextField(blank=True, null=True)
    place_id = models.CharField(unique=True, max_length=50)
    colloquial_area = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    premise = models.CharField(max_length=50, blank=True, null=True)
    subpremise = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=50, blank=True, null=True)
    sublocality_level_5 = models.CharField(max_length=50, blank=True, null=True)
    sublocality_level_4 = models.CharField(max_length=50, blank=True, null=True)
    sublocality_level_3 = models.CharField(max_length=50, blank=True, null=True)
    sublocality_level_2 = models.CharField(max_length=50, blank=True, null=True)
    sublocality_level_1 = models.CharField(max_length=50, blank=True, null=True)
    administrative_area_level_5 = models.CharField(max_length=50, blank=True, null=True)
    administrative_area_level_4 = models.CharField(max_length=50, blank=True, null=True)
    administrative_area_level_3 = models.CharField(max_length=50, blank=True, null=True)
    administrative_area_level_2 = models.CharField(max_length=50, blank=True, null=True)
    administrative_area_level_1 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    tree_node = models.ForeignKey('GeographyLocalitytreenode', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Geography_localitysamplepoint'


class GeographyLocalitytag(models.Model):
    tag_name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    hex_color = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'Geography_localitytag'


class GeographyLocalitytagLocalities(models.Model):
    localitytag = models.ForeignKey(GeographyLocalitytag, models.DO_NOTHING)
    locality = models.ForeignKey(GeographyLocality, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Geography_localitytag_localities'
        unique_together = (('localitytag', 'locality'),)


class GeographyLocalitytreenode(models.Model):
    field_left = models.IntegerField(db_column='_left')  # Field renamed because it started with '_'.
    field_right = models.IntegerField(db_column='_right')  # Field renamed because it started with '_'.
    field_depth = models.IntegerField(db_column='_depth')  # Field renamed because it started with '_'.
    field_deleting = models.BooleanField(db_column='_deleting')  # Field renamed because it started with '_'.
    name = models.CharField(max_length=40)
    tag = models.SmallIntegerField(blank=True, null=True)
    field_tree_id = models.CharField(db_column='_tree_id', max_length=36)  # Field renamed because it started with '_'.
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent_id', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'Geography_localitytreenode'
        unique_together = (('tag', 'name', 'field_parent'),)


class GeographyLocationeta(models.Model):
    originstr = models.CharField(max_length=200)
    destinationstr = models.CharField(max_length=200)
    shift = models.CharField(max_length=5)
    seconds = models.IntegerField()
    meters = models.IntegerField()
    transfers = models.IntegerField()
    p2pdistance = models.FloatField()
    destination = models.ForeignKey(GeographyLocality, models.DO_NOTHING)
    origin = models.ForeignKey(GeographyLocality, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Geography_locationeta'


class GeographyMedicalfacility(models.Model):
    name = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=2)
    address = models.ForeignKey(GeographyCareaddress, models.DO_NOTHING, unique=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    beds = models.SmallIntegerField(blank=True, null=True)
    staff = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Geography_medicalfacility'


class GeographyPincodelist(models.Model):
    office_name = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=6)
    office_type = models.CharField(max_length=50, blank=True, null=True)
    delivery_status = models.CharField(max_length=50, blank=True, null=True)
    division_name = models.CharField(max_length=50, blank=True, null=True)
    region_name = models.CharField(max_length=50, blank=True, null=True)
    circle_name = models.CharField(max_length=50, blank=True, null=True)
    taluk = models.CharField(max_length=50, blank=True, null=True)
    district_name = models.CharField(max_length=50, blank=True, null=True)
    state_name = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    related_sub_office = models.CharField(max_length=50, blank=True, null=True)
    related_head_office = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Geography_pincodelist'


class GeographyRegion(models.Model):
    name = models.CharField(unique=True, max_length=40)
    modified = models.DateTimeField()
    created = models.DateTimeField()
    poly = models.TextField(blank=True, null=True)  # This field type is a guess.
    center = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Geography_region'


class GeographyServicelocalitygroup(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Geography_servicelocalitygroup'


class GeographyServicelocalitygroupLocalities(models.Model):
    servicelocalitygroup = models.ForeignKey(GeographyServicelocalitygroup, models.DO_NOTHING)
    servicelocality = models.ForeignKey(GeographyLocality, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Geography_servicelocalitygroup_localities'
        unique_together = (('servicelocalitygroup', 'servicelocality'),)


class HypertrackEventlog(models.Model):
    event_id = models.UUIDField(unique=True)
    typ = models.CharField(max_length=120)
    json_text = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Hypertrack_eventlog'


class IvrIvr(models.Model):
    name = models.CharField(unique=True, max_length=60)
    app_id = models.IntegerField()
    phn_num = models.CharField(max_length=128)
    caller_id = models.CharField(max_length=128)
    description = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'IVR_ivr'


class IvrIvrobjective(models.Model):
    name = models.CharField(unique=True, max_length=100)
    desc = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    ivr = models.ForeignKey(IvrIvr, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'IVR_ivrobjective'


class IvrIvrrecord(models.Model):
    call_sid = models.CharField(unique=True, max_length=50)
    reply = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    object_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    phn_num = models.ForeignKey('InteractionmanagerPhonenumber', models.DO_NOTHING)
    ivr_objective = models.ForeignKey(IvrIvrobjective, models.DO_NOTHING, blank=True, null=True)
    try_counter = models.IntegerField(blank=True, null=True)
    todo = models.IntegerField(blank=True, null=True)
    done_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IVR_ivrrecord'


class IvrIvrrecordlog(models.Model):
    call_sid = models.CharField(max_length=50)
    reply = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    tstamp = models.DateTimeField()
    changes = models.CharField(max_length=150, blank=True, null=True)
    ivr_record = models.ForeignKey(IvrIvrrecord, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'IVR_ivrrecordlog'


class InteractionmanagerCalldisposition(models.Model):
    comments = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    call_disposition_type = models.ForeignKey('InteractionmanagerCalldispositiontype', models.DO_NOTHING, blank=True, null=True)
    callrecord = models.ForeignKey('InteractionmanagerCallrecord', models.DO_NOTHING)
    category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InteractionManager_calldisposition'


class InteractionmanagerCalldispositiontype(models.Model):
    name = models.CharField(unique=True, max_length=100)
    desc = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InteractionManager_calldispositiontype'


class InteractionmanagerCallrecord(models.Model):
    queued_at = models.DateTimeField()
    phnum = models.ForeignKey('InteractionmanagerPhonenumber', models.DO_NOTHING)
    call_sid = models.CharField(unique=True, max_length=40)
    call_type = models.SmallIntegerField()
    caller_id = models.CharField(max_length=15)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    recording_url = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    ccuser = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    phonenumber_sid = models.CharField(max_length=128, blank=True, null=True)
    price = models.CharField(max_length=15, blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    ccuser_role = models.ForeignKey(CompanyCallingrole, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InteractionManager_callrecord'


class InteractionmanagerEmailrecord(models.Model):
    queued_at = models.DateTimeField()
    data_json = models.TextField(blank=True, null=True)
    retry_counter = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    ccuser = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    phnum = models.ForeignKey('InteractionmanagerPhonenumber', models.DO_NOTHING)
    template = models.ForeignKey('InteractionmanagerEmailtemplate', models.DO_NOTHING)
    email = models.CharField(max_length=254, blank=True, null=True)
    reference_id = models.TextField(blank=True, null=True)
    reject_reason = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InteractionManager_emailrecord'


class InteractionmanagerEmailtemplate(models.Model):
    name = models.CharField(max_length=60)
    email_type = models.SmallIntegerField()
    automated = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    active = models.BooleanField()
    email_paragraph_1 = models.TextField(blank=True, null=True)
    email_paragraph_2 = models.TextField(blank=True, null=True)
    email_paragraph_3 = models.TextField(blank=True, null=True)
    email_paragraph_4 = models.TextField(blank=True, null=True)
    email_subject = models.CharField(max_length=100, blank=True, null=True)
    mandrill_template_name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'InteractionManager_emailtemplate'
        unique_together = (('name', 'active'),)


class InteractionmanagerExophone(models.Model):
    phone = models.CharField(unique=True, max_length=128)
    medium = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    city = models.ForeignKey(GeographyCity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'InteractionManager_exophone'


class InteractionmanagerExophoneDiscount(models.Model):
    exophone = models.ForeignKey(InteractionmanagerExophone, models.DO_NOTHING)
    discountmaster = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'InteractionManager_exophone_discount'
        unique_together = (('exophone', 'discountmaster'),)


class InteractionmanagerIvr(models.Model):
    name = models.CharField(unique=True, max_length=60)
    phn_num = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'InteractionManager_ivr'


class InteractionmanagerIvrrecord(models.Model):
    call_sid = models.CharField(unique=True, max_length=40)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    ivr = models.ForeignKey(InteractionmanagerIvr, models.DO_NOTHING)
    reply = models.SmallIntegerField(blank=True, null=True)
    visit = models.ForeignKey('RequestbookingC24Visit', models.DO_NOTHING)
    confirmation_type = models.SmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'InteractionManager_ivrrecord'


class InteractionmanagerMissedcallsmsrecord(models.Model):
    phn_num = models.CharField(max_length=128)
    status = models.CharField(max_length=40)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    visit = models.ForeignKey('RequestbookingC24Visit', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'InteractionManager_missedcallsmsrecord'


class InteractionmanagerMissedcgcallrecord(models.Model):
    phone_num_text = models.CharField(max_length=40)
    status = models.SmallIntegerField()
    call_active = models.BooleanField()
    no_of_attempts = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    last_attempt_by = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InteractionManager_missedcgcallrecord'


class InteractionmanagerOtpverification(models.Model):
    is_verified = models.BooleanField()
    otp = models.SmallIntegerField(blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    phone = models.ForeignKey('InteractionmanagerPhonenumber', models.DO_NOTHING, unique=True)
    no_of_attempts_to_verify = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'InteractionManager_otpverification'


class InteractionmanagerPhonenumber(models.Model):
    phnum = models.CharField(unique=True, max_length=128)
    is_dnd = models.NullBooleanField(db_column='is_DND')  # Field name made lowercase.
    curr_stat = models.SmallIntegerField(blank=True, null=True)
    curr_stat_expiry = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    verified = models.BooleanField()
    banned = models.BooleanField()
    banned_remarks = models.TextField(blank=True, null=True)
    disable_sms = models.BooleanField()
    profile = models.ForeignKey('UsermanagementProfile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InteractionManager_phonenumber'


class InteractionmanagerSmsprovider(models.Model):
    name = models.CharField(unique=True, max_length=50)
    key = models.CharField(unique=True, max_length=10)
    priority_order = models.IntegerField(unique=True)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'InteractionManager_smsprovider'


class InteractionmanagerSmsrecord(models.Model):
    queued_at = models.DateTimeField()
    phnum = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING)
    template = models.ForeignKey('InteractionmanagerSmstemplate', models.DO_NOTHING)
    sms_sid = models.CharField(unique=True, max_length=40)
    status = models.CharField(max_length=40, blank=True, null=True)
    sent_or_failed_at = models.DateTimeField(blank=True, null=True)
    data_json = models.TextField(blank=True, null=True)
    retry_counter = models.SmallIntegerField()
    smsprovider = models.ForeignKey(InteractionmanagerSmsprovider, models.DO_NOTHING, db_column='SMSProvider_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InteractionManager_smsrecord'


class InteractionmanagerSmstemplate(models.Model):
    name = models.CharField(max_length=60)
    stype = models.SmallIntegerField()
    template_text = models.TextField()
    next_send_after_minutes = models.IntegerField()
    can_be_sent_during_night = models.BooleanField()
    modified = models.DateTimeField()
    approved_on = models.DateField()
    on_demand = models.BooleanField()
    is_english = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'InteractionManager_smstemplate'


class LeadmanagerJoinusrequest(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    email = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeadManager_joinusrequest'


class LeadmanagerLead(models.Model):
    service = models.SmallIntegerField()
    lead_type = models.SmallIntegerField()
    cust_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    extra_props = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    linked2customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    lead_quantifier = models.CharField(max_length=255, blank=True, null=True)
    lstat = models.SmallIntegerField(blank=True, null=True)
    next_contact = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    reason_for_not_close = models.CharField(max_length=10, blank=True, null=True)
    modified = models.DateTimeField()
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    consider_as_premium = models.BooleanField()
    from_campaign = models.ForeignKey(CampaignmanagerCampaign, models.DO_NOTHING, blank=True, null=True)
    assigned_to = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    opened = models.BooleanField()
    c24offered_price = models.FloatField(blank=True, null=True)
    c24service = models.CharField(max_length=2, blank=True, null=True)
    c24service_price = models.FloatField(blank=True, null=True)
    coupon_codes = models.SmallIntegerField(blank=True, null=True)
    customer_price = models.FloatField(blank=True, null=True)
    duration = models.SmallIntegerField()
    duty_shift = models.SmallIntegerField()
    no_of_caregivers = models.SmallIntegerField(blank=True, null=True)
    patient_condition = models.CharField(max_length=255, blank=True, null=True)
    opened_by = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    infant_age = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    discount_code = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING, blank=True, null=True)
    exo_phone = models.ForeignKey(InteractionmanagerExophone, models.DO_NOTHING, blank=True, null=True)
    brs = models.ForeignKey(BillingBookingratestandardization, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(GeographyCity, models.DO_NOTHING, blank=True, null=True)
    booking_info_json = models.TextField(blank=True, null=True)
    profile = models.ForeignKey('UsermanagementProfile', models.DO_NOTHING, blank=True, null=True)
    referee = models.ForeignKey('UsermanagementCareuser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeadManager_lead'


class LeadmanagerLeadPatientConditions(models.Model):
    lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING)
    patientcondition = models.ForeignKey('RequestbookingPatientcondition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LeadManager_lead_patient_conditions'
        unique_together = (('lead', 'patientcondition'),)


class LeadmanagerLeadextraprops(models.Model):
    patient_name = models.CharField(max_length=60, blank=True, null=True)
    patient_condition = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    raw_address = models.TextField(blank=True, null=True)
    nearest_landmark = models.CharField(max_length=60, blank=True, null=True)
    pref_gender = models.CharField(max_length=2, blank=True, null=True)
    pref_eating_habit = models.CharField(max_length=2, blank=True, null=True)
    first_visit_at_hosp = models.BooleanField()
    duration = models.SmallIntegerField(blank=True, null=True)
    price_negotiated = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_hour = models.SmallIntegerField(blank=True, null=True)
    for_lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING, unique=True)
    relationship_with_customer = models.SmallIntegerField(blank=True, null=True)
    estimated_number_of_visits = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeadManager_leadextraprops'


class LeadmanagerLeadextrapropsPatientConditions(models.Model):
    leadextraprops = models.ForeignKey(LeadmanagerLeadextraprops, models.DO_NOTHING)
    patientcondition = models.ForeignKey('RequestbookingPatientcondition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LeadManager_leadextraprops_patient_conditions'
        unique_together = (('leadextraprops', 'patientcondition'),)


class LeadmanagerLeadextrapropsPrefLang(models.Model):
    leadextraprops = models.ForeignKey(LeadmanagerLeadextraprops, models.DO_NOTHING)
    language = models.ForeignKey(GenericdataLanguage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LeadManager_leadextraprops_pref_lang'
        unique_together = (('leadextraprops', 'language'),)


class LeadmanagerLeadgooglecampaigndetails(models.Model):
    adgrid = models.CharField(max_length=50, blank=True, null=True)
    cmpid = models.CharField(max_length=50, blank=True, null=True)
    adcpid = models.CharField(db_column='adCpid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adpos = models.CharField(max_length=50, blank=True, null=True)
    device = models.CharField(max_length=50, blank=True, null=True)
    kywd = models.CharField(max_length=100, blank=True, null=True)
    mtchtyp = models.CharField(max_length=50, blank=True, null=True)
    network = models.CharField(max_length=50, blank=True, null=True)
    placement = models.CharField(max_length=50, blank=True, null=True)
    formloc = models.CharField(max_length=50, blank=True, null=True)
    intloc = models.CharField(max_length=50, blank=True, null=True)
    targetid = models.CharField(max_length=50, blank=True, null=True)
    devmdl = models.CharField(max_length=50, blank=True, null=True)
    feedid = models.CharField(db_column='Feedid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gclid = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    for_lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeadManager_leadgooglecampaigndetails'


class LeadmanagerLeadpriority(models.Model):
    intent = models.SmallIntegerField()
    lead_type = models.SmallIntegerField()
    service = models.SmallIntegerField()
    lstat = models.SmallIntegerField(blank=True, null=True)
    start_minute_offset = models.IntegerField()
    end_minute_offset = models.IntegerField()
    priority = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'LeadManager_leadpriority'


class LeadmanagerLeadquantifierservicemapping(models.Model):
    lead_quantifier = models.CharField(max_length=100)
    service = models.SmallIntegerField()
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    region = models.ForeignKey(GeographyRegion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LeadManager_leadquantifierservicemapping'


class LeadmanagerLeadqueuehistory(models.Model):
    lead_queue_status = models.SmallIntegerField()
    created = models.DateTimeField()
    ccuser = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LeadManager_leadqueuehistory'


class LeadmanagerLeadstatus(models.Model):
    lstat = models.SmallIntegerField(blank=True, null=True)
    tstamp = models.DateTimeField()
    next_contact = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    for_lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING)
    changes = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeadManager_leadstatus'


class LeadmanagerLeadstatuspriortiy(models.Model):
    lead_status = models.CharField(max_length=50)
    lead_status_code = models.SmallIntegerField()
    priority = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'LeadManager_leadstatuspriortiy'


class LeadmanagerLeadtypepriortiy(models.Model):
    lead_type = models.CharField(max_length=50)
    lead_type_code = models.SmallIntegerField()
    priority = models.SmallIntegerField()
    lead_type_category = models.CharField(max_length=50)
    lead_type_category_code = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'LeadManager_leadtypepriortiy'


class LeadmanagerPayment(models.Model):
    pid = models.CharField(unique=True, max_length=64)
    status = models.CharField(max_length=10, blank=True, null=True)
    buyer_name = models.CharField(max_length=256, blank=True, null=True)
    buyer_phone = models.CharField(max_length=128, blank=True, null=True)
    buyer_email = models.CharField(max_length=254, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    offer_slug = models.CharField(max_length=256, blank=True, null=True)
    lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeadManager_payment'


class LeadmanagerPractolead(models.Model):
    service = models.SmallIntegerField()
    lead_type = models.SmallIntegerField()
    phone = models.CharField(max_length=128, blank=True, null=True)
    call_duration = models.SmallIntegerField(blank=True, null=True)
    call_status = models.CharField(max_length=30, blank=True, null=True)
    c24_cc_no = models.CharField(max_length=128, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    call_time = models.DateTimeField(blank=True, null=True)
    practo_call_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeadManager_practolead'


class LeadmanagerServicepriortiy(models.Model):
    service = models.CharField(max_length=50)
    service_code = models.SmallIntegerField()
    priority = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'LeadManager_servicepriortiy'


class LeadmanagerTimepriority(models.Model):
    start_time = models.SmallIntegerField()
    end_time = models.SmallIntegerField()
    priority = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'LeadManager_timepriority'


class LeadmanagerWebengagelead(models.Model):
    survey_response = models.TextField(blank=True, null=True)
    survey_id = models.CharField(max_length=60, blank=True, null=True)
    for_lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LeadManager_webengagelead'


class MedicationreminderDisease(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MedicationReminder_disease'


class MedicationreminderMedicine(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    medicine_name = models.CharField(max_length=50, blank=True, null=True)
    med_type = models.CharField(max_length=50)
    meal_type = models.CharField(max_length=20)
    remarks = models.TextField(blank=True, null=True)
    quantity_unit = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'MedicationReminder_medicine'


class MedicationreminderMedicinedisease(models.Model):
    disease = models.ForeignKey(MedicationreminderDisease, models.DO_NOTHING, blank=True, null=True)
    medicine = models.ForeignKey(MedicationreminderMedicine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MedicationReminder_medicinedisease'


class MedicationreminderPrescplantimemap(models.Model):
    intake_time = models.TimeField(blank=True, null=True)
    quantity = models.SmallIntegerField()
    active = models.BooleanField()
    presc_plan = models.ForeignKey('MedicationreminderPrescriptionplan', models.DO_NOTHING)
    time_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'MedicationReminder_prescplantimemap'


class MedicationreminderPrescription(models.Model):
    prescription_img = models.CharField(max_length=100)
    verified = models.BooleanField()
    comments = models.TextField()
    amount = models.CharField(max_length=5, blank=True, null=True)
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    patient = models.ForeignKey('UsermanagementC24Patient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'MedicationReminder_prescription'


class MedicationreminderPrescriptionlog(models.Model):
    remarks = models.TextField(blank=True, null=True)
    previous_status = models.CharField(max_length=2)
    status = models.CharField(max_length=2)
    status_time = models.DateTimeField()
    source = models.CharField(max_length=1)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    visit = models.ForeignKey('RequestbookingC24Visit', models.DO_NOTHING)
    presc_plan_time = models.ForeignKey(MedicationreminderPrescplantimemap, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MedicationReminder_prescriptionlog'


class MedicationreminderPrescriptionplan(models.Model):
    meal_type = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    medicine = models.ForeignKey(MedicationreminderMedicine, models.DO_NOTHING, blank=True, null=True)
    prescription = models.ForeignKey(MedicationreminderPrescription, models.DO_NOTHING, blank=True, null=True)
    freq_gap = models.SmallIntegerField(blank=True, null=True)
    freq_unit = models.CharField(max_length=10)
    is_freq = models.BooleanField()
    afternoon = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    evening = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    morning = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    night = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MedicationReminder_prescriptionplan'


class MedicationreminderSymptom(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MedicationReminder_symptom'


class NewsletterEmaillist(models.Model):
    email = models.CharField(max_length=254, blank=True, null=True)
    unsubscribe = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Newsletter_emaillist'


class PatientdiseasedetailDailyassessmentdetails(models.Model):
    datetime = models.DateTimeField()
    json_data = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    patient_disease_details = models.ForeignKey('PatientdiseasedetailPatientdiseasedetails', models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PatientDiseaseDetail_dailyassessmentdetails'


class PatientdiseasedetailPatientdiseasedetails(models.Model):
    age = models.SmallIntegerField()
    gender = models.SmallIntegerField()
    disease = models.SmallIntegerField()
    disease_type = models.SmallIntegerField()
    disease_stage = models.CharField(max_length=3)
    other_healthcare_professional = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING)
    patient = models.ForeignKey('UsermanagementC24Patient', models.DO_NOTHING, blank=True, null=True)
    disease_type_other_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PatientDiseaseDetail_patientdiseasedetails'


class PatientdiseasedetailPatientdoctordetails(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    medical_team = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    patient_disease_details = models.ForeignKey(PatientdiseasedetailPatientdiseasedetails, models.DO_NOTHING)
    phone_number = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PatientDiseaseDetail_patientdoctordetails'


class PatientdiseasedetailPatientmedicalreports(models.Model):
    report_type = models.SmallIntegerField()
    file = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    patient_disease_details = models.ForeignKey(PatientdiseasedetailPatientdiseasedetails, models.DO_NOTHING)
    tags = models.TextField()

    class Meta:
        managed = False
        db_table = 'PatientDiseaseDetail_patientmedicalreports'


class PatientdiseasedetailPatientnotes(models.Model):
    note_title = models.CharField(max_length=100, blank=True, null=True)
    note_remarks = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey('UsermanagementC24Patient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'PatientDiseaseDetail_patientnotes'


class PatientdiseasedetailPatienttreatmentdetails(models.Model):
    treatment = models.SmallIntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    no_of_cycle_prescribed = models.CharField(max_length=10, blank=True, null=True)
    no_of_cycle_received = models.CharField(max_length=10, blank=True, null=True)
    device_implanted = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    patient_disease_details = models.ForeignKey(PatientdiseasedetailPatientdiseasedetails, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'PatientDiseaseDetail_patienttreatmentdetails'


class PatientdiseasedetailThoughtsoftheday(models.Model):
    datetime = models.DateTimeField()
    thought = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'PatientDiseaseDetail_thoughtsoftheday'


class PaymentgatewayPaymentresponse(models.Model):
    merchant_id = models.TextField(unique=True)
    vendor_txn_id = models.TextField(blank=True, null=True)
    vendor_txn_status = models.TextField(blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vendor_txn_msg = models.TextField(blank=True, null=True)
    pg_txn_id = models.TextField(blank=True, null=True)
    issuer_ref_no = models.TextField(blank=True, null=True)
    auth_id_code = models.TextField(blank=True, null=True)
    txn_first_name = models.TextField(blank=True, null=True)
    txn_last_name = models.TextField(blank=True, null=True)
    pg_resp_code = models.TextField(blank=True, null=True)
    txn_address_zip = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vendor_signature = models.TextField(blank=True, null=True)
    txn_status = models.SmallIntegerField()
    invoice = models.ForeignKey(BillingCollectioninvoices, models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, blank=True, null=True)
    advance = models.ForeignKey(BillingAdvancepayment, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    source = models.TextField(blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    payment_gateway = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PaymentGateway_paymentresponse'


class PaymentgatewayPaymentresponseDiscounts(models.Model):
    paymentresponse = models.ForeignKey(PaymentgatewayPaymentresponse, models.DO_NOTHING)
    discountmaster = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'PaymentGateway_paymentresponse_discounts'
        unique_together = (('paymentresponse', 'discountmaster'),)


class ProjectconfigsAlertengine(models.Model):
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    notification_dict = models.TextField(blank=True, null=True)
    popup_parameter = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    project_configuration = models.ForeignKey('ProjectconfigsProjectconfigparameter', models.DO_NOTHING, unique=True)
    alert_category = models.SmallIntegerField()
    alert_sub_category = models.SmallIntegerField()
    is_ticket_active = models.BooleanField()
    sms_template_fk = models.ForeignKey(InteractionmanagerSmstemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_alertengine'


class ProjectconfigsAlertengineGroup(models.Model):
    alertengine = models.ForeignKey(ProjectconfigsAlertengine, models.DO_NOTHING)
    notificationgroup = models.ForeignKey('ProjectconfigsNotificationgroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_alertengine_group'
        unique_together = (('alertengine', 'notificationgroup'),)


class ProjectconfigsAlertengineNotificationChannel(models.Model):
    alertengine = models.ForeignKey(ProjectconfigsAlertengine, models.DO_NOTHING)
    notificationchannel = models.ForeignKey('ProjectconfigsNotificationchannel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_alertengine_notification_channel'
        unique_together = (('alertengine', 'notificationchannel'),)


class ProjectconfigsAlertengineServicesForAlert(models.Model):
    alertengine = models.ForeignKey(ProjectconfigsAlertengine, models.DO_NOTHING)
    servicetype = models.ForeignKey('ProjectconfigsServicetype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_alertengine_services_for_alert'
        unique_together = (('alertengine', 'servicetype'),)


class ProjectconfigsAlertlog(models.Model):
    data_json = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_alertlog'


class ProjectconfigsConfigdict(models.Model):
    key = models.CharField(unique=True, max_length=50)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_configdict'


class ProjectconfigsDispostionnotification(models.Model):
    message = models.TextField()
    action_text = models.CharField(max_length=400, blank=True, null=True)
    action_target = models.CharField(max_length=400, blank=True, null=True)
    msg_id = models.CharField(max_length=200)
    msg_type = models.CharField(max_length=200)
    call_status = models.CharField(max_length=100)
    timeout = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    disposition = models.ForeignKey(InteractionmanagerCalldisposition, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_dispostionnotification'


class ProjectconfigsGroupmember(models.Model):
    name = models.CharField(max_length=100)
    slack_group = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    desktop_notification_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    phone_number_fk = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_groupmember'


class ProjectconfigsGroupmemberServicesForAlert(models.Model):
    groupmember = models.ForeignKey(ProjectconfigsGroupmember, models.DO_NOTHING)
    servicetype = models.ForeignKey('ProjectconfigsServicetype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_groupmember_services_for_alert'
        unique_together = (('groupmember', 'servicetype'),)


class ProjectconfigsNotificationchannel(models.Model):
    medium = models.SmallIntegerField(unique=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_notificationchannel'


class ProjectconfigsNotificationgroup(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    cc_user_group = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_notificationgroup'


class ProjectconfigsNotificationgroupGroupMembers(models.Model):
    notificationgroup = models.ForeignKey(ProjectconfigsNotificationgroup, models.DO_NOTHING)
    groupmember = models.ForeignKey(ProjectconfigsGroupmember, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_notificationgroup_group_members'
        unique_together = (('notificationgroup', 'groupmember'),)


class ProjectconfigsProjectconfigparameter(models.Model):
    key = models.CharField(unique=True, max_length=100)
    value = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_projectconfigparameter'


class ProjectconfigsServicetype(models.Model):
    short = models.CharField(max_length=3)
    internal_name = models.CharField(unique=True, max_length=45)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ProjectConfigs_servicetype'


class ProviderpropsCgaccount(models.Model):
    ac_num = models.CharField(max_length=20)
    branch = models.CharField(max_length=200)
    ifsc = models.CharField(max_length=15)
    ac_type = models.CharField(max_length=2)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    bank = models.ForeignKey(GenericdataBank, models.DO_NOTHING)
    for_cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    is_verified = models.BooleanField()
    verified_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    is_primary = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ProviderProps_cgaccount'


class ProviderpropsCv(models.Model):
    education = models.SmallIntegerField()
    workex = models.FloatField()
    for_cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'ProviderProps_cv'


class ProviderpropsCvWorkedInHospitals(models.Model):
    cv = models.ForeignKey(ProviderpropsCv, models.DO_NOTHING)
    medicalfacility = models.ForeignKey(GeographyMedicalfacility, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProviderProps_cv_worked_in_hospitals'
        unique_together = (('cv', 'medicalfacility'),)


class ProviderpropsIdfydetailscg(models.Model):
    purpose = models.CharField(max_length=3)
    details_json = models.CharField(max_length=1024, blank=True, null=True)
    provider_document = models.ForeignKey('ProviderpropsProviderdocument', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProviderProps_idfydetailscg'


class ProviderpropsLanguage(models.Model):
    name = models.CharField(max_length=40)
    modified = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ProviderProps_language'


class ProviderpropsPersonalattributes(models.Model):
    strength = models.SmallIntegerField()
    comm_skills = models.SmallIntegerField()
    shift_preference = models.CharField(max_length=2)
    for_cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, unique=True)
    eating_habit = models.CharField(max_length=2, blank=True, null=True)
    can_handle_baby_ages = models.SmallIntegerField(blank=True, null=True)
    can_handle_twins = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ProviderProps_personalattributes'


class ProviderpropsPersonalattributesLanguagesSpoken(models.Model):
    personalattributes = models.ForeignKey(ProviderpropsPersonalattributes, models.DO_NOTHING)
    language = models.ForeignKey(GenericdataLanguage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProviderProps_personalattributes_languages_spoken'
        unique_together = (('personalattributes', 'language'),)


class ProviderpropsPersonalattributesShift(models.Model):
    personalattributes = models.ForeignKey(ProviderpropsPersonalattributes, models.DO_NOTHING)
    shiftpreference = models.ForeignKey('ProviderpropsShiftpreference', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProviderProps_personalattributes_shift'
        unique_together = (('personalattributes', 'shiftpreference'),)


class ProviderpropsProviderdocument(models.Model):
    doc_type = models.CharField(max_length=5)
    name_or_number = models.CharField(max_length=40)
    scanned_file = models.CharField(max_length=100, blank=True, null=True)
    for_cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    address_type = models.SmallIntegerField(blank=True, null=True)
    details_json = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProviderProps_providerdocument'


class ProviderpropsProviderfamilydetails(models.Model):
    name_honorifics = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    relationship = models.SmallIntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    for_cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProviderProps_providerfamilydetails'


class ProviderpropsProviderhobbies(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField()
    modified = models.DateField()

    class Meta:
        managed = False
        db_table = 'ProviderProps_providerhobbies'


class ProviderpropsProviderinventory(models.Model):
    inventory_type = models.SmallIntegerField()
    date_of_issuance = models.DateField()
    date_of_return = models.DateField(blank=True, null=True)
    active = models.BooleanField()
    modified = models.DateTimeField()
    created = models.DateTimeField()
    for_cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    notes = models.TextField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ProviderProps_providerinventory'


class ProviderpropsProviderstat(models.Model):
    visits_completed = models.IntegerField()
    no_shows = models.IntegerField()
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProviderProps_providerstat'


class ProviderpropsServiceprocedure(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    service_offered = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'ProviderProps_serviceprocedure'


class ProviderpropsServicespecialization(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    service_offered = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'ProviderProps_servicespecialization'


class ProviderpropsShiftpreference(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ProviderProps_shiftpreference'


class QrcticketingActionticket(models.Model):
    status = models.SmallIntegerField()
    due_date = models.DateTimeField()
    task_description = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    delay_remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    assigned_team = models.ForeignKey('UsermanagementC24Team', models.DO_NOTHING, blank=True, null=True)
    assigned_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    serviceticket = models.ForeignKey('QrcticketingServiceticket', models.DO_NOTHING)
    alt_assigned_team_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_actionticket'


class QrcticketingActiontickethist(models.Model):
    changes = models.CharField(max_length=150, blank=True, null=True)
    status = models.SmallIntegerField()
    comments = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    delay_remarks = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField()
    actionticket = models.ForeignKey(QrcticketingActionticket, models.DO_NOTHING)
    assigned_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_actiontickethist'


class QrcticketingAllocationticket(models.Model):
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING)
    ticket = models.ForeignKey('HelpdeskTicket', models.DO_NOTHING, unique=True)
    typ = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_allocationticket'


class QrcticketingConfigureticketpriority(models.Model):
    category = models.SmallIntegerField()
    priority = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    assigned_team = models.ForeignKey('UsermanagementC24Team', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_configureticketpriority'
        unique_together = (('category', 'assigned_team'),)


class QrcticketingMcrstathistory(models.Model):
    resolution = models.SmallIntegerField()
    next_call = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    changes = models.CharField(max_length=150, blank=True, null=True)
    tstamp = models.DateTimeField()
    assigned_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    mcr = models.ForeignKey('QrcticketingMissedcallrecord', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_mcrstathistory'


class QrcticketingMissedcallrecord(models.Model):
    from_number_type = models.CharField(max_length=2)
    resolution = models.SmallIntegerField()
    missed_at = models.DateTimeField()
    next_call = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField()
    phnum = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING)
    remarks = models.TextField(blank=True, null=True)
    assigned_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    alt_num_updated4cust = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    linked2lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING, blank=True, null=True)
    linked2booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, blank=True, null=True)
    ticket = models.ForeignKey('HelpdeskTicket', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_missedcallrecord'


class QrcticketingServiceticket(models.Model):
    raised_by = models.SmallIntegerField()
    category = models.SmallIntegerField()
    priority = models.SmallIntegerField()
    customer_mood = models.SmallIntegerField()
    validity = models.BooleanField()
    status = models.SmallIntegerField()
    due_date = models.DateTimeField()
    remarks = models.TextField(blank=True, null=True)
    action_plan = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    assigned_team = models.ForeignKey('UsermanagementC24Team', models.DO_NOTHING, blank=True, null=True)
    booking = models.ForeignKey('RequestbookingBooking', models.DO_NOTHING, blank=True, null=True)
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('UsermanagementC24Customer', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    ticket_service = models.CharField(max_length=2, blank=True, null=True)
    ticket_active = models.DateTimeField()
    ticket_source = models.SmallIntegerField()
    alt_assigned_team_id = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey(GeographyCity, models.DO_NOTHING)
    allocation_end_date = models.DateField(blank=True, null=True)
    allocation_start_date = models.DateField(blank=True, null=True)
    repeat_count = models.SmallIntegerField(blank=True, null=True)
    permanent = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'QRCTicketing_serviceticket'


class QrcticketingServicetickethist(models.Model):
    changes = models.CharField(max_length=150, blank=True, null=True)
    priority = models.SmallIntegerField()
    category = models.SmallIntegerField()
    status = models.SmallIntegerField()
    due_date = models.DateTimeField()
    remarks = models.TextField(blank=True, null=True)
    action_plan = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField()
    assigned_team = models.ForeignKey('UsermanagementC24Team', models.DO_NOTHING, blank=True, null=True)
    serviceticket = models.ForeignKey(QrcticketingServiceticket, models.DO_NOTHING)
    alt_assigned_team_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_servicetickethist'


class QrcticketingThirdpartycallattempt(models.Model):
    sid = models.CharField(unique=True, max_length=100)
    typ = models.CharField(max_length=2)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    ph_num = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING)
    is_processed = models.BooleanField()
    exo_phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_thirdpartycallattempt'


class QrcticketingThirdpartycallattemptUrls(models.Model):
    thirdpartycallattempt = models.ForeignKey(QrcticketingThirdpartycallattempt, models.DO_NOTHING)
    tpcallingurl = models.ForeignKey('QrcticketingTpcallingurl', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_thirdpartycallattempt_urls'
        unique_together = (('thirdpartycallattempt', 'tpcallingurl'),)


class QrcticketingTpcallingurl(models.Model):
    url_class = models.CharField(unique=True, max_length=3)
    url = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'QRCTicketing_tpcallingurl'


class QuestionnaireandtrainingCgintcategoryresults(models.Model):
    question_category = models.ForeignKey('QuestionnaireandtrainingQuestioncategory', models.DO_NOTHING)
    caregiver_lead = models.ForeignKey('TrainingandonboardingCglead', models.DO_NOTHING)
    interview_score = models.SmallIntegerField(blank=True, null=True)
    total_time = models.TextField()
    interviewer = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QuestionnaireAndTraining_cgintcategoryresults'


class QuestionnaireandtrainingCgintresult(models.Model):
    question_master = models.ForeignKey('QuestionnaireandtrainingQuestionmaster', models.DO_NOTHING)
    caregiver_lead = models.ForeignKey('TrainingandonboardingCglead', models.DO_NOTHING)
    comments = models.TextField()
    interviewer = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QuestionnaireAndTraining_cgintresult'


class QuestionnaireandtrainingLeadquestionnaireresult(models.Model):
    question_master = models.ForeignKey('QuestionnaireandtrainingQuestionmaster', models.DO_NOTHING)
    lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING)
    comments = models.TextField()
    input_choice = models.ForeignKey('QuestionnaireandtrainingQuestionanswer', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'QuestionnaireAndTraining_leadquestionnaireresult'


class QuestionnaireandtrainingQuestionanswer(models.Model):
    question_master = models.ForeignKey('QuestionnaireandtrainingQuestionmaster', models.DO_NOTHING)
    answer = models.TextField()
    correct_flag = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'QuestionnaireAndTraining_questionanswer'


class QuestionnaireandtrainingQuestioncategory(models.Model):
    service = models.CharField(max_length=2)
    type = models.SmallIntegerField()
    category = models.CharField(max_length=80)
    score = models.SmallIntegerField(blank=True, null=True)
    display_rank = models.SmallIntegerField()
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'QuestionnaireAndTraining_questioncategory'
        unique_together = (('service', 'type', 'category', 'active'),)


class QuestionnaireandtrainingQuestionmaster(models.Model):
    question_category = models.ForeignKey(QuestionnaireandtrainingQuestioncategory, models.DO_NOTHING)
    question_text = models.TextField()
    question_type = models.SmallIntegerField()
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'QuestionnaireAndTraining_questionmaster'


class RequestbookingActionreason(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    context = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'RequestBooking_actionreason'


class RequestbookingBooking(models.Model):
    patient_condition = models.CharField(max_length=255, blank=True, null=True)
    pref_gender = models.CharField(max_length=2)
    pref_eating_habit = models.CharField(max_length=2, blank=True, null=True)
    price_negotiated = models.FloatField(blank=True, null=True)
    start_date = models.DateField()
    start_hour = models.SmallIntegerField()
    estimated_visits = models.SmallIntegerField(blank=True, null=True)
    frequency = models.SmallIntegerField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    was_at_hosp = models.ForeignKey(GeographyMedicalfacility, models.DO_NOTHING, blank=True, null=True)
    for_lead = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING, unique=True, blank=True, null=True)
    patient = models.ForeignKey('UsermanagementC24Patient', models.DO_NOTHING)
    duration = models.SmallIntegerField()
    first_visit_at_hosp = models.BooleanField()
    service = models.CharField(max_length=2)
    next_review = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    nearest_landmark = models.CharField(max_length=100, blank=True, null=True)
    raw_address = models.TextField(blank=True, null=True)
    bstat = models.CharField(max_length=3)
    pref_comm_channel = models.SmallIntegerField(blank=True, null=True)
    pref_comm_frequency = models.SmallIntegerField(blank=True, null=True)
    pref_payment_method = models.SmallIntegerField(blank=True, null=True)
    price_tenure = models.SmallIntegerField()
    address = models.ForeignKey(GeographyCareaddress, models.DO_NOTHING, blank=True, null=True)
    source = models.CharField(max_length=2)
    status_reason = models.TextField(blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    duty_shift = models.SmallIntegerField()
    no_of_caregivers = models.SmallIntegerField()
    onboarding_timeslots = models.TextField(blank=True, null=True)
    onboarding_date = models.DateField(blank=True, null=True)
    onboarding_status = models.CharField(max_length=2, blank=True, null=True)
    onboarding_agent = models.TextField(blank=True, null=True)
    customer_estimated_days = models.IntegerField()
    onboard_agent = models.ForeignKey('RequestbookingOnboardingagent', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.SmallIntegerField(blank=True, null=True)
    discount = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING, blank=True, null=True)
    allocation_end_date = models.DateField(blank=True, null=True)
    allocation_start_date = models.DateField(blank=True, null=True)
    payer = models.ForeignKey('UsermanagementPayerinformation', models.DO_NOTHING, blank=True, null=True)
    review_remarks = models.TextField(blank=True, null=True)
    allocation_remarks = models.TextField(blank=True, null=True)
    subbstat = models.CharField(max_length=10, blank=True, null=True)
    assign_to = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    complex = models.BooleanField()
    followup_date = models.DateField(blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)
    collection_timeslots = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_booking'


class RequestbookingBookingFiles(models.Model):
    name = models.CharField(max_length=20)
    datetime = models.DateTimeField(blank=True, null=True)
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    prescription = models.ForeignKey('RequestbookingPrescription', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_booking_files'


class RequestbookingBookingPatientConditions(models.Model):
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    patientcondition = models.ForeignKey('RequestbookingPatientcondition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_booking_patient_conditions'
        unique_together = (('booking', 'patientcondition'),)


class RequestbookingBookingPrefLang(models.Model):
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    language = models.ForeignKey(GenericdataLanguage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_booking_pref_lang'
        unique_together = (('booking', 'language'),)


class RequestbookingBookingbroadcast(models.Model):
    is_interested = models.NullBooleanField()
    cost = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    notification = models.ForeignKey(DevicemanagerNotification, models.DO_NOTHING, blank=True, null=True)
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    is_visible = models.NullBooleanField()
    review_at = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    reschedule_datetime = models.DateTimeField(blank=True, null=True)
    location_extra = models.TextField(blank=True, null=True)
    accepted = models.NullBooleanField()
    accepted_time = models.DateTimeField(blank=True, null=True)
    reject_reason = models.IntegerField()
    rejected_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_bookingbroadcast'
        unique_together = (('booking', 'provider', 'notification'),)


class RequestbookingBookingcrosssell(models.Model):
    sell_type = models.SmallIntegerField(blank=True, null=True)
    service_type = models.SmallIntegerField(blank=True, null=True)
    service_category = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    initiated_by = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    confirmed = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'RequestBooking_bookingcrosssell'


class RequestbookingBookingcrosssellPrescription(models.Model):
    bookingcrosssell = models.ForeignKey(RequestbookingBookingcrosssell, models.DO_NOTHING)
    prescription = models.ForeignKey('RequestbookingPrescription', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_bookingcrosssell_prescription'
        unique_together = (('bookingcrosssell', 'prescription'),)


class RequestbookingBookingdiscounthistory(models.Model):
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    discount_code = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_bookingdiscounthistory'


class RequestbookingBookingmedicalcondition(models.Model):
    patient_location = models.TextField(blank=True, null=True)
    symtoms = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    surgery_details = models.TextField(blank=True, null=True)
    patient_condition = models.TextField(blank=True, null=True)
    breathing = models.TextField(blank=True, null=True)
    eating = models.TextField(blank=True, null=True)
    excretion = models.TextField(blank=True, null=True)
    skin_condition = models.TextField(blank=True, null=True)
    movement = models.TextField(blank=True, null=True)
    blood_investigation = models.TextField(blank=True, null=True)
    patient_lines = models.TextField(blank=True, null=True)
    treatment_medication = models.TextField(blank=True, null=True)
    disease_condition = models.TextField(blank=True, null=True)
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_bookingmedicalcondition'


class RequestbookingBookingmedicalconditionPatientConditions(models.Model):
    bookingmedicalcondition = models.ForeignKey(RequestbookingBookingmedicalcondition, models.DO_NOTHING)
    patientcondition = models.ForeignKey('RequestbookingPatientcondition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_bookingmedicalcondition_patient_conditions'
        unique_together = (('bookingmedicalcondition', 'patientcondition'),)


class RequestbookingBookingpricehistory(models.Model):
    price = models.FloatField()
    duration = models.SmallIntegerField()
    no_of_caregivers = models.SmallIntegerField()
    duty_shift = models.SmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_bookingpricehistory'


class RequestbookingBookingstatus(models.Model):
    status = models.CharField(max_length=3)
    changes = models.CharField(max_length=150, blank=True, null=True)
    tstamp = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    remarks = models.TextField(blank=True, null=True)
    sub_status = models.CharField(max_length=5, blank=True, null=True)
    status_reason = models.TextField(blank=True, null=True)
    allocation_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_bookingstatus'


class RequestbookingBruteforcevt(models.Model):
    is_done = models.BooleanField()
    is_later = models.BooleanField()
    is_opened = models.BooleanField()
    later_time = models.DateTimeField(blank=True, null=True)
    done_by = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    later_counter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'RequestBooking_bruteforcevt'


class RequestbookingC24Visit(models.Model):
    home_or_hospital = models.CharField(max_length=2)
    date_time = models.DateTimeField()
    hours = models.SmallIntegerField()
    curr_status = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    address = models.ForeignKey(GeographyCareaddress, models.DO_NOTHING)
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    for_booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    cg_consumables = models.SmallIntegerField(blank=True, null=True)
    cg_fees = models.FloatField(blank=True, null=True)
    cg_travel = models.SmallIntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    allowance_transaction = models.ForeignKey(AccountingTransaction, models.DO_NOTHING, blank=True, null=True)
    fee_transaction = models.ForeignKey(AccountingTransaction, models.DO_NOTHING, blank=True, null=True)
    actual_end = models.DateTimeField(blank=True, null=True)
    actual_start = models.DateTimeField(blank=True, null=True)
    cg_remarks = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)  # This field type is a guess.
    vt = models.ForeignKey('RequestbookingVisittracking', models.DO_NOTHING, unique=True, blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    shortlist_type = models.CharField(max_length=20, blank=True, null=True)
    bfvt = models.ForeignKey(RequestbookingBruteforcevt, models.DO_NOTHING, unique=True, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    cx_confirmed_status = models.SmallIntegerField(blank=True, null=True)
    signature_cg = models.CharField(max_length=100, blank=True, null=True)
    pre_confirmation = models.DateTimeField(blank=True, null=True)
    alloted_time = models.DateTimeField(blank=True, null=True)
    left_home_at = models.DateTimeField(blank=True, null=True)
    reached_at = models.DateTimeField(blank=True, null=True)
    discount = models.ForeignKey(DiscountsDiscountmaster, models.DO_NOTHING, blank=True, null=True)
    customer_remarks = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    cash_cheque_preference = models.IntegerField(blank=True, null=True)
    visit_issues = models.TextField(blank=True, null=True)
    ht_visit_id = models.UUIDField(blank=True, null=True)
    ht_trip_id = models.UUIDField(blank=True, null=True)
    end_gps = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_gps = models.TextField(blank=True, null=True)  # This field type is a guess.
    ht_stopover_id = models.UUIDField(blank=True, null=True)
    source = models.SmallIntegerField(blank=True, null=True)
    cg_null_reason = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_c24visit'
        unique_together = (('fee_transaction', 'allowance_transaction'),)


class RequestbookingC24Visitstatus(models.Model):
    curr_status = models.SmallIntegerField()
    hours = models.SmallIntegerField()
    cg_fees = models.FloatField(blank=True, null=True)
    changes = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField()
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)
    visit = models.ForeignKey(RequestbookingC24Visit, models.DO_NOTHING)
    source = models.SmallIntegerField(blank=True, null=True)
    cg_null_reason = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_c24visitstatus'


class RequestbookingCgallocationresponse(models.Model):
    response_status = models.SmallIntegerField()
    remarks = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_cgallocationresponse'


class RequestbookingConditionanswers(models.Model):
    answers = models.TextField(blank=True, null=True)
    condition_questions = models.ForeignKey('RequestbookingConditionquestions', models.DO_NOTHING)
    lead_id = models.ForeignKey(LeadmanagerLead, models.DO_NOTHING)
    patient = models.ForeignKey('UsermanagementC24Patient', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_conditionanswers'


class RequestbookingConditionquestions(models.Model):
    questions = models.TextField()
    rank = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'RequestBooking_conditionquestions'


class RequestbookingConditionquestionsCondition(models.Model):
    conditionquestions = models.ForeignKey(RequestbookingConditionquestions, models.DO_NOTHING)
    patientcondition = models.ForeignKey('RequestbookingPatientcondition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_conditionquestions_condition'
        unique_together = (('conditionquestions', 'patientcondition'),)


class RequestbookingCrosssellmasterdata(models.Model):
    service = models.CharField(max_length=2, blank=True, null=True)
    service_type = models.SmallIntegerField(blank=True, null=True)
    category = models.SmallIntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=256, blank=True, null=True)
    item_type = models.CharField(max_length=256, blank=True, null=True)
    item_brand = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    vendor_name = models.CharField(max_length=256, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_tenure = models.SmallIntegerField(blank=True, null=True)
    min_days = models.IntegerField(blank=True, null=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    delivery_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_crosssellmasterdata'


class RequestbookingExtendedvisit(models.Model):
    extended_date = models.DateField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    extended_by = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_extendedvisit'


class RequestbookingOnboardingagent(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    auth_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    phone = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_onboardingagent'


class RequestbookingPatientcondition(models.Model):
    condition = models.CharField(max_length=100)
    authorised = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'RequestBooking_patientcondition'


class RequestbookingPrescription(models.Model):
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'RequestBooking_prescription'


class RequestbookingReviewdatehistory(models.Model):
    review_date = models.DateTimeField()
    review_remarks = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_reviewdatehistory'


class RequestbookingVisitaction(models.Model):
    action = models.CharField(max_length=5)
    date_time = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    reason = models.ForeignKey(RequestbookingActionreason, models.DO_NOTHING, blank=True, null=True)
    visit = models.ForeignKey(RequestbookingC24Visit, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'RequestBooking_visitaction'


class RequestbookingVisittracking(models.Model):
    cg_call_status = models.SmallIntegerField(blank=True, null=True)
    cg_no_of_tries = models.IntegerField(blank=True, null=True)
    cg_call_remarks = models.TextField(blank=True, null=True)
    cg_response = models.SmallIntegerField(blank=True, null=True)
    cust_call_status = models.SmallIntegerField(blank=True, null=True)
    cust_no_of_tries = models.IntegerField(blank=True, null=True)
    cust_call_remarks = models.TextField(blank=True, null=True)
    cust_response = models.SmallIntegerField(blank=True, null=True)
    cust_action_required = models.SmallIntegerField(blank=True, null=True)
    cg_spoke_to = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    cust_spoke_to = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)
    alloc_user = models.ForeignKey(CompanyCallcenter, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequestBooking_visittracking'


class TasklistBookingtask(models.Model):
    frequency_gap = models.SmallIntegerField()
    active = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    task_time = models.TimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    task = models.ForeignKey('TasklistTask', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TaskList_bookingtask'


class TasklistBookingtaskmap(models.Model):
    map_id = models.IntegerField(blank=True, null=True)
    map_model = models.CharField(max_length=100, blank=True, null=True)
    booking_task = models.ForeignKey(TasklistBookingtask, models.DO_NOTHING)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'TaskList_bookingtaskmap'


class TasklistCgbookingtask(models.Model):
    frequency_gap = models.SmallIntegerField()
    active = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    task_time = models.TimeField(blank=True, null=True)
    source = models.CharField(max_length=5)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING)
    task = models.ForeignKey('TasklistTask', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TaskList_cgbookingtask'


class TasklistCgbookingtaskmap(models.Model):
    map_id = models.IntegerField(blank=True, null=True)
    map_model = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField()
    cg_booking_task = models.ForeignKey(TasklistCgbookingtask, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TaskList_cgbookingtaskmap'


class TasklistCgcompulsorydos(models.Model):
    context = models.CharField(max_length=10)
    provider_role = models.CharField(max_length=5)
    task_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'TaskList_cgcompulsorydos'


class TasklistCgcompulsorydoslog(models.Model):
    checked = models.BooleanField()
    updated = models.DateTimeField(blank=True, null=True)
    comp_do = models.ForeignKey(TasklistCgcompulsorydos, models.DO_NOTHING)
    visit = models.ForeignKey(RequestbookingC24Visit, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TaskList_cgcompulsorydoslog'


class TasklistCgdailyvisittask(models.Model):
    remarks = models.TextField(blank=True, null=True)
    missed = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    cg_booking_task = models.ForeignKey(TasklistCgbookingtask, models.DO_NOTHING)
    visit = models.ForeignKey(RequestbookingC24Visit, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TaskList_cgdailyvisittask'


class TasklistTask(models.Model):
    name = models.CharField(max_length=150)
    frequency_type = models.CharField(max_length=50)
    service = models.CharField(max_length=2)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    category = models.ForeignKey('TasklistTaskcategory', models.DO_NOTHING, blank=True, null=True)
    medicine = models.ForeignKey(MedicationreminderMedicine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskList_task'


class TasklistTaskSpecializations(models.Model):
    task = models.ForeignKey(TasklistTask, models.DO_NOTHING)
    servicespecialization = models.ForeignKey(ProviderpropsServicespecialization, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TaskList_task_specializations'
        unique_together = (('task', 'servicespecialization'),)


class TasklistTaskcategory(models.Model):
    name = models.CharField(max_length=50)
    category_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'TaskList_taskcategory'


class TasklistVisittask(models.Model):
    remarks = models.TextField(blank=True, null=True)
    previous_status = models.CharField(max_length=2)
    status = models.CharField(max_length=2)
    status_time = models.DateTimeField()
    source = models.CharField(max_length=1)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    task = models.ForeignKey(TasklistBookingtask, models.DO_NOTHING)
    visit = models.ForeignKey(RequestbookingC24Visit, models.DO_NOTHING)
    cust_mood = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'TaskList_visittask'


class TimeseriesTimeseriesdata(models.Model):
    tslabel = models.ForeignKey('TimeseriesTslabel', models.DO_NOTHING)
    timestamp = models.DateTimeField()
    data = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TimeSeries_timeseriesdata'
        unique_together = (('tslabel', 'timestamp'),)


class TimeseriesTslabel(models.Model):
    label = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    caption = models.CharField(max_length=255)
    granularity_choice = models.IntegerField()
    function = models.IntegerField()
    args = models.TextField(blank=True, null=True)
    multiplier = models.IntegerField()
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    auto_pop = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'TimeSeries_tslabel'


class TrainingandonboardingC24Traininglocation(models.Model):
    raw_address = models.TextField()
    name = models.CharField(max_length=30)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    city = models.ForeignKey(GeographyCity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_c24traininglocation'


class TrainingandonboardingC24Trainingmaster(models.Model):
    type = models.SmallIntegerField()
    service = models.CharField(max_length=2)
    remarks = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_c24trainingmaster'


class TrainingandonboardingCginterview(models.Model):
    type = models.SmallIntegerField()
    date = models.DateField()
    slot = models.SmallIntegerField()
    result = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    cg_lead = models.ForeignKey('TrainingandonboardingCglead', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_cginterview'


class TrainingandonboardingCglead(models.Model):
    phone = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=2)
    source = models.SmallIntegerField()
    newspaper_name = models.SmallIntegerField(blank=True, null=True)
    service = models.CharField(max_length=2)
    aadhar_id_flag = models.BooleanField()
    education = models.SmallIntegerField(blank=True, null=True)
    degree_certificate_flag = models.BooleanField()
    workex_yrs = models.FloatField(blank=True, null=True)
    raw_address = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    status_reason = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    city = models.ForeignKey(GeographyCity, models.DO_NOTHING, blank=True, null=True)
    referral_cg = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_cglead'


class TrainingandonboardingCgleadstatus(models.Model):
    status = models.SmallIntegerField()
    status_reason = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField()
    cg_lead = models.ForeignKey(TrainingandonboardingCglead, models.DO_NOTHING)
    changes = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_cgleadstatus'


class TrainingandonboardingCgtraining(models.Model):
    attendance_status = models.SmallIntegerField()
    remarks = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    cg_training_session = models.ForeignKey('TrainingandonboardingCgtrainingsession', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_cgtraining'


class TrainingandonboardingCgtrainingsession(models.Model):
    start_time = models.DateTimeField()
    duration = models.SmallIntegerField()
    status = models.SmallIntegerField()
    remarks = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    training = models.ForeignKey(TrainingandonboardingC24Trainingmaster, models.DO_NOTHING)
    training_location = models.ForeignKey(TrainingandonboardingC24Traininglocation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_cgtrainingsession'


class TrainingandonboardingIdfydocumentfield(models.Model):
    reference_id = models.CharField(max_length=50)
    doc_type = models.CharField(max_length=5)
    field_type = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_idfydocumentfield'
        unique_together = (('reference_id', 'doc_type', 'field_type'),)


class TrainingandonboardingIdfydocumentrecord(models.Model):
    reference_id = models.CharField(max_length=50)
    doc_type = models.CharField(max_length=5)
    status = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_idfydocumentrecord'
        unique_together = (('reference_id', 'doc_type'),)


class TrainingandonboardingIdfyrecord(models.Model):
    reference_id = models.CharField(max_length=50)
    request_id = models.CharField(max_length=50, blank=True, null=True)
    profile_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    request_status = models.SmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    pdf_report = models.TextField(blank=True, null=True)
    zip_report = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    provider = models.ForeignKey('UsermanagementC24Provider', models.DO_NOTHING)
    json_sent = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrainingAndOnboarding_idfyrecord'


class UsermanagementC24Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateTimeField()
    created = models.DateTimeField()
    gender = models.CharField(max_length=2, blank=True, null=True)
    billing_address = models.ForeignKey(GeographyCareaddress, models.DO_NOTHING, unique=True, blank=True, null=True)
    alt_phnum = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, blank=True, null=True)
    auth_user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phnum = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING)
    receivable_account = models.ForeignKey(AccountingAccount, models.DO_NOTHING, unique=True, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=16, decimal_places=2)
    payment_method = models.SmallIntegerField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    onboarding_date = models.DateField(blank=True, null=True)
    onboarding_status = models.CharField(max_length=2, blank=True, null=True)
    pref_comm_channel = models.SmallIntegerField(blank=True, null=True)
    pref_comm_time = models.SmallIntegerField(blank=True, null=True)
    source = models.SmallIntegerField(blank=True, null=True)
    lead_type = models.SmallIntegerField()
    advance_paying = models.BooleanField()
    onboard_agent = models.ForeignKey(RequestbookingOnboardingagent, models.DO_NOTHING, blank=True, null=True)
    ht_customer_id = models.UUIDField(blank=True, null=True)
    feedback_day = models.TextField(blank=True, null=True)
    billing_cycle = models.SmallIntegerField(blank=True, null=True)
    preferred_address = models.ForeignKey(GeographyCareaddress, models.DO_NOTHING, blank=True, null=True)
    preferred_patient = models.ForeignKey('UsermanagementC24Patient', models.DO_NOTHING, blank=True, null=True)
    preferred_region = models.ForeignKey(GeographyRegion, models.DO_NOTHING, blank=True, null=True)
    profile = models.ForeignKey('UsermanagementProfile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24customer'


class UsermanagementC24Customerprofilehistory(models.Model):
    email = models.CharField(max_length=254, blank=True, null=True)
    tstamp = models.DateTimeField()
    customer = models.ForeignKey(UsermanagementC24Customer, models.DO_NOTHING)
    changes = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24customerprofilehistory'


class UsermanagementC24Patient(models.Model):
    relationship = models.SmallIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(UsermanagementC24Customer, models.DO_NOTHING)
    age = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    contact_num = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    allergies = models.CharField(max_length=100, blank=True, null=True)
    pre_existing_conditions = models.CharField(max_length=100, blank=True, null=True)
    last_visit_address = models.ForeignKey(GeographyCareaddress, models.DO_NOTHING, blank=True, null=True)
    ht_last_visit_dest_id = models.UUIDField(blank=True, null=True)
    last_visit = models.ForeignKey(RequestbookingC24Visit, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    pref_eating_habit = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24patient'
        unique_together = (('customer', 'name', 'relationship'),)


class UsermanagementC24PatientAddresses(models.Model):
    c24patient = models.ForeignKey(UsermanagementC24Patient, models.DO_NOTHING)
    careaddress = models.ForeignKey(GeographyCareaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24patient_addresses'
        unique_together = (('c24patient', 'careaddress'),)


class UsermanagementC24PatientPatientConditions(models.Model):
    c24patient = models.ForeignKey(UsermanagementC24Patient, models.DO_NOTHING)
    patientcondition = models.ForeignKey(RequestbookingPatientcondition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24patient_patient_conditions'
        unique_together = (('c24patient', 'patientcondition'),)


class UsermanagementC24PatientPrefLanguage(models.Model):
    c24patient = models.ForeignKey(UsermanagementC24Patient, models.DO_NOTHING)
    language = models.ForeignKey(GenericdataLanguage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24patient_pref_language'
        unique_together = (('c24patient', 'language'),)


class UsermanagementC24Patientprofilehistory(models.Model):
    gender = models.CharField(max_length=2, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    pre_existing_conditions = models.CharField(max_length=100, blank=True, null=True)
    tstamp = models.DateTimeField()
    patient = models.ForeignKey(UsermanagementC24Patient, models.DO_NOTHING)
    changes = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=100)
    relationship = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24patientprofilehistory'


class UsermanagementC24Provider(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField()
    service_offered = models.CharField(max_length=2)
    modified = models.DateTimeField()
    created = models.DateTimeField()
    gender = models.CharField(max_length=2)
    from_agency = models.ForeignKey('UsermanagementExternalagency', models.DO_NOTHING, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    residential_locality = models.ForeignKey(GeographyLocality, models.DO_NOTHING, blank=True, null=True)
    training_completed = models.BooleanField()
    more_info = models.TextField(blank=True, null=True)
    base_price = models.SmallIntegerField()
    onboarding_date = models.DateTimeField(blank=True, null=True)
    aph_cstat = models.CharField(max_length=3)
    ph_cstat = models.CharField(max_length=3)
    complete_raw_address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    unavailable_till = models.DateField(blank=True, null=True)
    uniform_size = models.CharField(max_length=3, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True)
    cg_lead = models.ForeignKey(TrainingandonboardingCglead, models.DO_NOTHING, blank=True, null=True)
    idfy_counter = models.IntegerField()
    c24_employment_type = models.CharField(max_length=2)
    payable_account = models.ForeignKey(AccountingAccount, models.DO_NOTHING, unique=True, blank=True, null=True)
    app_active = models.NullBooleanField()
    temporary_id_given = models.NullBooleanField()
    uniforms_given = models.SmallIntegerField(blank=True, null=True)
    cg_availability_status = models.CharField(max_length=2, blank=True, null=True)
    cg_status = models.SmallIntegerField(blank=True, null=True)
    address = models.ForeignKey(GeographyCareaddress, models.DO_NOTHING, unique=True, blank=True, null=True)
    idfy_invoice_no = models.CharField(max_length=100, blank=True, null=True)
    phone = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, unique=True, blank=True, null=True)
    alt_phone_0 = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, db_column='alt_phone_id', blank=True, null=True)  # Field renamed because of name conflict.
    known_for = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    marital_status = models.CharField(max_length=2)
    credit_limit = models.DecimalField(max_digits=16, decimal_places=2)
    ht_driver_id = models.UUIDField(blank=True, null=True)
    oust_training = models.BooleanField()
    religion = models.SmallIntegerField(blank=True, null=True)
    medical_skills_score = models.IntegerField(blank=True, null=True)
    soft_skills_score = models.IntegerField(blank=True, null=True)
    is_tracking_pending = models.BooleanField()
    tracking_attempts = models.IntegerField()
    app_payment = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'UserManagement_c24provider'


class UsermanagementC24ProviderHobbies(models.Model):
    c24provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING)
    providerhobbies = models.ForeignKey(ProviderpropsProviderhobbies, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24provider_hobbies'
        unique_together = (('c24provider', 'providerhobbies'),)


class UsermanagementC24ProviderServiceProcedure(models.Model):
    c24provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING)
    serviceprocedure = models.ForeignKey(ProviderpropsServiceprocedure, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24provider_service_procedure'
        unique_together = (('c24provider', 'serviceprocedure'),)


class UsermanagementC24ProviderServiceSpecialization(models.Model):
    c24provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING)
    servicespecialization = models.ForeignKey(ProviderpropsServicespecialization, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24provider_service_specialization'
        unique_together = (('c24provider', 'servicespecialization'),)


class UsermanagementC24ProviderServingLocalities(models.Model):
    c24provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING)
    localitytreenode = models.ForeignKey(GeographyLocalitytreenode, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24provider_serving_localities'
        unique_together = (('c24provider', 'localitytreenode'),)


class UsermanagementC24ProviderWillingToServeInLocalities(models.Model):
    c24provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING)
    locality = models.ForeignKey(GeographyLocality, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24provider_willing_to_serve_in_localities'
        unique_together = (('c24provider', 'locality'),)


class UsermanagementC24Team(models.Model):
    name = models.CharField(unique=True, max_length=40)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'UserManagement_c24team'


class UsermanagementC24Userteammap(models.Model):
    active = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    auth_user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    c24team = models.ForeignKey(UsermanagementC24Team, models.DO_NOTHING)
    team_role = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_c24userteammap'
        unique_together = (('auth_user', 'c24team', 'active'),)


class UsermanagementCareuser(models.Model):
    data = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    auth_user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)
    customer = models.ForeignKey(UsermanagementC24Customer, models.DO_NOTHING, unique=True, blank=True, null=True)
    phone = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, blank=True, null=True)
    provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_careuser'
        unique_together = (('auth_user', 'customer'), ('auth_user', 'provider'),)


class UsermanagementCollectiontracking(models.Model):
    status = models.SmallIntegerField()
    collection_date = models.DateTimeField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    customer = models.ForeignKey(UsermanagementC24Customer, models.DO_NOTHING)
    updated_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    call_status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    to_show = models.BooleanField()
    provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING, blank=True, null=True)
    reason = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_collectiontracking'


class UsermanagementExternalagency(models.Model):
    agency_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=128)
    allows_direct_contact = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'UserManagement_externalagency'


class UsermanagementLoginfo(models.Model):
    field_data = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_loginfo'


class UsermanagementPatientmeals(models.Model):
    meal_type = models.CharField(max_length=5)
    meal_time = models.TimeField(blank=True, null=True)
    patient = models.ForeignKey(UsermanagementC24Patient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_patientmeals'


class UsermanagementPayerinformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    created = models.DateField()
    modified = models.DateTimeField()
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey(UsermanagementC24Patient, models.DO_NOTHING)
    city = models.ForeignKey(GeographyCity, models.DO_NOTHING)
    email = models.CharField(max_length=50, blank=True, null=True)
    landmark = models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=128)
    pin_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_payerinformation'


class UsermanagementPhonenumbermanager(models.Model):
    is_primary = models.BooleanField()
    is_active = models.BooleanField()
    customer = models.ForeignKey(UsermanagementC24Customer, models.DO_NOTHING, blank=True, null=True)
    phone = models.ForeignKey(InteractionmanagerPhonenumber, models.DO_NOTHING, unique=True)
    provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    is_alternate = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'UserManagement_phonenumbermanager'
        unique_together = (('provider', 'phone'), ('customer', 'phone'),)


class UsermanagementProfile(models.Model):
    primary_phone = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'UserManagement_profile'


class UsermanagementProviderstatushistory(models.Model):
    status = models.SmallIntegerField(blank=True, null=True)
    emp_status = models.CharField(max_length=3, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    provider = models.ForeignKey(UsermanagementC24Provider, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserManagement_providerstatushistory'


class UsermanagementServicecreditlimit(models.Model):
    service = models.CharField(unique=True, max_length=2)
    credit_limit = models.DecimalField(max_digits=16, decimal_places=2)
    created = models.DateField()
    modified = models.DateTimeField()
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_servicecreditlimit'


class UsermanagementSocialmedialink(models.Model):
    typ = models.SmallIntegerField()
    user_id = models.CharField(max_length=64)
    email = models.CharField(max_length=254, blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    customer = models.ForeignKey(UsermanagementC24Customer, models.DO_NOTHING, blank=True, null=True)
    care_user = models.ForeignKey(UsermanagementCareuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserManagement_socialmedialink'
        unique_together = (('typ', 'user_id', 'care_user'), ('typ', 'user_id', 'customer'),)


class VitalsVital(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=20)
    min_value = models.CharField(max_length=10, blank=True, null=True)
    max_value = models.CharField(max_length=10, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Vitals_vital'


class VitalsVitallog(models.Model):
    value = models.CharField(max_length=10)
    update_time = models.DateTimeField()
    value_position = models.CharField(max_length=30)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    booking = models.ForeignKey(RequestbookingBooking, models.DO_NOTHING, blank=True, null=True)
    vital = models.ForeignKey(VitalsVital, models.DO_NOTHING)
    patient = models.ForeignKey(UsermanagementC24Patient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vitals_vitallog'
        unique_together = (('booking', 'vital', 'update_time'),)


class AccCollectionsBkp3Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    payment_to = models.CharField(max_length=4, blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)
    caregiver_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_collections_bkp_3sep'


class AccountingCollection13Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    payment_to = models.CharField(max_length=4, blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)
    caregiver_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_collection_13sep'


class AccountingPayments13Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    request_date = models.DateField(blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    process_date = models.DateField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    caregiver_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_payments_13sep'


class AccountingVisitCpa13Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    charge_fee = models.SmallIntegerField(blank=True, null=True)
    charge_equip_rent = models.SmallIntegerField(blank=True, null=True)
    charge_travel_a = models.SmallIntegerField(blank=True, null=True)
    charge_consumable_a = models.SmallIntegerField(blank=True, null=True)
    charge_other_a = models.SmallIntegerField(blank=True, null=True)
    pay_fee = models.SmallIntegerField(blank=True, null=True)
    pay_travel_a = models.SmallIntegerField(blank=True, null=True)
    pay_consumable_a = models.SmallIntegerField(blank=True, null=True)
    pay_other_a = models.SmallIntegerField(blank=True, null=True)
    penalty = models.SmallIntegerField(blank=True, null=True)
    incentive = models.SmallIntegerField(blank=True, null=True)
    discount = models.SmallIntegerField(blank=True, null=True)
    caregiver_invoice_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    customer_invoice_id = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)
    discount_remarks = models.TextField(blank=True, null=True)
    incentive_remarks = models.TextField(blank=True, null=True)
    penalty_remarks = models.TextField(blank=True, null=True)
    discount_type = models.SmallIntegerField(blank=True, null=True)
    incentive_type = models.SmallIntegerField(blank=True, null=True)
    penalty_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_visit_cpa_13sep'


class AccountingVisitCpa13SepTemp(models.Model):
    id = models.IntegerField(blank=True, null=True)
    charge_fee = models.SmallIntegerField(blank=True, null=True)
    charge_equip_rent = models.SmallIntegerField(blank=True, null=True)
    charge_travel_a = models.SmallIntegerField(blank=True, null=True)
    charge_consumable_a = models.SmallIntegerField(blank=True, null=True)
    charge_other_a = models.SmallIntegerField(blank=True, null=True)
    pay_fee = models.SmallIntegerField(blank=True, null=True)
    pay_travel_a = models.SmallIntegerField(blank=True, null=True)
    pay_consumable_a = models.SmallIntegerField(blank=True, null=True)
    pay_other_a = models.SmallIntegerField(blank=True, null=True)
    penalty = models.SmallIntegerField(blank=True, null=True)
    incentive = models.SmallIntegerField(blank=True, null=True)
    discount = models.SmallIntegerField(blank=True, null=True)
    caregiver_invoice_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    customer_invoice_id = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)
    discount_remarks = models.TextField(blank=True, null=True)
    incentive_remarks = models.TextField(blank=True, null=True)
    penalty_remarks = models.TextField(blank=True, null=True)
    discount_type = models.SmallIntegerField(blank=True, null=True)
    incentive_type = models.SmallIntegerField(blank=True, null=True)
    penalty_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_visit_cpa_13sep_temp'


class Actiondump(models.Model):
    id = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    task_description = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    delay_remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    assigned_team_id = models.IntegerField(blank=True, null=True)
    assigned_user_id = models.IntegerField(blank=True, null=True)
    serviceticket_id = models.IntegerField(blank=True, null=True)
    alt_assigned_team_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actiondump'


class AdvanceBkp3Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    no_of_visits = models.SmallIntegerField(blank=True, null=True)
    duration = models.SmallIntegerField(blank=True, null=True)
    price_negotiated = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    no_of_cg = models.SmallIntegerField(blank=True, null=True)
    service = models.CharField(max_length=2, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advance_bkp_3sep'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BillingCollection13Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    total_visits = models.IntegerField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    prev_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    invoice_status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    payment_received_date = models.DateField(blank=True, null=True)
    discount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    invoice_name = models.TextField(blank=True, null=True)
    invoice_identifier = models.TextField(blank=True, null=True)
    bad_debt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    previous_invoice_list = models.CharField(max_length=200, blank=True, null=True)
    invoice_stage = models.SmallIntegerField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_collection_13sep'


class BillingLedgerDet13Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    credit_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    debit_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    payment_type = models.SmallIntegerField(blank=True, null=True)
    created_by = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    collection_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    refund_id = models.IntegerField(blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    refund_type = models.SmallIntegerField(blank=True, null=True)
    invoice_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_ledger_det_13sep'


class BookId24Feb2015(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_id_24feb2015'


class BookingBkp0402017(models.Model):
    id = models.IntegerField(blank=True, null=True)
    patient_condition = models.CharField(max_length=255, blank=True, null=True)
    pref_gender = models.CharField(max_length=2, blank=True, null=True)
    pref_eating_habit = models.CharField(max_length=2, blank=True, null=True)
    price_negotiated = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_hour = models.SmallIntegerField(blank=True, null=True)
    estimated_visits = models.SmallIntegerField(blank=True, null=True)
    frequency = models.SmallIntegerField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    was_at_hosp_id = models.IntegerField(blank=True, null=True)
    for_lead_id = models.IntegerField(blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    duration = models.SmallIntegerField(blank=True, null=True)
    first_visit_at_hosp = models.NullBooleanField()
    service = models.CharField(max_length=2, blank=True, null=True)
    next_review = models.DateField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    nearest_landmark = models.CharField(max_length=100, blank=True, null=True)
    raw_address = models.TextField(blank=True, null=True)
    bstat = models.CharField(max_length=3, blank=True, null=True)
    pref_comm_channel = models.SmallIntegerField(blank=True, null=True)
    pref_comm_frequency = models.SmallIntegerField(blank=True, null=True)
    pref_payment_method = models.SmallIntegerField(blank=True, null=True)
    price_tenure = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=2, blank=True, null=True)
    status_reason = models.TextField(blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    duty_shift = models.SmallIntegerField(blank=True, null=True)
    no_of_caregivers = models.SmallIntegerField(blank=True, null=True)
    onboarding_timeslots = models.TextField(blank=True, null=True)
    onboarding_date = models.DateField(blank=True, null=True)
    onboarding_status = models.CharField(max_length=2, blank=True, null=True)
    onboarding_agent = models.TextField(blank=True, null=True)
    customer_estimated_days = models.IntegerField(blank=True, null=True)
    onboard_agent_id = models.IntegerField(blank=True, null=True)
    payment_method = models.SmallIntegerField(blank=True, null=True)
    discount_id = models.IntegerField(blank=True, null=True)
    allocation_end_date = models.DateField(blank=True, null=True)
    allocation_start_date = models.DateField(blank=True, null=True)
    payer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_bkp_0402017'


class BookingBkp11Jan2017(models.Model):
    id = models.IntegerField(blank=True, null=True)
    patient_condition = models.CharField(max_length=255, blank=True, null=True)
    pref_gender = models.CharField(max_length=2, blank=True, null=True)
    pref_eating_habit = models.CharField(max_length=2, blank=True, null=True)
    price_negotiated = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_hour = models.SmallIntegerField(blank=True, null=True)
    estimated_visits = models.SmallIntegerField(blank=True, null=True)
    frequency = models.SmallIntegerField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    was_at_hosp_id = models.IntegerField(blank=True, null=True)
    for_lead_id = models.IntegerField(blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    duration = models.SmallIntegerField(blank=True, null=True)
    first_visit_at_hosp = models.NullBooleanField()
    service = models.CharField(max_length=2, blank=True, null=True)
    next_review = models.DateField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    nearest_landmark = models.CharField(max_length=100, blank=True, null=True)
    raw_address = models.TextField(blank=True, null=True)
    bstat = models.CharField(max_length=3, blank=True, null=True)
    pref_comm_channel = models.SmallIntegerField(blank=True, null=True)
    pref_comm_frequency = models.SmallIntegerField(blank=True, null=True)
    pref_payment_method = models.SmallIntegerField(blank=True, null=True)
    price_tenure = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=2, blank=True, null=True)
    status_reason = models.TextField(blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    duty_shift = models.SmallIntegerField(blank=True, null=True)
    no_of_caregivers = models.SmallIntegerField(blank=True, null=True)
    onboarding_timeslots = models.TextField(blank=True, null=True)
    onboarding_date = models.DateField(blank=True, null=True)
    onboarding_status = models.CharField(max_length=2, blank=True, null=True)
    onboarding_agent = models.TextField(blank=True, null=True)
    customer_estimated_days = models.IntegerField(blank=True, null=True)
    onboard_agent_id = models.IntegerField(blank=True, null=True)
    payment_method = models.SmallIntegerField(blank=True, null=True)
    discount_id = models.IntegerField(blank=True, null=True)
    allocation_end_date = models.DateField(blank=True, null=True)
    allocation_start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_bkp_11jan2017'


class BookingIdLog(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_id_log'


class BookingPerformance(models.Model):
    booking_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    lead_id = models.IntegerField(blank=True, null=True)
    booking_creation = models.DateTimeField(blank=True, null=True)
    booking_status = models.CharField(max_length=40, blank=True, null=True)
    booking_service = models.CharField(max_length=40, blank=True, null=True)
    booking_price = models.SmallIntegerField(blank=True, null=True)
    discount_code = models.CharField(max_length=40, blank=True, null=True)
    first_cg_allocation_time = models.DateTimeField(blank=True, null=True)
    total_visits = models.IntegerField(blank=True, null=True)
    total_interview_visits = models.IntegerField(blank=True, null=True)
    total_visits_cancelled = models.IntegerField(blank=True, null=True)
    total_visits_completed = models.IntegerField(blank=True, null=True)
    total_visits_not_completed = models.IntegerField(blank=True, null=True)
    total_serving_cgs_allocated = models.IntegerField(blank=True, null=True)
    total_cgs_allocated = models.IntegerField(blank=True, null=True)
    total_premium_cg_visits = models.IntegerField(blank=True, null=True)
    total_app_cg_visits = models.IntegerField(blank=True, null=True)
    total_cg_payouts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_performance'


class BookingsPhysioMarch01(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookings_physio_march_01'


class BookingsTempPhysio(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookings_temp_physio'


class C24VisitTempDump03Feb2017(models.Model):
    id = models.IntegerField(blank=True, null=True)
    for_booking_id = models.IntegerField(blank=True, null=True)
    curr_status = models.SmallIntegerField(blank=True, null=True)
    cg_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c24_visit_temp_dump_03feb2017'


class C24Visit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    home_or_hospital = models.CharField(max_length=2, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    hours = models.SmallIntegerField(blank=True, null=True)
    curr_status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    cg_id = models.IntegerField(blank=True, null=True)
    for_booking_id = models.IntegerField(blank=True, null=True)
    cg_consumables = models.SmallIntegerField(blank=True, null=True)
    cg_fees = models.SmallIntegerField(blank=True, null=True)
    cg_travel = models.SmallIntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    allowance_transaction_id = models.IntegerField(blank=True, null=True)
    fee_transaction_id = models.IntegerField(blank=True, null=True)
    actual_end = models.DateTimeField(blank=True, null=True)
    actual_start = models.DateTimeField(blank=True, null=True)
    cg_remarks = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)  # This field type is a guess.
    vt_id = models.IntegerField(blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    shortlist_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c24visit'


class C24Visit24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    home_or_hospital = models.CharField(max_length=2, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    hours = models.SmallIntegerField(blank=True, null=True)
    curr_status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    cg_id = models.IntegerField(blank=True, null=True)
    for_booking_id = models.IntegerField(blank=True, null=True)
    cg_consumables = models.SmallIntegerField(blank=True, null=True)
    cg_fees = models.SmallIntegerField(blank=True, null=True)
    cg_travel = models.SmallIntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    allowance_transaction_id = models.IntegerField(blank=True, null=True)
    fee_transaction_id = models.IntegerField(blank=True, null=True)
    actual_end = models.DateTimeField(blank=True, null=True)
    actual_start = models.DateTimeField(blank=True, null=True)
    cg_remarks = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)  # This field type is a guess.
    vt_id = models.IntegerField(blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    shortlist_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c24visit_24feb'


class C24VisitIdsMarch01(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c24visit_ids_march01'


class C24VisitMarch01(models.Model):
    id = models.IntegerField(blank=True, null=True)
    home_or_hospital = models.CharField(max_length=2, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    hours = models.SmallIntegerField(blank=True, null=True)
    curr_status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    cg_id = models.IntegerField(blank=True, null=True)
    for_booking_id = models.IntegerField(blank=True, null=True)
    cg_consumables = models.SmallIntegerField(blank=True, null=True)
    cg_fees = models.SmallIntegerField(blank=True, null=True)
    cg_travel = models.SmallIntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    allowance_transaction_id = models.IntegerField(blank=True, null=True)
    fee_transaction_id = models.IntegerField(blank=True, null=True)
    actual_end = models.DateTimeField(blank=True, null=True)
    actual_start = models.DateTimeField(blank=True, null=True)
    cg_remarks = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)  # This field type is a guess.
    vt_id = models.IntegerField(blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    shortlist_type = models.CharField(max_length=20, blank=True, null=True)
    bfvt_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c24visit_march01'


class C24VisitPhysio24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    home_or_hospital = models.CharField(max_length=2, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    hours = models.SmallIntegerField(blank=True, null=True)
    curr_status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    cg_id = models.IntegerField(blank=True, null=True)
    for_booking_id = models.IntegerField(blank=True, null=True)
    cg_consumables = models.SmallIntegerField(blank=True, null=True)
    cg_fees = models.SmallIntegerField(blank=True, null=True)
    cg_travel = models.SmallIntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    allowance_transaction_id = models.IntegerField(blank=True, null=True)
    fee_transaction_id = models.IntegerField(blank=True, null=True)
    actual_end = models.DateTimeField(blank=True, null=True)
    actual_start = models.DateTimeField(blank=True, null=True)
    cg_remarks = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)  # This field type is a guess.
    vt_id = models.IntegerField(blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    shortlist_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c24visit_physio_24feb'


class C24Visitstatus24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    curr_status = models.SmallIntegerField(blank=True, null=True)
    hours = models.SmallIntegerField(blank=True, null=True)
    cg_fees = models.SmallIntegerField(blank=True, null=True)
    changes = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField(blank=True, null=True)
    cg_id = models.IntegerField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c24visitstatus_24feb'


class C24VisitstatusPhy24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    curr_status = models.SmallIntegerField(blank=True, null=True)
    hours = models.SmallIntegerField(blank=True, null=True)
    cg_fees = models.SmallIntegerField(blank=True, null=True)
    changes = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField(blank=True, null=True)
    cg_id = models.IntegerField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c24visitstatus_phy_24feb'


class CaregiverBkp(models.Model):
    id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.NullBooleanField()
    service_offered = models.CharField(max_length=2, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    from_agency_id = models.IntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    is_blacklisted = models.NullBooleanField()
    residential_locality_id = models.IntegerField(blank=True, null=True)
    training_completed = models.NullBooleanField()
    more_info = models.TextField(blank=True, null=True)
    base_price = models.SmallIntegerField(blank=True, null=True)
    onboarding_date = models.DateTimeField(blank=True, null=True)
    aph_cstat = models.CharField(max_length=3, blank=True, null=True)
    ph_cstat = models.CharField(max_length=3, blank=True, null=True)
    complete_raw_address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    unavailable_till = models.DateField(blank=True, null=True)
    uniform_size = models.CharField(max_length=3, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True)
    cg_lead_id = models.IntegerField(blank=True, null=True)
    idfy_counter = models.IntegerField(blank=True, null=True)
    c24_employment_type = models.CharField(max_length=2, blank=True, null=True)
    payable_account_id = models.IntegerField(blank=True, null=True)
    app_active = models.NullBooleanField()
    temporary_id_given = models.NullBooleanField()
    uniforms_given = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caregiver_bkp'


class CaregiverPerformance(models.Model):
    cg_id = models.IntegerField(blank=True, null=True)
    trained_status = models.CharField(max_length=40, blank=True, null=True)
    bgcheck_status = models.CharField(max_length=40, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    cg_status = models.CharField(max_length=40, blank=True, null=True)
    on_duty_flag = models.CharField(max_length=1, blank=True, null=True)
    first_duty_date = models.DateField(blank=True, null=True)
    last_duty_date = models.DateField(blank=True, null=True)
    app_flag = models.CharField(max_length=1, blank=True, null=True)
    total_completed_visits = models.IntegerField(blank=True, null=True)
    total_uncompleted_visits = models.IntegerField(blank=True, null=True)
    service = models.CharField(max_length=40, blank=True, null=True)
    idfy_status = models.CharField(max_length=40, blank=True, null=True)
    emp_type = models.CharField(max_length=40, blank=True, null=True)
    bankaccount_flag = models.CharField(max_length=2, blank=True, null=True)
    aadhar_flag = models.CharField(max_length=2, blank=True, null=True)
    address_proof_doc_flag = models.CharField(max_length=2, blank=True, null=True)
    residential_locality_flag = models.CharField(max_length=2, blank=True, null=True)
    shift_preference = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caregiver_performance'


class CgBookings24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cg_bookings_24feb'


class CgaccountBkp26102016(models.Model):
    id = models.IntegerField(blank=True, null=True)
    ac_num = models.CharField(max_length=20, blank=True, null=True)
    branch = models.CharField(max_length=200, blank=True, null=True)
    ifsc = models.CharField(max_length=15, blank=True, null=True)
    ac_type = models.CharField(max_length=2, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    bank_id = models.IntegerField(blank=True, null=True)
    for_cg_id = models.IntegerField(blank=True, null=True)
    is_verified = models.NullBooleanField()
    verified_by_id = models.IntegerField(blank=True, null=True)
    is_primary = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'cgaccount_bkp_26102016'


class Choices(models.Model):
    tbl = models.CharField(max_length=150, blank=True, null=True)
    field = models.CharField(max_length=150, blank=True, null=True)
    key = models.CharField(max_length=150, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choices'


class ChronographJob(models.Model):
    name = models.CharField(max_length=200)
    frequency = models.CharField(max_length=10)
    params = models.TextField(blank=True, null=True)
    command = models.CharField(max_length=200)
    args = models.CharField(max_length=200)
    disabled = models.BooleanField()
    next_run = models.DateTimeField(blank=True, null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    is_running = models.BooleanField()
    last_run_successful = models.BooleanField()
    lock_file = models.CharField(max_length=255)
    force_run = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'chronograph_job'


class ChronographJobSubscribers(models.Model):
    job = models.ForeignKey(ChronographJob, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chronograph_job_subscribers'
        unique_together = (('job', 'user'),)


class ChronographLog(models.Model):
    job = models.ForeignKey(ChronographJob, models.DO_NOTHING)
    run_date = models.DateTimeField()
    stdout = models.TextField()
    stderr = models.TextField()
    success = models.BooleanField()
    duration = models.FloatField()

    class Meta:
        managed = False
        db_table = 'chronograph_log'


class CollectionBkp12Dec2016(models.Model):
    id = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    total_visits = models.IntegerField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    prev_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    cheque_no = models.TextField(blank=True, null=True)
    invoice_status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    payment_received_date = models.DateField(blank=True, null=True)
    discount = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    invoice_name = models.TextField(blank=True, null=True)
    invoice_identifier = models.TextField(blank=True, null=True)
    bad_debt = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    previous_invoice_list = models.CharField(max_length=200, blank=True, null=True)
    invoice_stage = models.SmallIntegerField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection_bkp_12dec2016'


class CollectiontrackingBkp(models.Model):
    id = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    collection_date = models.DateTimeField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    updated_by_id = models.IntegerField(blank=True, null=True)
    call_status = models.SmallIntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    to_show = models.NullBooleanField()
    provider_id = models.IntegerField(blank=True, null=True)
    reason = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collectiontracking_bkp'


class CustomerBkpNullPhones(models.Model):
    id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    alt_phnum_id = models.IntegerField(blank=True, null=True)
    auth_user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phnum_id = models.IntegerField(blank=True, null=True)
    receivable_account_id = models.IntegerField(blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    payment_method = models.SmallIntegerField(blank=True, null=True)
    payment_mode = models.SmallIntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    onboarding_date = models.DateField(blank=True, null=True)
    onboarding_status = models.CharField(max_length=2, blank=True, null=True)
    pref_comm_channel = models.SmallIntegerField(blank=True, null=True)
    pref_comm_time = models.SmallIntegerField(blank=True, null=True)
    source = models.SmallIntegerField(blank=True, null=True)
    lead_type = models.SmallIntegerField(blank=True, null=True)
    advance_paying = models.NullBooleanField()
    onboard_agent_id = models.IntegerField(blank=True, null=True)
    ht_customer_id = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_bkp_null_phones'


class DTime(models.Model):
    date = models.DateField(blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
    month = models.FloatField(blank=True, null=True)
    monthname = models.TextField(blank=True, null=True)
    day = models.FloatField(blank=True, null=True)
    dayofyear = models.FloatField(blank=True, null=True)
    weekdayname = models.TextField(blank=True, null=True)
    calendarweek = models.FloatField(blank=True, null=True)
    quartal = models.TextField(blank=True, null=True)
    yearquartal = models.TextField(blank=True, null=True)
    yearmonth = models.TextField(blank=True, null=True)
    yearcalendarweek = models.TextField(blank=True, null=True)
    weekend = models.TextField(blank=True, null=True)
    monthstart = models.DateField(blank=True, null=True)
    monthend = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_time'


class DelAdvanceledger(models.Model):
    id = models.AutoField()
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2)
    credit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    debit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    advance_id = models.IntegerField()
    caregiver_id = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'del_advanceledger'


class DelCgAdvance(models.Model):
    id = models.AutoField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    type = models.SmallIntegerField()
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=16, decimal_places=2)
    total_installment = models.SmallIntegerField()
    first_installment_date = models.DateField(blank=True, null=True)
    last_installment_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver_id = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)
    emi_type = models.SmallIntegerField()
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'del_cg_advance'


class DelCgDeposit(models.Model):
    id = models.AutoField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    type = models.SmallIntegerField()
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=16, decimal_places=2)
    total_installment = models.SmallIntegerField()
    first_installment_date = models.DateField(blank=True, null=True)
    last_installment_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver_id = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)
    emi_type = models.SmallIntegerField()
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'del_cg_deposit'


class DelCgPayment(models.Model):
    id = models.AutoField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    payment_mode = models.SmallIntegerField()
    account_no = models.TextField(blank=True, null=True)
    ifsc_code = models.TextField(blank=True, null=True)
    reference_no = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    bank_name_id = models.IntegerField(blank=True, null=True)
    caregiver_id = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    payment_to = models.SmallIntegerField()
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'del_cg_payment'


class DelCgPayout(models.Model):
    id = models.AutoField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    total_visits = models.IntegerField()
    type = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver_id = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)
    total_fees = models.DecimalField(max_digits=16, decimal_places=2)
    total_incentive = models.DecimalField(max_digits=16, decimal_places=2)
    total_penalty = models.DecimalField(max_digits=16, decimal_places=2)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'del_cg_payout'


class DelCgincentive(models.Model):
    id = models.AutoField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver_id = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)
    transaction_date = models.DateField()
    cg_incentive_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'del_cgincentive'


class DelCgincentiveType(models.Model):
    id = models.AutoField()
    quant_count = models.CharField(max_length=25, blank=True, null=True)
    break_count = models.CharField(max_length=25, blank=True, null=True)
    is_valid = models.BooleanField()
    has_achieved = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver_id = models.IntegerField()
    incentive_desc_id = models.IntegerField(blank=True, null=True)
    amount_achieved = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'del_cgincentive_type'


class DelDepositledger(models.Model):
    id = models.AutoField()
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2)
    credit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    debit_amount = models.DecimalField(max_digits=16, decimal_places=2)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver_id = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)
    deposit_id = models.IntegerField()
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'del_depositledger'


class DelPenalty(models.Model):
    id = models.AutoField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    type = models.SmallIntegerField()
    remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    caregiver_id = models.IntegerField()
    created_by_id = models.IntegerField(blank=True, null=True)
    transaction_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'del_penalty'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HelpdeskAttachment(models.Model):
    file = models.CharField(max_length=1000)
    filename = models.CharField(max_length=1000)
    mime_type = models.CharField(max_length=255)
    size = models.IntegerField()
    followup = models.ForeignKey('HelpdeskFollowup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_attachment'


class HelpdeskCustomfield(models.Model):
    name = models.CharField(unique=True, max_length=50)
    label = models.CharField(max_length=30)
    help_text = models.TextField(blank=True, null=True)
    data_type = models.CharField(max_length=100)
    max_length = models.IntegerField(blank=True, null=True)
    decimal_places = models.IntegerField(blank=True, null=True)
    empty_selection_list = models.BooleanField()
    list_values = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    required = models.BooleanField()
    staff_only = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'helpdesk_customfield'


class HelpdeskEmailtemplate(models.Model):
    template_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    plain_text = models.TextField()
    html = models.TextField()
    locale = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helpdesk_emailtemplate'


class HelpdeskEscalationexclusion(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'helpdesk_escalationexclusion'


class HelpdeskEscalationexclusionQueues(models.Model):
    escalationexclusion = models.ForeignKey(HelpdeskEscalationexclusion, models.DO_NOTHING)
    queue = models.ForeignKey('HelpdeskQueue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_escalationexclusion_queues'
        unique_together = (('escalationexclusion', 'queue'),)


class HelpdeskFollowup(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    public = models.BooleanField()
    new_status = models.IntegerField(blank=True, null=True)
    ticket = models.ForeignKey('HelpdeskTicket', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helpdesk_followup'


class HelpdeskIgnoreemail(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    email_address = models.CharField(max_length=150)
    keep_in_mailbox = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'helpdesk_ignoreemail'


class HelpdeskIgnoreemailQueues(models.Model):
    ignoreemail = models.ForeignKey(HelpdeskIgnoreemail, models.DO_NOTHING)
    queue = models.ForeignKey('HelpdeskQueue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_ignoreemail_queues'
        unique_together = (('ignoreemail', 'queue'),)


class HelpdeskKbcategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'helpdesk_kbcategory'


class HelpdeskKbitem(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    votes = models.IntegerField()
    recommendations = models.IntegerField()
    last_updated = models.DateTimeField()
    category = models.ForeignKey(HelpdeskKbcategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_kbitem'


class HelpdeskPresetreply(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'helpdesk_presetreply'


class HelpdeskPresetreplyQueues(models.Model):
    presetreply = models.ForeignKey(HelpdeskPresetreply, models.DO_NOTHING)
    queue = models.ForeignKey('HelpdeskQueue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_presetreply_queues'
        unique_together = (('presetreply', 'queue'),)


class HelpdeskQueue(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=50)
    email_address = models.CharField(max_length=254, blank=True, null=True)
    locale = models.CharField(max_length=10, blank=True, null=True)
    allow_public_submission = models.BooleanField()
    allow_email_submission = models.BooleanField()
    escalate_days = models.IntegerField(blank=True, null=True)
    new_ticket_cc = models.CharField(max_length=200, blank=True, null=True)
    updated_ticket_cc = models.CharField(max_length=200, blank=True, null=True)
    email_box_type = models.CharField(max_length=5, blank=True, null=True)
    email_box_host = models.CharField(max_length=200, blank=True, null=True)
    email_box_port = models.IntegerField(blank=True, null=True)
    email_box_ssl = models.BooleanField()
    email_box_user = models.CharField(max_length=200, blank=True, null=True)
    email_box_pass = models.CharField(max_length=200, blank=True, null=True)
    email_box_imap_folder = models.CharField(max_length=100, blank=True, null=True)
    email_box_interval = models.IntegerField(blank=True, null=True)
    email_box_last_check = models.DateTimeField(blank=True, null=True)
    socks_proxy_type = models.CharField(max_length=8, blank=True, null=True)
    socks_proxy_host = models.GenericIPAddressField(blank=True, null=True)
    socks_proxy_port = models.IntegerField(blank=True, null=True)
    permission_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helpdesk_queue'


class HelpdeskSavedsearch(models.Model):
    title = models.CharField(max_length=100)
    shared = models.BooleanField()
    query = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_savedsearch'


class HelpdeskTicket(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    submitter_email = models.CharField(max_length=254, blank=True, null=True)
    status = models.IntegerField()
    on_hold = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    resolution = models.TextField(blank=True, null=True)
    priority = models.IntegerField()
    due_date = models.DateTimeField(blank=True, null=True)
    last_escalation = models.DateTimeField(blank=True, null=True)
    assigned_to = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    queue = models.ForeignKey(HelpdeskQueue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_ticket'


class HelpdeskTicketcc(models.Model):
    email = models.CharField(max_length=254, blank=True, null=True)
    can_view = models.BooleanField()
    can_update = models.BooleanField()
    ticket = models.ForeignKey(HelpdeskTicket, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helpdesk_ticketcc'


class HelpdeskTicketchange(models.Model):
    field = models.CharField(max_length=100)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    followup = models.ForeignKey(HelpdeskFollowup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_ticketchange'


class HelpdeskTicketcustomfieldvalue(models.Model):
    value = models.TextField(blank=True, null=True)
    field = models.ForeignKey(HelpdeskCustomfield, models.DO_NOTHING)
    ticket = models.ForeignKey(HelpdeskTicket, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_ticketcustomfieldvalue'


class HelpdeskTicketdependency(models.Model):
    depends_on = models.ForeignKey(HelpdeskTicket, models.DO_NOTHING)
    ticket = models.ForeignKey(HelpdeskTicket, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'helpdesk_ticketdependency'
        unique_together = (('ticket', 'depends_on'),)


class HelpdeskUsersettings(models.Model):
    settings_pickled = models.TextField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'helpdesk_usersettings'


class IntertmgrMissrec24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    phn_num = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intertmgr_missrec_24feb'


class IntertmgrMissrecPhy24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    phn_num = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intertmgr_missrec_phy_24feb'


class IntertmgrVtrec24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    call_sid = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    ivr_id = models.IntegerField(blank=True, null=True)
    reply = models.SmallIntegerField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)
    confirmation_type = models.SmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intertmgr_vtrec_24feb'


class IntertmgrVtrecPhy24Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    call_sid = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    ivr_id = models.IntegerField(blank=True, null=True)
    reply = models.SmallIntegerField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)
    confirmation_type = models.SmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intertmgr_vtrec_phy_24feb'


class LeadPerformance(models.Model):
    lead_id = models.IntegerField(blank=True, null=True)
    lead_service = models.CharField(max_length=40, blank=True, null=True)
    lead_type = models.CharField(max_length=40, blank=True, null=True)
    lead_status = models.CharField(max_length=40, blank=True, null=True)
    lead_closed_by = models.CharField(max_length=40, blank=True, null=True)
    lead_first_callback = models.DateTimeField(blank=True, null=True)
    lead_total_attempt_closure = models.IntegerField(blank=True, null=True)
    lead_creation = models.DateTimeField(blank=True, null=True)
    lead_closure = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead_performance'


class LedgerBkp12Dec2016(models.Model):
    id = models.IntegerField(blank=True, null=True)
    credit_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    debit_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    payment_type = models.SmallIntegerField(blank=True, null=True)
    created_by = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    collection_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    invoices_id = models.IntegerField(blank=True, null=True)
    refund_id = models.IntegerField(blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    refund_type = models.SmallIntegerField(blank=True, null=True)
    invoice_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ledger_bkp_12dec2016'


class MFinanceCpa(models.Model):
    date = models.DateField(blank=True, null=True)
    leads = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    cust_type = models.TextField(blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)
    discount_code = models.CharField(max_length=10, blank=True, null=True)
    discount_value = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    completed_visits = models.BigIntegerField(blank=True, null=True)
    cx_price = models.BigIntegerField(blank=True, null=True)
    cg_cost = models.BigIntegerField(blank=True, null=True)
    charge_fee = models.BigIntegerField(blank=True, null=True)
    charge_equip_rent = models.BigIntegerField(blank=True, null=True)
    charge_travel_a = models.BigIntegerField(blank=True, null=True)
    charge_consumable_a = models.BigIntegerField(blank=True, null=True)
    charge_other_a = models.BigIntegerField(blank=True, null=True)
    discount = models.BigIntegerField(blank=True, null=True)
    pay_fee = models.BigIntegerField(blank=True, null=True)
    pay_travel_a = models.BigIntegerField(blank=True, null=True)
    pay_consumable_a = models.BigIntegerField(blank=True, null=True)
    pay_other_a = models.BigIntegerField(blank=True, null=True)
    incentive = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_finance_cpa'


class Misreportdata(models.Model):
    id = models.AutoField()
    section = models.CharField(max_length=255, blank=True, null=True)
    sub_section = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    metrics = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    current_week = models.CharField(max_length=255, blank=True, null=True)
    previous_week = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'misreportdata'


class PaymentGatewayBkp3Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    merchant_id = models.TextField(blank=True, null=True)
    vendor_txn_id = models.TextField(blank=True, null=True)
    vendor_txn_status = models.TextField(blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vendor_txn_msg = models.TextField(blank=True, null=True)
    pg_txn_id = models.TextField(blank=True, null=True)
    issuer_ref_no = models.TextField(blank=True, null=True)
    auth_id_code = models.TextField(blank=True, null=True)
    txn_first_name = models.TextField(blank=True, null=True)
    txn_last_name = models.TextField(blank=True, null=True)
    pg_resp_code = models.TextField(blank=True, null=True)
    txn_address_zip = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vendor_signature = models.TextField(blank=True, null=True)
    txn_status = models.SmallIntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)
    advance_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_bkp_3sep'


class PaymentResponse13Sep(models.Model):
    id = models.IntegerField(blank=True, null=True)
    merchant_id = models.TextField(blank=True, null=True)
    vendor_txn_id = models.TextField(blank=True, null=True)
    vendor_txn_status = models.TextField(blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vendor_txn_msg = models.TextField(blank=True, null=True)
    pg_txn_id = models.TextField(blank=True, null=True)
    issuer_ref_no = models.TextField(blank=True, null=True)
    auth_id_code = models.TextField(blank=True, null=True)
    txn_first_name = models.TextField(blank=True, null=True)
    txn_last_name = models.TextField(blank=True, null=True)
    pg_resp_code = models.TextField(blank=True, null=True)
    txn_address_zip = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vendor_signature = models.TextField(blank=True, null=True)
    txn_status = models.SmallIntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)
    advance_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_response_13sep'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class ProviderBkp05Mar(models.Model):
    id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.NullBooleanField()
    service_offered = models.CharField(max_length=2, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    from_agency_id = models.IntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    is_blacklisted = models.NullBooleanField()
    residential_locality_id = models.IntegerField(blank=True, null=True)
    training_completed = models.NullBooleanField()
    more_info = models.TextField(blank=True, null=True)
    base_price = models.SmallIntegerField(blank=True, null=True)
    onboarding_date = models.DateTimeField(blank=True, null=True)
    aph_cstat = models.CharField(max_length=3, blank=True, null=True)
    ph_cstat = models.CharField(max_length=3, blank=True, null=True)
    complete_raw_address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    unavailable_till = models.DateField(blank=True, null=True)
    uniform_size = models.CharField(max_length=3, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True)
    cg_lead_id = models.IntegerField(blank=True, null=True)
    idfy_counter = models.IntegerField(blank=True, null=True)
    c24_employment_type = models.CharField(max_length=2, blank=True, null=True)
    payable_account_id = models.IntegerField(blank=True, null=True)
    app_active = models.NullBooleanField()
    temporary_id_given = models.NullBooleanField()
    uniforms_given = models.SmallIntegerField(blank=True, null=True)
    cg_availability_status = models.CharField(max_length=2, blank=True, null=True)
    cg_status = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_bkp_05mar'


class ProviderBkp18Feb2016(models.Model):
    id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.NullBooleanField()
    service_offered = models.CharField(max_length=2, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    from_agency_id = models.IntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    is_blacklisted = models.NullBooleanField()
    residential_locality_id = models.IntegerField(blank=True, null=True)
    training_completed = models.NullBooleanField()
    more_info = models.TextField(blank=True, null=True)
    base_price = models.SmallIntegerField(blank=True, null=True)
    onboarding_date = models.DateTimeField(blank=True, null=True)
    aph_cstat = models.CharField(max_length=3, blank=True, null=True)
    ph_cstat = models.CharField(max_length=3, blank=True, null=True)
    complete_raw_address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    unavailable_till = models.DateField(blank=True, null=True)
    uniform_size = models.CharField(max_length=3, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True)
    cg_lead_id = models.IntegerField(blank=True, null=True)
    idfy_counter = models.IntegerField(blank=True, null=True)
    c24_employment_type = models.CharField(max_length=2, blank=True, null=True)
    payable_account_id = models.IntegerField(blank=True, null=True)
    app_active = models.NullBooleanField()
    temporary_id_given = models.NullBooleanField()
    uniforms_given = models.SmallIntegerField(blank=True, null=True)
    cg_availability_status = models.CharField(max_length=2, blank=True, null=True)
    cg_status = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_bkp_18feb2016'


class ProviderBkp20160205(models.Model):
    id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.NullBooleanField()
    service_offered = models.CharField(max_length=2, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    from_agency_id = models.IntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    is_blacklisted = models.NullBooleanField()
    residential_locality_id = models.IntegerField(blank=True, null=True)
    training_completed = models.NullBooleanField()
    more_info = models.TextField(blank=True, null=True)
    base_price = models.SmallIntegerField(blank=True, null=True)
    onboarding_date = models.DateTimeField(blank=True, null=True)
    aph_cstat = models.CharField(max_length=3, blank=True, null=True)
    ph_cstat = models.CharField(max_length=3, blank=True, null=True)
    complete_raw_address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    unavailable_till = models.DateField(blank=True, null=True)
    uniform_size = models.CharField(max_length=3, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True)
    cg_lead_id = models.IntegerField(blank=True, null=True)
    idfy_counter = models.IntegerField(blank=True, null=True)
    c24_employment_type = models.CharField(max_length=2, blank=True, null=True)
    payable_account_id = models.IntegerField(blank=True, null=True)
    app_active = models.NullBooleanField()
    temporary_id_given = models.NullBooleanField()
    uniforms_given = models.SmallIntegerField(blank=True, null=True)
    cg_availability_status = models.CharField(max_length=2, blank=True, null=True)
    cg_status = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    service_polygon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_bkp_20160205'


class ProviderBkp25Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.NullBooleanField()
    service_offered = models.CharField(max_length=2, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    from_agency_id = models.IntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    is_blacklisted = models.NullBooleanField()
    residential_locality_id = models.IntegerField(blank=True, null=True)
    training_completed = models.NullBooleanField()
    more_info = models.TextField(blank=True, null=True)
    base_price = models.SmallIntegerField(blank=True, null=True)
    onboarding_date = models.DateTimeField(blank=True, null=True)
    aph_cstat = models.CharField(max_length=3, blank=True, null=True)
    ph_cstat = models.CharField(max_length=3, blank=True, null=True)
    complete_raw_address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    unavailable_till = models.DateField(blank=True, null=True)
    uniform_size = models.CharField(max_length=3, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True)
    cg_lead_id = models.IntegerField(blank=True, null=True)
    idfy_counter = models.IntegerField(blank=True, null=True)
    c24_employment_type = models.CharField(max_length=2, blank=True, null=True)
    payable_account_id = models.IntegerField(blank=True, null=True)
    app_active = models.NullBooleanField()
    temporary_id_given = models.NullBooleanField()
    uniforms_given = models.SmallIntegerField(blank=True, null=True)
    cg_availability_status = models.CharField(max_length=2, blank=True, null=True)
    cg_status = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_bkp_25feb'


class ProviderDump13Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.NullBooleanField()
    service_offered = models.CharField(max_length=2, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    from_agency_id = models.IntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    is_blacklisted = models.NullBooleanField()
    residential_locality_id = models.IntegerField(blank=True, null=True)
    training_completed = models.NullBooleanField()
    more_info = models.TextField(blank=True, null=True)
    base_price = models.SmallIntegerField(blank=True, null=True)
    onboarding_date = models.DateTimeField(blank=True, null=True)
    aph_cstat = models.CharField(max_length=3, blank=True, null=True)
    ph_cstat = models.CharField(max_length=3, blank=True, null=True)
    complete_raw_address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    unavailable_till = models.DateField(blank=True, null=True)
    uniform_size = models.CharField(max_length=3, blank=True, null=True)
    display_name = models.CharField(max_length=20, blank=True, null=True)
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True)
    cg_lead_id = models.IntegerField(blank=True, null=True)
    idfy_counter = models.IntegerField(blank=True, null=True)
    c24_employment_type = models.CharField(max_length=2, blank=True, null=True)
    payable_account_id = models.IntegerField(blank=True, null=True)
    app_active = models.NullBooleanField()
    temporary_id_given = models.NullBooleanField()
    uniforms_given = models.SmallIntegerField(blank=True, null=True)
    cg_availability_status = models.CharField(max_length=2, blank=True, null=True)
    cg_status = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_dump_13feb'


class ProviderPayoutData(models.Model):
    id = models.IntegerField(blank=True, null=True)
    base_price = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    ac_num = models.CharField(max_length=100, blank=True, null=True)
    bank_id = models.IntegerField(blank=True, null=True)
    payment_mode = models.IntegerField(blank=True, null=True)
    reference_no = models.CharField(max_length=100, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_payout_data'


class ProviderPhoneBkp(models.Model):
    id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.NullBooleanField()
    service_offered = models.CharField(max_length=2, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    from_agency_id = models.IntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    alt_phone = models.CharField(max_length=128, blank=True, null=True)
    residential_locality_id = models.IntegerField(blank=True, null=True)
    training_completed = models.NullBooleanField()
    more_info = models.TextField(blank=True, null=True)
    base_price = models.SmallIntegerField(blank=True, null=True)
    onboarding_date = models.DateTimeField(blank=True, null=True)
    aph_cstat = models.CharField(max_length=3, blank=True, null=True)
    ph_cstat = models.CharField(max_length=3, blank=True, null=True)
    complete_raw_address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    unavailable_till = models.DateField(blank=True, null=True)
    uniform_size = models.CharField(max_length=3, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    father_or_husband_name = models.CharField(max_length=100, blank=True, null=True)
    cg_lead_id = models.IntegerField(blank=True, null=True)
    idfy_counter = models.IntegerField(blank=True, null=True)
    c24_employment_type = models.CharField(max_length=2, blank=True, null=True)
    payable_account_id = models.IntegerField(blank=True, null=True)
    app_active = models.NullBooleanField()
    temporary_id_given = models.NullBooleanField()
    uniforms_given = models.SmallIntegerField(blank=True, null=True)
    cg_availability_status = models.CharField(max_length=2, blank=True, null=True)
    cg_status = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    idfy_invoice_no = models.CharField(max_length=100, blank=True, null=True)
    phone_id = models.IntegerField(blank=True, null=True)
    alt_phone_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provider_phone_bkp'


class Qrcdump(models.Model):
    id = models.IntegerField(blank=True, null=True)
    raised_by = models.SmallIntegerField(blank=True, null=True)
    category = models.SmallIntegerField(blank=True, null=True)
    priority = models.SmallIntegerField(blank=True, null=True)
    customer_mood = models.SmallIntegerField(blank=True, null=True)
    validity = models.NullBooleanField()
    status = models.SmallIntegerField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    action_plan = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    assigned_team_id = models.IntegerField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)
    caregiver_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    ticket_service = models.CharField(max_length=2, blank=True, null=True)
    ticket_active = models.DateTimeField(blank=True, null=True)
    ticket_source = models.SmallIntegerField(blank=True, null=True)
    alt_assigned_team_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qrcdump'


class RequestbookingBookingBkp15Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    patient_condition = models.CharField(max_length=255, blank=True, null=True)
    pref_gender = models.CharField(max_length=2, blank=True, null=True)
    pref_eating_habit = models.CharField(max_length=2, blank=True, null=True)
    price_negotiated = models.SmallIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_hour = models.SmallIntegerField(blank=True, null=True)
    estimated_visits = models.SmallIntegerField(blank=True, null=True)
    frequency = models.SmallIntegerField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    was_at_hosp_id = models.IntegerField(blank=True, null=True)
    for_lead_id = models.IntegerField(blank=True, null=True)
    patient_id = models.IntegerField(blank=True, null=True)
    duration = models.SmallIntegerField(blank=True, null=True)
    first_visit_at_hosp = models.NullBooleanField()
    service = models.CharField(max_length=2, blank=True, null=True)
    next_review = models.DateField(blank=True, null=True)
    created_by_id = models.IntegerField(blank=True, null=True)
    nearest_landmark = models.CharField(max_length=100, blank=True, null=True)
    raw_address = models.TextField(blank=True, null=True)
    bstat = models.CharField(max_length=3, blank=True, null=True)
    pref_comm_channel = models.SmallIntegerField(blank=True, null=True)
    pref_comm_frequency = models.SmallIntegerField(blank=True, null=True)
    pref_payment_method = models.SmallIntegerField(blank=True, null=True)
    price_tenure = models.SmallIntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=2, blank=True, null=True)
    status_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requestbooking_booking_bkp_15feb'


class RequestbookingBookingstatusBkp15Feb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=3, blank=True, null=True)
    changes = models.CharField(max_length=150, blank=True, null=True)
    tstamp = models.DateTimeField(blank=True, null=True)
    booking_id = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requestbooking_bookingstatus_bkp_15feb'


class SaifMisReport(models.Model):
    city = models.CharField(max_length=25, blank=True, null=True)
    metric = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    month_1 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_2 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_3 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_4 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_5 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_6 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_7 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_8 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_9 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_10 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_11 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    month_12 = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saif_mis_report'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class UllasDump(models.Model):
    phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ullas_dump'


class VisitcpaBkp12Dec2016(models.Model):
    id = models.IntegerField(blank=True, null=True)
    charge_fee = models.SmallIntegerField(blank=True, null=True)
    charge_equip_rent = models.SmallIntegerField(blank=True, null=True)
    charge_travel_a = models.SmallIntegerField(blank=True, null=True)
    charge_consumable_a = models.SmallIntegerField(blank=True, null=True)
    charge_other_a = models.SmallIntegerField(blank=True, null=True)
    pay_fee = models.SmallIntegerField(blank=True, null=True)
    pay_travel_a = models.SmallIntegerField(blank=True, null=True)
    pay_consumable_a = models.SmallIntegerField(blank=True, null=True)
    pay_other_a = models.SmallIntegerField(blank=True, null=True)
    penalty = models.SmallIntegerField(blank=True, null=True)
    incentive = models.SmallIntegerField(blank=True, null=True)
    discount = models.SmallIntegerField(blank=True, null=True)
    caregiver_invoice_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    customer_invoice_id = models.IntegerField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    visit_id = models.IntegerField(blank=True, null=True)
    discount_remarks = models.TextField(blank=True, null=True)
    incentive_remarks = models.TextField(blank=True, null=True)
    penalty_remarks = models.TextField(blank=True, null=True)
    discount_type = models.SmallIntegerField(blank=True, null=True)
    incentive_type = models.SmallIntegerField(blank=True, null=True)
    penalty_type = models.SmallIntegerField(blank=True, null=True)
    discount_code_id = models.IntegerField(blank=True, null=True)
    caregiver_payout_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitcpa_bkp_12dec2016'


class Weekclassification(models.Model):
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    weekname = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weekclassification'
