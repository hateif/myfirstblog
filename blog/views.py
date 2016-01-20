from django.shortcuts import render

# Create your views here.

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

#def simple_chart(request):
    #plot = figure()
    #plot.circle([1,2], [3,4])

    #script, div = components(plot, CDN)

    #return render(request, "blog/simple_chart.html", {"the_script":script, "the_div":div})

from bokeh.models import Range1d

def simple_chart(request):

    if request.method == "POST":



        return HttpResponse('POST ok!')
    else:
        # create some data
        x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y1 = [0, 8, 2, 4, 6, 9, 5, 6, 25, 28, 4, 7]
        x2 = [2, 5, 7, 15, 18, 19, 25, 28, 9, 10, 4]
        y2 = [2, 4, 6, 9, 15, 18, 0, 8, 2, 25, 28]
        x3 = [0, 1, 0, 8, 2, 4, 6, 9, 7, 8, 9]
        y3 = [0, 8, 4, 6, 9, 15, 18, 19, 19, 25, 28]




    # select the tools we want
    TOOLS="pan,wheel_zoom,box_zoom,reset,save"

    # the red and blue graphs will share this data range
    xr1 = Range1d(start=0, end=30)
    yr1 = Range1d(start=0, end=30)

    # only the green will use this data range
    xr2 = Range1d(start=0, end=30)
    yr2 = Range1d(start=0, end=30)

    # build our figures
    p1 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
    p1.scatter(x1, y1, size=12, color="red", alpha=0.5)

    p2 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
    p2.scatter(x2, y2, size=12, color="blue", alpha=0.5)

    p3 = figure(x_range=xr2, y_range=yr2, tools=TOOLS, plot_width=300, plot_height=300)
    p3.scatter(x3, y3, size=12, color="green", alpha=0.5)

    # plots can be a single Bokeh Model, a list/tuple, or even a dictionary
    plots = {'Red': p1, 'Blue': p2, 'Green': p3}

    script, div = components(plots)

    return render(request, "blog/simple_chart.html", {"the_script":script, "the_div":div})



#--------------------------------------

def post_list(request):
    return render(request, 'blog/post_list.html', {})



#--------------------------------------
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExamInfoForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ExamInfoForm(request.POST)
        if form.is_valid():
            exam_info = form.save()
            exam_info.save()
            return HttpResponse('Thank you')
    else:
        form = ExamInfoForm()
    return render(request, 'blog/exam.html', {'form_info': form})




#-------------
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from compute import computecsvfile

import pandas as pd
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure
#from matplotlib.dates import DateFormatter

# Create your views here.
def register(request):
    if request.method == "POST":
        #if !reflag:
            uf = UserForm(request.POST,request.FILES)
            if uf.is_valid():

                username = uf.cleaned_data['username']
                headImg = uf.cleaned_data['headImg']
                user = User()
                user.username = username
                user.headImg = headImg
                user.save()
                #return HttpResponse('upload ok!')
                #colnames = ['time', 'value', 'status']
                #colnames2 = ['time', 'value']
                #data_df = pd.read_csv(headImg, parse_dates=['time'],header=None,names=colnames,index_col='time')
                #data_df = pd.read_csv(headImg, header=None,names=colnames2,index_col='time')
                #data_df = pd.DataFrame(data_df)
                #fig = Figure()
                #ax = fig.add_subplot(111)
                #data_df.plot(ax=ax)
                #canvas = FigureCanvas(fig)
                #response = HttpResponse(content_type='image/png')
                #canvas.print_png(response)
                #return response

                result, script, div= computecsvfile(headImg.name)
                #reflag = True

                return render(request, 'blog/register.html', {"uf":uf, "the_script":script, "the_div":div, "result":result, "filename": headImg.name,"teststr":'upload ok!'})
        #else:



    else:
        uf = UserForm()
    return render(request, 'blog/register.html',{'uf':uf})



#---------------------------------
from .models import Average
def numcompute(request):
    form = Average(forms.Form)
    filename = None  # default
    if request.method == 'POST':

        # Save uploaded file on server if it exists and is valid
        if request.files:
            file = request.files[form.filename.name]
            if file and allowed_file(file.filename):
                # Make a valid version of filename for any file ystem
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                       filename))

        result = compute_mean_std(filename)
    else:
        result = None

    return render_template("blog/compute.html", form=form, result=result)
