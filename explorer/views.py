from django.shortcuts import render
from .models import County, VisitedCounty

# Create your views here.
def dashboard(request):

    total_counties = County.objects.count()

    visited_counties = VisitedCounty.objects.filter(user=request.user).count()

    if total_counties == 0:
        percentage = 0
    else:
        percentage = (visited_counties / total_counties) * 100

    context = {
        "total": total_counties,
        "visited": visited_counties,
        "percentage": round(percentage, 2)
    }

    return render(request, "dashboard.html", context)


    # testing