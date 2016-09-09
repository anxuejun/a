from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect
from django .contrib.auth import authenticate,login,logout
from django .contrib.auth.decorators import login_required
import models

# Create your views here.
def index(request):

    return  render(request,'index.html')






def dashboard(request):
    if request.method == 'GET':
        ret = {}
        ret['step_1'] = models.Asset.objects.filter(asset_type=0).count()
        ret['step_2'] = models.Asset.objects.filter(asset_type=1).count()
        ret['step_3'] = models.Asset.objects.filter(asset_type=2).count()
        ret['step_4'] = models.Asset.objects.filter(asset_type=3).count()
        ret['step_5'] = models.Asset.objects.filter(asset_type=4).count()
        ret['step_6'] = models.Asset.objects.filter(asset_type=5).count()

        return render(request, 'dashboard.html', {"ret":ret})
