

from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORS.utility.DataValidator import DataValidator
from service.forms import TimeTableForm
from service.models import TimeTable
from service.service.TimeTableService import TimeTableService

class TimeTableListCtl(BaseCtl):

    def request_to_form(self,requestForm):
        # self.form["examTime"]=requestForm.get("examTime",None)
        self.form["examDate"]=requestForm.get("examDate",None)
        self.form["subject_ID"]=requestForm.get("subject_ID",None)
        self.form["subjectName"]=requestForm.get("subjectName",None)
        self.form["course_ID"]=requestForm.get("course_ID",None)
        self.form["courseName"]=requestForm.get("courseName",None)
        self.form["semester"]=requestForm.get("semester",None)

    def display(self,request,params={}):
        self.page_list = self.get_service().search(self.form)
        res = render(request,self.get_template(),{"pageList":self.page_list})
        return res

    def submit(self,request,params={}):
        self.request_to_form(request.POST)
        self.page_list = self.get_service().search(self.form)
        res = render(request,self.get_template(),{"pageList":self.page_list, "form":self.form})
        return res
        
    def get_template(self):
        return "ors/TimeTableList.html"          

    # Service of Marksheet     
    def get_service(self):
        return TimeTableService()        

    def deleteRecord(self,request,params={}):
        self.page_list = self.get_service().search(self.form)
        print("--------------->------------->")
        if( params["id"] > 0):
            r = self.get_service().get(params["id"])
        
            if r is not None:
                self.get_service().delete(r.id)
                self.form["error"] = False
                self.form["message"] = "Data is delete"
                res = render(request,self.get_template(),{"pageList":self.page_list})
            else:
                self.form["error"] = False
                self.form["message"] = "Data is not delete"
                res = render(request,self.get_template(),{"pageList":self.page_list})
        return res 



