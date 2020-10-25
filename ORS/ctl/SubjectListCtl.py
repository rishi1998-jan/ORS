

from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render,redirect
from ORS.utility.DataValidator import DataValidator
from service.forms import SubjectForm
from service.models import Subject
from service.service.SubjectService import SubjectService  

class SubjectListCtl(BaseCtl):

    def request_to_form(self,requestForm):
        self.form["subjectName"]=requestForm.get("subjectName",None)
        self.form["subjectDescription"]=requestForm.get("subjectDescription",None)
        self.form["dob"]=requestForm.get("dob",None)
        self.form["course_ID"]=requestForm.get("course_ID",None)
        self.form["courseName"]=requestForm.get("courseName",None)
        # self.form["college_ID"]=requestForm.get("college_ID",None)
        # self.form["collegeName"]=requestForm.get("collegeName",None)

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
        return "ORS/SubjectList.html"          

    # Service of Marksheet     
    def get_service(self):
        return SubjectService()        

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
