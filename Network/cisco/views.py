from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Device_IP, ImageModel, Server
from  .forms import DeviceIPForm
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q # Search Datbase task
from django.db import connection
from django.conf import settings
import xlwt
from django.contrib.auth.models import User
from tablib import Dataset
from .resources import  DeviceIPResource

# Create your views here.


class IndexClass(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        Datas = {'DevcieIP': Device_IP.objects.all()}
        return render(request, 'cisco/home.html', Datas)

    def post(self, request):
        pass


class LoginClass(View):
    def get(self,request):
        return render(request, 'cisco/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        UserWeb = authenticate(username=username,password=password)
        if UserWeb is None:
            return render(request, 'cisco/loginfail.html')
        login(request, UserWeb)
        return redirect('/home')


class LogoutClass(View):
    def get(self,request):
        logout(request)
        return redirect('/login')


class ControlSite(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        return render(request, 'cisco/controlsite.html')

    def post(self, request):
        pass


class HomeClass(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        Datas = {'DevcieIP':Device_IP.objects.order_by('status','name')}
        # Datas = {'DevcieIP':Device_IP.objects.all()}
        return render(request, 'cisco/home.html',Datas)

    def post(self, request):
        return HttpResponse('Come back Home!')


class AddeviceClass(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        FormDevice = DeviceIPForm()
        return render(request, 'cisco/addevice.html', {'f':FormDevice})

    def post(self, request):
        DataForm = DeviceIPForm(request.POST)
        print(DataForm)
        if DataForm.is_valid():
            try:
                DataForm.save()
                return redirect('/home')
            except:
                pass
        else:

            pass


class AboutClass(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        ImageMe = ImageModel.objects.all()
        return render(request, 'cisco/about.html', {'im':ImageMe})

    def post(self, request):
        pass

@decorators.login_required(login_url='/login/')
def delete(request, id):
    IpDevice = Device_IP.objects.get(id=id)
    IpDevice.delete()
    return redirect('/home')
    
@decorators.login_required(login_url='/login/')
def edit(request, id):
    IpDevice = Device_IP.objects.get(id=id)
    return render(request,'cisco/edit.html', {'IDe':IpDevice})

def update(request, id):
    deviceIP = get_object_or_404(Device_IP, id=id)
    print(deviceIP)
    if request.method == 'GET':
        form = DeviceIPForm(instance=deviceIP)
        return redirect("/home")
    else:
        form = DeviceIPForm(request.POST, instance=deviceIP)
        
        # form.save(commit=False)
        # form.EnableMonitor =True
        form.save()
        return redirect("/home")


class SearchResultsView(ListView):
    model = Device_IP
    template_name = 'cisco/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Device_IP.objects.filter(
            Q(name__icontains=query) | Q(ip__icontains=query) | Q(status__icontains=query)| Q(description__icontains=query)
        )
        return object_list


class CSVPageView(TemplateView):
    template_name = "cisco/excel_home.html"

def export_users_xls(request):

    response = HttpResponse(content_type='application/ms-excel') # return excel thay vì https.
    response['Content-Disposition'] = 'attachment; filename="device.xls"' # đặt tên và download lại file excel.

    wb = xlwt.Workbook(encoding='utf-8') # Tạo workbook với bộ giải mã utf-8
    ws = wb.add_sheet('Device Data') # this will make a sheet named Users Data

    # Sheet header, first row
    # Xử lý với hàng đầu tiên trong excel
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True # tạo kiểu chữ đậm.

    columns = ['name', 'ip','status', 'description','EnableMonitor',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Device_IP.objects.all().values_list('name', 'ip','status', 'description','EnableMonitor')
    print(rows)
    print(type(rows))
    # xử lý với dữ liệu đầu tiên.
    for row in rows:
        print()
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


class settings(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self,request):
        return render(request, 'cisco/settings.html')

    def post(self, request):
        # name = request.POST.get('name')
        # print(name)
        if 'export' in request.POST:
            print('export')
            return redirect('export/excel')
        elif 'myfile' in request.POST:
            print('import')
            return redirect('import')
        else:
            pass


@decorators.login_required(login_url='/login/')

def simple_upload(request):
    if request.method == 'POST':
        device_resource = DeviceIPResource()
        dataset = Dataset()
        new_devices = request.FILES['myfile']

        imported_data = dataset.load(new_devices.read())
        result = device_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            device_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'cisco/settings.html')
 

class Monitor(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        # Datas = {'DevcieIP':Device_IP.objects.order_by('status','name')}
        MonitorData = {'Monitors':Server.objects.all()}
        return render(request, 'cisco/monitor.html',MonitorData)

    def post(self, request):
        return HttpResponse('Come back Home!')