from django.contrib import admin
from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.utils.html import format_html

@admin.register(EmployeeRole)
class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ('RoleName',)
    search_fields = ('RoleName',)
    list_filter = ('RegisteredDate',)
    fieldsets = (
        (None, {
            'fields': ('RoleName',)
        }),

    )
@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('DomainName', )
    search_fields = ('DomainName',)
    list_filter = ('RegisteredDate',)
    fieldsets = (
        (None, {
            'fields': ('DomainName',)
        }),

    )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('LastName', 'FirstName', 'PhoneNumber','RegisteredDate','LastUpdated', 'Email', 'AddressedTo', 'status')
    search_fields = ('FirstName', 'LastName', 'PhoneNumber', 'Email')
    list_filter = ('RegisteredDate', 'LastUpdated', 'status')
    list_editable = ('status','AddressedTo',)
    readonly_fields = ('RegisteredDate', 'LastUpdated')
    date_hierarchy = 'RegisteredDate'
    save_on_top = True
    list_per_page = 8
    list_max_show_all = 8
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    empty_value_display = '-empty-'
    show_full_result_count = False
    list_select_related = True
    fieldsets = (
        (None, {
            'fields': ('FirstName', 'LastName', 'PhoneNumber', 'Email', 'AddressedTo', 'status')
        }),
   
    )
class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ('Position', 'Phone1', 'Phone2', 'Station', 'RegisteredDate', 'LastUpdated')   
    list_filter = ('Station',)  
    search_fields = ('Position', 'Phone1', 'Phone2', 'Station')  
    ordering = ('Position',) 
    save_as = True 
    save_on_top = True
    show_full_result_count = True
    actions_on_top = True 
    ordering = ['Position'] 
    list_max_show_all = 9
    list_per_page=9
    list_editable = ['Phone1', 'Phone2', 'Station']  # Allow inline editing of 'Type' field
  

class AfflictionAdmin(admin.ModelAdmin):
    list_display = ['Firstname', 'Middlename', 'Fullname', 'Incident', 'Amount', 'RegisteredDate', 'Date', 'view_report_icon']
    search_fields = ['Date','Firstname', 'Middlename', 'Fullname', 'Incident', 'Amount']
    list_filter = ['Incident', 'RegisteredDate', 'Date']
    date_hierarchy='RegisteredDate'
    save_as = True 
    save_on_top = True
    show_full_result_count = True
    actions_on_top = True 
    list_max_show_all = 9
    list_per_page=9  
    ordering = ['Firstname'] 
    list_editable = ['Incident'] 
   
    list_max_show_all = 10    
    def view_report_icon(self, obj):
        if obj.Report:
            return format_html('<a href="{0}" download title="Download Report"><i class="fas fa-file-alt text-success"></i></a>', obj.Report.url)  # Change the class to the desired Font Awesome icon
        else:
            return None   
    view_report_icon.short_description = 'Document'   


#class hii inarekodi Vikao kazi vya weredi kila wiki/dharura n.k
class WorkMeetingAdmin(admin.ModelAdmin):
    list_display = ['DateTime','Type', 'ChairMan', 'RegisteredDate', 'LastUpdated','view_report_icon']
    search_fields = ['Type', 'DateTime', 'ChairMan']
    list_filter = ['Type', 'RegisteredDate','DateTime' ]
    save_as = True 
    save_on_top = True
    show_full_result_count = True
    actions_on_top = True 
    ordering = ['ChairMan'] 
    list_max_show_all = 9
    list_per_page=9
    list_editable = ['Type'] 
    def view_report_icon(self, obj):
        if obj.Report:
            return format_html('<a href="{0}" download title="Download Report"><i class="fas fa-file-alt text-dark"></i></a>', obj.Report.url)  # Change the class to the desired Font Awesome icon
        else:
            return None   
    view_report_icon.short_description = 'Report Document'   
 
class MahudhurioAdmin(admin.ModelAdmin):
   
    list_display = ('CheckNumber', 'MeetingDate', 'Firstname', 'LastName', 'Unit', 'PhoneNumber','MeetingType')
    list_filter = ('MeetingDate','Firstname', 'LastName', 'Unit', 'PhoneNumber','CheckNumber')
    search_fields = ('Firstname', 'LastName', 'Unit', 'PhoneNumber')
    date_hierarchy = 'MeetingDate'
    readonly_fields = ('RegisteredDate', 'LastUpdated',)
    list_editable = ['MeetingType','Unit'] 
   # raw_id_fields = ('',)  # Add this line to specify the ForeignKey field

    fieldsets = (
        (None, {
            'fields': ('CheckNumber', )
        }),
        ('Personal Information', {
            'fields': ('Firstname', 'MiddleName', 'LastName', 'PhoneNumber',)
        }),
       
          ('Meeting Type & Unit', {
            'fields': ('MeetingType','Unit','MeetingDate')
        }),
           ('Additional Information', {
            'fields': ('LastUpdated','RegisteredDate')
        })
    )

admin.site.register(Mahudhurio, MahudhurioAdmin)
admin.site.register(Type)

#Registration
admin.site.register(Unit)
admin.site.register(AfflictionType)
admin.site.register(Affliction, AfflictionAdmin)
admin.site.register(WorkMeeting, WorkMeetingAdmin)
 