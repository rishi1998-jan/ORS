

from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORS.utility.DataValidator import DataValidator
from service.models import Faculty
from service.forms import FacultyForm
from service.service.AddFacultyService import AddFacultyService

class AddFacultyListCtl(BaseCtl):
         
    # Populate Form from HTTP Request
    def request_to_form(self, requestForm):
        # self.form["id"] = requestForm.get("id", None)
        self.form["firstName"] = requestForm.get("firstName", None)
        self.form["lastName"] = requestForm.get("lastName", None)
        self.form["email"] = requestForm.get("email", None)
        self.form["password"] = requestForm.get("password", None)
        # self.form["mobileNumber"] = requestForm.get("mobileNumber", None)
        self.form["address"] = requestForm.get("address", None)
        self.form["gender"] = requestForm.get("gender", None)
        self.form["dob"] = requestForm.get("dob", None)
        self.form["college_ID"] = requestForm.get("college_ID", None)
        self.form["subject_ID"] = requestForm.get("subject_ID", None)
        self.form["subjectName"] = requestForm.get("subjetName", None)
        self.form["course_ID"] = requestForm.get("course_ID", None)
        self.form["courseName"] = requestForm.get("courseName", None)
        
   

        # Display College page

    def display(self, request, params={}):
        self.page_list = self.get_service().search(self.form)
        res = render(request, self.get_template(), {"pageList": self.page_list})
        return res

    def submit(self, request, params={}):
        self.request_to_form(request.POST)
        self.page_list = self.get_service().search(self.form)
        res = render(request, self.get_template(), {"pageList": self.page_list, "form": self.form})
        return res

    # Template html of Role page    
    def get_template(self):
        return "ors/AddFacultyList.html"

        # Service of Role

    def get_service(self):
        return AddFacultyService()


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
