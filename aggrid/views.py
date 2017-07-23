# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from aggrid.models import *

from django.template import loader 

from django.db import connection

from django.http import JsonResponse, HttpResponse
# Create your views here.

def dictfetchall(cursor):
	columns = [col[0] for col in cursor.description]
	return [
		dict(zip(columns, row))
		for row in cursor.fetchall()
	]


latest_visits = (""" 
					select (rbc.id) as id,
					(case when curr_status = '0' then 'TESTING DO NOT USE'when curr_status = '1' then 'Scheduled'
					when curr_status = '2' then 'Ongoing'
					when curr_status = '3' then 'Completed'
					when curr_status = '-1' then 'Cancelled Cust'
					when curr_status = '-2' then 'Cancelled Prov'
					when curr_status = '-3' then 'Cancelled C24'
					when curr_status = '-4' then 'Bad Prov Not Reached'
					when curr_status = '-5' then 'Bad LastMoment Cancellation Cust'
					when curr_status = '-6' then 'Bad LastMoment Cancellation Prov'
					when curr_status = '-7' then 'Half-Day'
					when curr_status = '-8' then 'Booking Cancelled'
					when curr_status = '-9' then 'Bad Cust Cancelled MISSEDCALL'
					when curr_status = '-10' then 'Bad Prov Cancelled IVR'
					when curr_status = '4' then 'Paid Leave' else 'unknown' end ) as status,
					umc.id as cust_id,umc.first_name||' '||coalesce(umc.last_name,'') as cust_name,
					umcp.id cg_id,umcp.first_name||' '||coalesce(umcp.last_name,'') as cg_name,
					(case when rbb.service = 'N' then 'Nurse Sister+Brother'
					when rbb.service = 'A' then 'Attendant Aaya+Wardboy'
					when rbb.service = 'P' then 'Physiotherapist'
					when rbb.service = 'Nu' then 'Nutritionist'
					when rbb.service = 'Eq' then 'Equipment'
					when rbb.service = 'Ic' then 'InfantCare'
					when rbb.service = 'St' then 'Speech Therapy'
					when rbb.service = 'Ot' then 'Occupational Therapy'
					when rbb.service = 'Cp' then 'Clinical Psychology'
					when rbb.service = 'On' then 'Onco Nurse'
					when rbb.service = 'Cc' then 'Cancer Coach'
					when rbb.service = 'Pc' then 'Pregnancy Care'
					when rbb.service = 'Ph' then 'Pharmacy'
					when rbb.service = 'Cm' then 'Consumables'
					when rbb.service = 'D' then 'Diagnostics'
					when rbb.service = 'Py' then 'Physician'
					 else 'Unknown'
					 end) service ,to_char(date_time+interval'5:30','dd/mm/yyyy') as date, charge_fee,
					charge_equip_rent,
					charge_travel_a,
					charge_consumable_a,
					charge_other_a,
					pay_fee as cg_fees,
					pay_travel_a,
					pay_consumable_a,
					pay_other_a,
					penalty,
					incentive,
					discount,rbc.duration,(case when duty_shift = '1' then 'Day'
					when duty_shift = '2' then 'Night'
					when duty_shift = '3' then '24-Hour'
					when duty_shift = '4' then 'Intervention' else null end) duty_shift,closing_balance,discount_value,code,rbb.id as booking_id,
					(case when region_id  = 2 then 'delhi' else 'mumbai' end) as city


					 from "RequestBooking_booking" rbb
					join "UserManagement_c24patient" ump on rbb.patient_id = ump.id 
					join  "UserManagement_c24customer" umc on ump.customer_id = umc.id
					join  "RequestBooking_c24visit" rbc on rbb.id = rbc.for_booking_id  
					join  "Accounting_visitcpavalues" acv on rbc.id = acv.visit_id  
					join "UserManagement_c24provider" umcp on rbc.cg_id =  umcp.id
					left join (SELECT  a.customer_id,date(modified+interval'5:30') as modified,closing_balance from "Billing_ledgerdetail" a
					        join (select customer_id, max(modified) max from "Billing_ledgerdetail" group by customer_id) b
					        on a.customer_id = b.customer_id and a.modified = b.max)a on umc.id  = a.customer_id 
					left join  "Discounts_discountmaster"  ddm on rbc.discount_id = ddm.id 
					join "Geography_careaddress" gca on rbc.address_id = gca.id
					join  "Geography_city" gc on gca.city_id =gc.id
					where(date_time at time zone 'Asia/Calcutta')::date between '2017-04-01' and '2017-04-30'
					order by date_time 
					""")

def index(request):	
	template = loader.get_template('aggrid/index.html')
	context = {
		'latest_visits': latest_visits,
	}
	return HttpResponse(template.render(context, request))

	
def agdu(request):
	cursor = connection.cursor()
	cursor.execute(latest_visits)
	return JsonResponse({
		"data": dictfetchall(cursor),
		"status": True
	})
